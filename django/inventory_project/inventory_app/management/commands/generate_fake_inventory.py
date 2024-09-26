from faker import Faker
from django.core.management.base import BaseCommand
from inventory_app.models import InventoryItem, Category, Supplier
import random

# Initialize Faker
fake = Faker()

class Command(BaseCommand):
    help = 'Generate random inventory items using the Faker library'

    def handle(self, *args, **kwargs):
        # Create some fake categories if they don't exist
        categories = [Category.objects.create(name=fake.word().capitalize()) for _ in range(5)]
        suppliers = [Supplier.objects.create(name=fake.company(), contact_info=fake.phone_number()) for _ in range(5)]

        for _ in range(50):  # Generate 50 random items
            name = fake.word().capitalize()  # Generate a random word for the item name
            description = fake.sentence()    # Generate a random sentence for description
            quantity = fake.random_int(min=1, max=1000)  # Generate a random quantity
            price = round(fake.random_number(digits=5, fix_len=False) / 100, 2)  # Generate a random price

            # Create a new InventoryItem object and save it to the database
            InventoryItem.objects.create(
                name=name,
                description=description,
                quantity=quantity,
                price=price,  # Assign a random price
                category=random.choice(categories),  # Assign a random category
                supplier=random.choice(suppliers),  # Assign a random supplier
                status=random.choice(['In Stock', 'Out of Stock'])  # Randomly choose status
            )

            # Print a success message
            self.stdout.write(self.style.SUCCESS(f"Created item: {name} with quantity: {quantity} and price: {price}"))

        self.stdout.write(self.style.SUCCESS('Successfully generated random inventory items using Faker.'))
