from django.urls import path,include
import shop.views
app_name = "shop"
urlpatterns = [
    #strting from shop/
    path('',shop.views.main),
    path('groups/',shop.views.groups_list),
    path('orders/', shop.views.order_list,name = "order_list"),
    path('products/create/', shop.views.create_product,name= 'product_create'),

]