from django.urls import path,include
import vlad.views

urlpatterns = [
    path('', vlad.views.main),
]