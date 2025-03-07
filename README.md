# Django Chatroom

A chatroom web application built with Django where users can **sign up, log in, create chat rooms, and join existing rooms** to chat with other users.

## FeaturesUser 

- Authentication (Signup, Login, Logout)
- Create new chat rooms
- Join existing chat rooms
- Messages are stored in the database for chat history
- Simple and user-friendly interface
- Update and delete chat rooms
- Delete your own messages
- Update user profile

## Installation

### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django (>=4.0)
- Virtual environment (optional but recommended)

### Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/Vedant-Raulkar/Chatroom.git
   cd Chatroom
   ```

2. **Create and activate a virtual environment** (optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up the admin credentials.

6. **Run the development server**
   ```sh
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and go to:  
   ```
   http://127.0.0.1:8000/
   ```

## Usage
- **Sign up** for a new account or log in with existing credentials.
- **Create a chat room** by providing a name.
- **Update** or **delete** chat rooms if you created them.
- **Join a chat room** by selecting an existing room.
- **Send** messages and **delete** your own messages if needed.
- **Update** your profile details.
- Messages are stored in the database using the `Messages` model.


## Technologies Used
- **Django** - Backend framework
- **SQLite** - Default database (can be switched to PostgreSQL for production)
- **HTML, CSS** - Frontend styling

![home](https://github.com/user-attachments/assets/f9015328-f12b-4885-8004-d9a51cd1cba8)
![room](https://github.com/user-attachments/assets/1c7cb604-338a-4ea6-b74b-aad267746a27)
![rofile](https://github.com/user-attachments/assets/986cc202-e41f-4ec7-a032-058a124df603)



