from faker import Faker
from django.core.management.base import BaseCommand
from inventory_app.models import InventoryItem, Category, Supplier

fake = Faker()

class Command(BaseCommand):
    help = 'Generate random inventory items using the Faker library'

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        suppliers = Supplier.objects.all()

        for _ in range(50):  # Generate 50 random items
            name = fake.word().capitalize()
            description = fake.sentence()
            quantity = fake.random_int(min=1, max=1000)
            price = round(fake.random_number(digits=5, fix_len=False) / 100, 2)
            category = fake.random_element(categories)
            supplier = fake.random_element(suppliers)

            InventoryItem.objects.create(
                name=name,
                description=description,
                quantity=quantity,
                price=price,
                category=category,
                supplier=supplier
            )
            self.stdout.write(self.style.SUCCESS(f"Created item: {name}, category: {category.name}, supplier: {supplier.name}"))

        self.stdout.write(self.style.SUCCESS('Successfully generated random inventory items.'))
