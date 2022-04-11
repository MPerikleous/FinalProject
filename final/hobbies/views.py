from django.shortcuts import render
from django.http import Http404

from django.views.generic import CreateView, UpdateView

from django.contrib.auth.views import LoginView, LogoutView
from hobbies.forms import UserForm

from django.contrib.auth.forms import UserCreationForm

from .forms import UserForm
from .models import User

def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {
        'users': users
    })

def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404('user not found')
    return render(request, 'user_detail.html', {
        'user': user
    })

class UserCreateView(CreateView):
    model = User
    success_url = "/hobbies/users"
    form_class = UserForm

class UserUpdateView(UpdateView):
    model = User
    success_url = "/hobbies/users"
    form_class = UserForm

class LoginInterfaceView(LoginView):
    template_name = 'hobbies/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'hobbies/logout.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'hobbies/register.html'
    success_url = '/hobbies'