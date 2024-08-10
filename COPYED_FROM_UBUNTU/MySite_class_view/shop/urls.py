
from django.urls import path, include
from .views import (ShopMainView,
    GroupsListView,
    order_list,
    ProductsDetailsView,
    ProductsListView,
    OrderListView,
    OrderDetailsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)
app_name = "shop"
urlpatterns = [
    # strting from shop/ф
    path('', ShopMainView.as_view()),
    path('groups/', GroupsListView.as_view()),
    path('orders/', OrderListView.as_view(), name="order_list"),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/', ProductsListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductsDetailsView.as_view(), name='product_details'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/archive/', ProductDeleteView.as_view(), name='product_delete'),
    path('orders/<int:pk>/', OrderDetailsView.as_view(), name="order_details"),
]
