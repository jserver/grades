import csv
from datetime import datetime

from pytz import timezone

from django.core.management.base import BaseCommand

from inspections.models import Action


class Command(BaseCommand):
    args = '<actionfile>'
    help = 'Loads the database with actions'

    def handle(self, *args, **options):
        tz = timezone('America/New_York')
        with open(args[0]) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if reader.line_num == 1:
                    continue
                action = Action()
                action.start_date = tz.localize(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
                action.end_date = tz.localize(datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S'))
                action.code = row[2].strip()
                action.desc = row[3].strip()
                action.save()
