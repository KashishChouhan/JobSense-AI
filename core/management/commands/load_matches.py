import csv
from django.core.management.base import BaseCommand
from core.models import UserProfile, Job, JobMatch


class Command(BaseCommand):
    help = "Load job-user matches from CSV into the database"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the matches CSV file")

    def handle(self, *args, **options):
        path = options["csv_file"]

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                try:
                    user = UserProfile.objects.get(id=row["user_id"])
                    job = Job.objects.get(id=row["job_id"])

                    JobMatch.objects.create(
                        user=user,
                        job=job,
                        match_score=float(row["match_score"]),
                    )
                    count += 1
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(f"Skipping row (job {row['job_id']} user {row['user_id']}): {e}")
                    )

        self.stdout.write(self.style.SUCCESS(f"Imported {count} matches"))

