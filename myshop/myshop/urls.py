"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# myshop/urls.py
from django.contrib import admin

from django.urls import path, include

from accounts.views import register
from orders.views import main_page, orders_page
from products.views import product_list

from django.contrib.auth.urls import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main_page'),
    path('orders/', orders_page, name='orders_page'),
    path('cart/', include('cart.urls')),  # Включаем маршруты для корзины
    path('products/', product_list, name='product_list'),
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),  # Включение стандартных представлений Django для авторизации
]