# Create your models here.
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    salary = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    experience = models.CharField(max_length=100, null=True, blank=True)
    skills = models.CharField(max_length=500, help_text="Comma-separated skills (e.g., python, sql, excel)")

    def __str__(self):
        return self.title
# New model for Users
class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    skills = models.TextField()
    
    def __str__(self):
        return self.name


# New model for Job ↔ User matches
class JobMatch(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    match_score = models.FloatField()
 # new fields
    matched_skills = models.TextField(blank=True, null=True)
    missing_skills = models.TextField(blank=True, null=True)
    recommended_resources = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.name} → {self.job.title} ({self.match_score}%)"