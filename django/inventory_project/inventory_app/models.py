from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('hope', 'Hope'),
        ('however', 'However'),
        ('attack', 'Attack'),
        ('citizen', 'Citizen'),
        ('type', 'Type'),
    ]
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.get_name_display()


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Foreign key linking to Category
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

