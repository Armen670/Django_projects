from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .admin_mixins import ExportAsCSVMixin

from .models import Order,Product

class OrderInline(admin.TabularInline):
    model = Product.orders.through

@admin.action(description="Archive products")
def mark_archived(modeladmin: admin.ModelAdmin , request: HttpRequest , queryset: QuerySet):
    queryset.update(archived = True)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin,ExportAsCSVMixin):
    actions = [
        mark_archived,
        "export_csv"
    ]
    inlines = [OrderInline]
    list_display = 'pk','name', 'desc_short' , 'price','category','archived'
    list_display_links = 'pk','name', 'desc_short' , 'price','category'
    ordering = '-pk',
    search_fields = 'delivery_addres',
    fieldsets = [
        (None,{
            'fields': ('name' , 'desc'),
        }),
        ("Price options",{
            'fields': ('price',),
            'classes' : ('wide',), #extrapretty collapse
            'description' : "Some information...",
        })
    ]

    def desc_short(self,obj: Product) -> str:
        if (len(obj.desc) > 25):
            return obj.desc[0:22]+ '...'
        return obj.desc

    def __str__(self) -> str:
        return f"Order(pk={self.pk})"


class ProductInline(admin.TabularInline):
    model = Order.products.through

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = 'pk','delivery_addres_short', 'promocode' , 'created_at','user_verbose'
    list_display_links = 'pk','delivery_addres_short',
    ordering = '-pk',
    search_fields = 'delivery_addres',
    def delivery_addres_short(self,obj: Order) -> str:
        if (len(obj.delivery_addres) > 25):
            return obj.delivery_addres[0:22]+ '...'
        return obj.delivery_addres

    def __str__(self) -> str:
        return f"Order(pk={self.pk})"

    def user_verbose(self,obj : Order) -> str:
        return obj.user.first_name or obj.user.username


