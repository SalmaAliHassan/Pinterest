from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import User

class UserList(ListView):
    model = User 

class UserDetail(DetailView):
    model = User 
