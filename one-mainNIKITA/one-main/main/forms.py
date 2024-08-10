from django import forms
from .models import Room, Post, News

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']