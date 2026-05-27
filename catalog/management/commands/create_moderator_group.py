from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from catalog.models import Product


class Command(BaseCommand):
    help = 'Create group "Модератор продуктов" and assign permissions'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        content_type = ContentType.objects.get_for_model(Product)

        unpublish_perm = Permission.objects.get(
            codename='can_unpublish_product',
            content_type=content_type
        )

        delete_perm = Permission.objects.get(
            codename='delete_product',
            content_type=content_type
        )

        group.permissions.set([unpublish_perm, delete_perm])
        group.save()

        if created:
            self.stdout.write(self.style.SUCCESS('Group created and permissions assigned'))
        else:
            self.stdout.write(self.style.SUCCESS('Group updated and permissions assigned'))