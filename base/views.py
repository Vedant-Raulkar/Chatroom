from django.shortcuts import render, redirect
from .models import Room, Topic, Messages, User
from .forms import RoomForm, Userform, MyUserCreationForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


# rooms = [
#     {'id': 1, 'name':'avads'},
#     {'id': 2, 'name':'bcx'},
#     {'id': 3, 'name':'qer'},

# ]


def loginpage(request):
   
    if request.user.is_authenticated:
         return redirect('home')
   
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')  

        user = authenticate(request, email=email, password=password)  

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    context = {}
    return render(request, 'base/loginuser.html', context)

def logoutuser(request):
     logout(request)
     return redirect('home')


def registerpage(request):
     form = MyUserCreationForm()
     if request.method == 'POST':
          form = MyUserCreationForm(request.POST)
          if form.is_valid():
               user = form.save(commit=False)
               user.username = user.username.lower()
               user.save()
               login(request, user)
               return redirect('home')
          else:
               messages.error(request, 'An error ocurred during registration')
     context={'form':form}
     return render(request, 'base/register.html', context)


def Home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
         Q(topic__name__icontains=q) |
         Q(name__icontains=q) |
         Q(description__icontains=q) |
         Q(host__username__icontains=q)
         )
    room_count = rooms.count()
    topics = Topic.objects.all()
    room_messages = Messages.objects.filter(Q(room__topic__name__icontains=q))
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)


def room(request, pk):
    rooms = Room.objects.get(id=pk)
    room_messages = rooms.messages_set.all()
    participants = rooms.participants.all()
   
    if request.method == 'POST':
         message = Messages.objects.create(
              user=request.user,
              room=rooms,
              message=request.POST.get('body')
         )
         rooms.participants.add(request.user)
         return redirect('room', pk=rooms.id)
    context = {'rooms': rooms, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/room.html', context)

@login_required(login_url='/login')
def userprofile(request, pk):
     user = User.objects.get(id=pk)
     rooms = user.room_set.all()
     room_messages = user.messages_set.all()
     topics = Topic.objects.all()
     context={'user': user, 'rooms': rooms, 'topics': topics , 'room_messages': room_messages}
     return render(request, 'base/profile.html', context)


@login_required(login_url='/login')
def createroom(request):
        form = RoomForm()
        topics=Topic.objects.all()
        if request.method == 'POST':
             topic_name=request.POST.get('topic')
             topic, created = Topic.objects.get_or_create(name=topic_name)

             Room.objects.create(
                  host=request.user,
                  topic=topic,
                  name=request.POST.get('name'),
                  description=request.POST.get('description'),
             )
             return redirect('home')
       
        context={'form': form , 'topics': topics}
        return render(request, 'base/createroom.html', context)


@login_required(login_url='/login')
def updateroom(request, pk):
     room = Room.objects.get(id=pk)
     form = RoomForm(instance=room)
     topics=Topic.objects.all()

     if request.user != room.host:
          return HttpResponse('You do not own this room')
     
     if request.method =='POST':
          topic_name=request.POST.get('topic')
          topic, created = Topic.objects.get_or_create(name=topic_name)
          room.name = request.POST.get('name')
          room.topic = topic
          room.description = request.POST.get('description')
          room.save()

          return redirect('home')
     context={'form':form , 'topics': topics, 'room': room}
     return render(request, 'base/createroom.html', context)


@login_required(login_url='/login')
def deleteroom(request, pk):
     room = Room.objects.get(id=pk)

     if request.user != room.host:
          return HttpResponse('You do not own this room')
     
     if request.method == 'POST':
          room.delete()
          return redirect('home')
     context={'obj':room}
     return render(request, 'base/delete.html', context)


@login_required(login_url='/login')
def deleteMessage(request, pk):
     message = Messages.objects.get(id=pk)
     
     if request.method == 'POST':
          message.delete()
          return redirect('home')
     context={'obj':message}
     return render(request, 'base/delete.html', context)


@login_required(login_url='/login')
def UpdateUser(request):
     user = request.user
     form=Userform(instance=user)

     if request.method == 'POST':
          form = Userform(request.POST,request.FILES, instance=user)
          if form.is_valid():
               form.save()
               return redirect('profile', pk=user.id)
     context={'form': form}
     return render(request, 'base/updateuser.html', context)


def topicspage(request):
     q = request.GET.get('q') if request.GET.get('q') != None else ''
     topics = Topic.objects.filter(name__icontains=q)
     
     context={'topics':topics}
     return render(request, 'base/topics.html',context)

def activitypage(request):
     room_messages=Messages.objects.all()
     context={'room_messages': room_messages}
     return render(request, 'base/activity.html', context)