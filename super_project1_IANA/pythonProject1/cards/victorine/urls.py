from django.urls import path
from .views import index, quiz_detail, answer_detail , quiz_list

app_name = 'victorine'
urlpatterns = [
    path("index/", index),
    path('index/quiz_list/', quiz_list, name='quiz_list'),
    path('index/quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),
    path('question/<int:answer_id>/', answer_detail, name='answer_detail'),
]