from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
            class User:
                model = User
                fields = ['username ','email','password','contractnumber'] 