from collections import Counter
import csv
import os.path

from django.core.management.base import BaseCommand
from dashboard import models


class Command(BaseCommand):
    help = "Import data from csv file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=open, help="Path to csv file")

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        reader = csv.DictReader(csv_file)
        c = Counter()
        for row in reader:
            models.Barcode.objects.create(
                barcode=row['barcode'],
                name=row['name'],
            )
            c['barcode'] += 1
        self.stdout.write(self.style.SUCCESS('Successfully imported data'))
        self.stdout.write(self.style.SUCCESS(f'Imported {c["barcode"]} barcodes'))
