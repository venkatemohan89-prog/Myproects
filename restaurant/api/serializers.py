from rest_framework import serializers
from .models import Order, OrderItem, Payment, MenuItem



class OrderItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.item_name')

    class Meta:
        model = OrderItem
        fields = ['item_name', 'size', 'price', 'qty', 'total']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'payment_type', 'total_paid', 'status']


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    payments = serializers.SerializerMethodField()
    order_total = serializers.SerializerMethodField()
    total_paid = serializers.SerializerMethodField()
    outstanding = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'order_id', 'order_date', 'status',
            'items', 'payments',
            'order_total', 'total_paid', 'outstanding'
        ]

    def get_items(self, obj):
        items = OrderItem.objects.filter(order=obj)
        return OrderItemSerializer(items, many=True).data

    def get_payments(self, obj):
        payments = Payment.objects.filter(order=obj)
        return PaymentSerializer(payments, many=True).data

    def get_order_total(self, obj):
        return sum(i.total for i in OrderItem.objects.filter(order=obj))

    def get_total_paid(self, obj):
        return sum(p.total_paid for p in Payment.objects.filter(order=obj))

    def get_outstanding(self, obj):
        return self.get_order_total(obj) - self.get_total_paid(obj)


from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
