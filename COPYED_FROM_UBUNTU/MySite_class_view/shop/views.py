import django.http
from django.contrib.auth.models import Group ,Us
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin, UserPassesTestMixin
from .models import Order, Product
from .forms import ProductForm, GroupForm


# Create your views here.
class ShopMainView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
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


# def main(request):

class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': GroupForm(),
            'groups': Group.objects.prefetch_related('permissions').all(),
            # prefetch_related('permissions') - для оптимизации
        }
        return render(request, template_name='shop/groups.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)


# def groups_list(request: django.http.HttpRequest):
class OrderListView(LoginRequiredMixin,ListView):
    template_name = 'shop/order-list.html'
    model = Order
    context_object_name = 'orders'


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
    return render(request, 'shop/order-list.html', context=context)


class ProductsListView(TemplateView):
    template_name = 'shop/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context


"""def product_list(request: HttpRequest) -> HttpResponse:
    context = {
        'products': Product.objects.all(),
    }
    return render(request,'shop/product_list.html',context=context)"""


class ProductsDetailsView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        product = get_object_or_404(Product, pk=pk)
        context = {
            'product': product,
        }
        return render(request, 'shop/product-details.html', context=context)


class OrderDetailsView(PermissionRequiredMixin,DetailView):
    permission_required = ["view_order"]
    template_name = 'shop/order-details.html'
    model = Order
    context_object_name = 'order'


class ProductCreateView(UserPassesTestMixin,CreateView):
    def test_func(self):
        #return self.request.user.groups.filter(name = "secret-group").exists()
        return  self.request.user.is_superuser
    model = Product
    fields = 'name', 'price', 'brand', 'desc','preview'
    # form_class = ProductForm
    success_url = reverse_lazy('shop:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = 'name', 'price', 'brand', 'desc', 'category', 'archived', 'country_manuf','preview'
    # form_class = ProductForm
    template_name_suffix = '_update_form'

    success_url = reverse_lazy('shop:product_list')

    def get_success_url(self):
        return reverse(
            'shop:product_details',
            kwargs={'pk': self.object.pk}
        )
"""
def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data["name"]
            # price = form.cleaned_data["price"]
            # desc = form.cleaned_data['desc']
            # Product.objects.create(name=name,price = price,desc=desc)
            form.save()
            url = reverse('shop:product_list')
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, 'shop/create-product.html', context=context)"""


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shop:product_list')

    """def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)"""