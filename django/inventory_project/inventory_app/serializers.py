from rest_framework import serializers
from .models import InventoryItem, Category

class InventoryItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    supplier = serializers.CharField(source='supplier.name', read_only=True)

    class Meta:
        model = InventoryItem
        fields = [
            'id', 'name', 'description', 'quantity', 'price', 'status', 
            'created_at', 'updated_at', 'category', 'supplier'
        ]


class CategorySerializer(serializers.ModelSerializer):
    name_display = serializers.CharField(source='get_name_display', read_only=True)  # Display the human-readable version

    class Meta:
        model = Category
        fields = ['id', 'name', 'name_display']