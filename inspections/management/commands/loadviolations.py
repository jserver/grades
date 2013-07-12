import csv
from datetime import datetime

from pytz import timezone

from django.core.management.base import BaseCommand

from inspections.models import Violation
from inspections.utils import clean


class Command(BaseCommand):
    args = '<violationfile>'
    help = 'Loads the database with violations'

    def handle(self, *args, **options):
        tz = timezone('America/New_York')
        with open(args[0]) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if reader.line_num == 1:
                    continue
                violation = Violation()
                violation.start_date = tz.localize(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))
                violation.end_date = tz.localize(datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S'))
                violation.critical = True if clean(row[2]) == 'Y' else False
                violation.code = clean(row[3])
                violation.desc = clean(row[4])
                violation.save()
