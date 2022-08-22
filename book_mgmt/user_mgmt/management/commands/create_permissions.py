from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create custom permissions'

    def handle(self, *args, **options):
        content_type, created = ContentType.objects.get_or_create(app_label='user_mgmt', model='custom_permission')

        custom_permissions = [
            {
                'name': 'Book Management Permission',
                'content_type': content_type,
                'codename': 'book_mgmt_perm',
            }
        ]

        for perm in custom_permissions:
            name = perm['name']
            content_type = perm['content_type']
            codename = perm['codename']
            Permission.objects.get_or_create(name=name, content_type=content_type, codename=codename)
            print(perm['name'])
