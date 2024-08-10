from django.core.management import BaseCommand
from shop.models import Product
class Command(BaseCommand):
    """
    creating products
    """
    def handle(self,*args,**kwargs):
        self.stdout.write("Create products")

        product = Product.objects.get_or_create(name= 'asd',price = 123)
        self.stdout.write(self.style.SUCCESS('Product created'))