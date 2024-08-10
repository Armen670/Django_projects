from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Room, Post, News
from .forms import RoomForm, PostForm, NewsForm
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    rooms = Room.objects.all()
    return render(request, 'main/index.html', {'rooms': rooms})


def news_list(request):
    news = News.objects.all().order_by('-created_date')
    return render(request, 'main/news_list.html', {'news': news})

@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'main/add_news.html', {'form': form})

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'main/news_detail.html', {'news': news})

def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    posts = room.posts.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.room = room
            post.save()
            return redirect('room_detail', room_id=room.id)
    else:
        form = PostForm()
    return render(request, 'main/room_detail.html', {'room': room, 'posts': posts, 'form': form})

@login_required
def new_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.author = request.user
            room.save()
            return redirect('index')
    else:
        form = RoomForm()
    return render(request, 'main/new_room.html', {'form': form})


def reg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/reg.html', {'form': form})

def logout_view(request):
    print("asdasdasdasd")
    logout(request)
    print("login        asdasdasdasd    login")
    return HttpResponseRedirect(reverse("main:login"))