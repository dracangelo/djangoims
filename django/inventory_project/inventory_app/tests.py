from django.test import TestCase
from .models import InventoryItem

class InventoryItemTestCase(TestCase):
    def setUp(self):
        InventoryItem.objects.create(name="Laptop", quantity=10, price=1500, category="Electronics", status="In Stock")
        InventoryItem.objects.create(name="Chair", quantity=0, price=45, category="Furniture", status="Out of Stock")

    def test_inventory_item_str(self):
        item = InventoryItem.objects.get(name="Laptop")
        self.assertEqual(str(item), 'Laptop')

    def test_out_of_stock(self):
        chair = InventoryItem.objects.get(name="Chair")
        self.assertEqual(chair.status, "Out of Stock")

    def test_restock_item(self):
        laptop = InventoryItem.objects.get(name="Laptop")
        laptop.quantity += 5
        laptop.save()
        self.assertEqual(laptop.quantity, 15)
