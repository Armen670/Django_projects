import django.http
from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect,reverse
from .models import Order, Product
from .forms import ProductForm


# Create your views here.
def main(request):
    products = [
        ('Smartphone', 12999),
        ('Laptop', 129999),
        ('Desktop', 59999),
        ('Headphones', 5999),

    ]
    context = {
        'products': products,
    }
    return render(request, template_name='shop/index.html', context=context)


def groups_list(request: django.http.HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
        # prefetch_related('permissions') - для оптимизации
    }
    return render(request, template_name='shop/groups.html', context=context)


def order_list(request: HttpRequest):
    context = {
        'orders': Order.objects.all(),  # select_related('user') - для оптимизации
        # 'asd': Order.objects.select_related('user').all().products.through,
    }
    """for i,order in enumerate(context['orders']):
        print(f"{i}: {order.products}")
        print(type(order.products))
        #print(f"{i}: {order.products.all()}")
        for j in order.products.all():
            print(j.name)
            print(j.desc)
            print(j.price)
            print(j.category)"""
    """name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=0,max_digits=10)
    category = models.CharField(max_length=50,default='default')
    brand = models.CharField(max_length=50,default='noname')
    country_manuf = models.CharField(max_length=50,default ='earth')
    archived
    """
    # print(context['orders'].get(pk= 1).products.all())
    """for i in context['orders'].get(pk= 1).products.all():
        print(i.name)"""
    return render(request, 'shop/orders-list.html', context=context)

def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            #name = form.cleaned_data["name"]
            #price = form.cleaned_data["price"]
            #desc = form.cleaned_data['desc']
            #Product.objects.create(name=name,price = price,desc=desc)
            form.save()
            url = reverse('shop:order_list')
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        "form": form
    }
    url = reverse("shop:order_list")
    return render(request,'shop/create-product.html',context=context)
