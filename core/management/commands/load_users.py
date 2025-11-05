import csv
from django.core.management.base import BaseCommand
from core.models import UserProfile


class Command(BaseCommand):
    help = "Load users from CSV into the database"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the users CSV file")

    def handle(self, *args, **options):
        path = options["csv_file"]

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                UserProfile.objects.create(
                    name=row["name"],
                    skills=row["skills"],
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f"Imported {count} users"))
