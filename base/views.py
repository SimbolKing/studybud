from django.shortcuts import render
from .models import Room

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Learn Python!'},
    {'id': 2, 'name': 'Design with me!'},
    {'id': 3, 'name': 'Front developers'}
]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'pages/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'pages/room.html', context)
