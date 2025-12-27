from django.db import models
# Create your models here.
from django.db import models


class MenuItem(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=100)
    cat_id = models.IntegerField()
    menu_id = models.IntegerField()

    def __str__(self):
        return self.item_name


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.order_id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    qty = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=5)


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=12, decimal_places=5)
    tips = models.DecimalField(max_digits=12, decimal_places=5)
    discount = models.DecimalField(max_digits=12, decimal_places=5)
    total_paid = models.DecimalField(max_digits=12, decimal_places=5)
    payment_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)




from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
