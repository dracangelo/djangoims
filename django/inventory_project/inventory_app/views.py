from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from .models import InventoryItem
from .serializers import InventoryItemSerializer

class InventoryListView(APIView):
    def get(self, request):
        items = InventoryItem.objects.all()

        category = request.query_params.get('category', None)
        status = request.query_params.get('status', None)

        if category:
            items = items.filter(category=category)  # Adjust based on your model
        if status:
            items = items.filter(status=status)

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(items, request)
        serializer = InventoryItemSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    @action(detail=True, methods=['patch'])
    def restock(self, request, pk=None):
        item = self.get_object()
        quantity = request.data.get('quantity', 0)
        try:
            quantity = int(quantity)
        except ValueError:
            return Response({"error": "Invalid quantity"}, status=status.HTTP_400_BAD_REQUEST)
        
        if quantity > 0:
            item.quantity += quantity
            item.save()
            return Response({'status': 'Item restocked', 'new_quantity': item.quantity})
        else:
            return Response({"error": "Quantity must be greater than 0"}, status=status.HTTP_400_BAD_REQUEST)
