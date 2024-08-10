from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shop.models import  Order

address = """23 Serenity Lane, Willow Springs, Azure Valley, CA 90210
Rosewood Manor, 7 Tranquil Terrace, Harmony Hills, TX 75001
10 Evergreen Court, Whispering Pines, Meadowbrook Meadows, FL 33160
Ivy Cottage, 15 Meadowview Lane, Riverside Meadows, GA 30303
Sunflower Villa, 42 Sunnyvale Street, Sunshine Heights, NV 89123
18 Riverbank Road, Brookside Bend, Waterside Estates, NY 10001
Maplewood Retreat, 5 Peaceful Path, Harmony Haven, CO 80020
Lavender Lane, 33 Serene Street, Tranquil Town, IL 60601
Oakwood Oasis, 12 Serenity Springs, Whispering Woods, AZ 85001
Willow Cottage, 8 Blissful Boulevard, Serenity Springs, WA 98101"""

promocods = """BLISSFUL15
SPARKLE20
ENCHANT10
GLOWING25
RADIANT30
DREAMY40
WHIMSICAL50
SERENE60
MAGICAL75
ETHEREAL80"""

class Command(BaseCommand):
    """
    creating order
    """
    def handle(self,*args,**kwargs):
        self.stdout.write("Create order")
        address_list = address.split('\n')
        promocods_list = promocods.split('\n')
        asd = User.objects.get(username= 'admin')
        for i in range(0,10):
            order = Order.objects.get_or_create(
                delivery_addres =address_list[i],
                promocode = promocods_list[i],
                user =  asd,
            )
            self.stdout.write(f" Create order { order}")