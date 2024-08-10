from django.contrib import admin
from .models import Quiz, Question, Answer, UserResponse

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = 'name',
    list_display_links = 'name',

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = 'text',
    list_display_links = 'text',

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = 'translation',
    list_display_links = 'translation',

@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = 'user',
    list_display_links = 'user',

