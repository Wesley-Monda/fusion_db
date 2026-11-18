import uuid
from asyncio.windows_events import NULL

from django.db import models

def gen_unique_path(instance, filename):
    ext = filename.split('.')[-1]  # Jane.png ['Jane', 'png']
    newfilename = f'{uuid.uuid4()}.{ext}'
    return f'products/{newfilename}'
# Create your models here.
# MVT
# MVC

CATEGORIES = [
    ('Food', 'Food Category'),
    ('Drinks', 'Drinks Category'),
    ('Cleaning', 'Cleaning Category'),
    ('Fruits', 'Fruits Category'),
    ('Hardware', 'Hardware Category'),
]
class Product(models.Model):
    name = models.CharField(max_length=100)
    code =models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    for_sale = models.BooleanField(default=False)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    pic =models.ImageField(upload_to=gen_unique_path,default='products/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True) # Once during the creation of a product
    updated_at = models.DateTimeField(auto_now=True) # Everytime update happens
    class Meta:
        db_table = 'products'

# Run Migrations
# python manage.py makemigrations
# python manage.py migrate
# Python manage.py createsuperuser

