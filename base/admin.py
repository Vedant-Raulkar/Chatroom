from django.contrib import admin

# Register your models here.
from .models import Room, Messages, Topic, User

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Messages)
admin.site.register(Topic)

