from django.db import models
from django.contrib import admin

class Category(models.Model) :
    category_text = models.CharField(max_length=200)

    def __str__(self) :
        return self.category_text

class Product(models.Model) :
    product_title = models.CharField(max_length=200)
    product_category = models.ForeignKey(Category, default=0, on_delete=models.CASCADE)
    product_text = models.CharField(max_length=200, blank=True)
    price = models.FloatField(default=0)
    product_amount = models.IntegerField(default=0)
    product_numbering = models.IntegerField(default=0)
    @admin.display(
            boolean=True,
            ordering="product_amount",
            description="In Stock?",
    )

    def __str__(self) :
        return self.product_title 
    
class Stock(models.Model) :
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE) 
    product_price = models.FloatField(default=0)
    product_amount = models.IntegerField(default=0)

    def __str__(self) :
        return self.product_name.product_title

class Order(models.Model) :
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)

    def __str__(self) :
        return self.amount + self.total_price

