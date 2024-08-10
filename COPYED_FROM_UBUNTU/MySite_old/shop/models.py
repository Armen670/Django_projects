from django.db import models
from django.contrib.auth.models import  User



# Create your models here.

class Product(models.Model):
    class Meta:
        ordering = ['-name']
        #db_table = 'some_products'
        verbose_name_plural = 'products'
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=0,max_digits=10)
    category = models.CharField(max_length=50,default='default')
    brand = models.CharField(max_length=50,default='noname')
    country_manuf = models.CharField(max_length=50,default ='earth')
    archived = models.BooleanField(default=False)


class Order(models.Model):
    delivery_addres = models.TextField(null = True,blank=True)
    promocode = models.CharField(max_length=20, null = False, blank = True)
    created_at= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")

    """@property
    def delivery_addres_short(self) -> str:
        if (len(self.delivery_addres) < 15):
            return self.delivery_addres[0:12]+ '...'
        return self.delivery_addres
    def __str__(self) -> str:
        return f"Order(pk={self.pk})"
        """