
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderList(APIView):
    permission_classes = [IsAuthenticated]  # protect the endpoint

    def get(self, request):
        orders = Order.objects.all()
        data = OrderSerializer(orders, many=True).data
        return Response(data)
    





