from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Fill database with test products'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        cat1 = Category.objects.create(name='Books', description='Books category')
        cat2 = Category.objects.create(name='Games', description='Games category')

        Product.objects.create(
            name='Django Book',
            description='About Django',
            category=cat1,
            price=1500
        )
        Product.objects.create(
            name='Python Book',
            description='About Python',
            category=cat1,
            price=1800
        )
        Product.objects.create(
            name='Game Guide',
            description='Guide for games',
            category=cat2,
            price=2000
        )

        self.stdout.write(self.style.SUCCESS('Test products added successfully'))