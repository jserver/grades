import csv
from datetime import datetime

from pytz import timezone

from django.core.management.base import BaseCommand

from inspections.models import WebExtract
from inspections.utils import clean


class Command(BaseCommand):
    args = '<extractfile>'
    help = 'Loads the database with extracts'

    def handle(self, *args, **options):
        tz = timezone('America/New_York')
        with open(args[0]) as csvfile:
            reader = csv.reader(csvfile)
            rows = []
            for row in reader:
                if reader.line_num == 1:
                    continue
                web_extract = WebExtract()
                web_extract.camis = clean(row[0])
                web_extract.dba = clean(row[1])
                web_extract.boro = int(row[2])
                web_extract.building = clean(row[3])
                web_extract.street = clean(row[4])
                web_extract.zip_code = clean(row[5])
                web_extract.phone = clean(row[6])
                if row[7]:
                    web_extract.cuisine_code_id = clean(row[7])
                web_extract.insp_date = tz.localize(datetime.strptime(row[8], '%Y-%m-%d %H:%M:%S'))
                web_extract.action = clean(row[9])
                web_extract.viol_code = clean(row[10])
                web_extract.score = clean(row[11])
                web_extract.current_grade = clean(row[12])
                if row[13]:
                    web_extract.grade_date = tz.localize(datetime.strptime(row[13], '%Y-%m-%d %H:%M:%S'))
                web_extract.record_date = tz.localize(datetime.strptime(row[14], '%Y-%m-%d %H:%M:%S.%f000'))
                rows.append(web_extract)
                if reader.line_num % 500 == 0:
                    print reader.line_num
                    WebExtract.objects.bulk_create(rows)
                    rows = []
