import csv

from django.core.management.base import BaseCommand

from inspections.models import Cuisine
from inspections.utils import clean


class Command(BaseCommand):
    args = '<cuisinefile>'
    help = 'Loads the database with cuisines'

    def handle(self, *args, **options):
        with open(args[0]) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if reader.line_num == 1:
                    continue
                cuisine = Cuisine()
                cuisine.code = clean(row[0])
                cuisine.desc = clean(row[1])
                cuisine.save()
