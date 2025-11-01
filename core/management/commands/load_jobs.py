from django.core.management.base import BaseCommand
import csv
from core.models import Job

class Command(BaseCommand):
    help = "Load jobs from CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def handle(self, *args, **options):
        path = options["csv_file"]
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                Job.objects.create(
                    title=row.get("title", ""),
                    company=row.get("company", ""),
                    location=row.get("location", ""),
                    salary=row.get("salary_range", ""),        # your CSV has salary_range
                    skills=row.get("required_skills", ""),     # your CSV has required_skills
                    description=row.get("job_description", ""),# your CSV has job_description
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f"Imported {count} jobs"))
