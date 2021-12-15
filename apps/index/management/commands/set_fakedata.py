from django_seed import Seed
from faker.generator import random
from apps.index.models import Spa
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        seeder = Seed.seeder('en_us')
        seeder.add_entity(Spa, 20, {
            'created_at': lambda x: seeder.faker.date(),
            'name': lambda x: seeder.faker.name(),
            'count': lambda x: random.randint(1,20),
            'distance': lambda x: random.randint(1,20),
        })
        seeder.execute()
        # print('data set to table')