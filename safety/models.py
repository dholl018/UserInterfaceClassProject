from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class SafetyReport(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    anonymous = models.BooleanField(default=False)
    location = models.CharField(max_length=30)
    like = models.IntegerField(default=0)
    author = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    mod_Locked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Safety:report-details', args=[self.id])


class CommentSection(models.Model):
    report = models.ForeignKey(SafetyReport, related_name="comments",  on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    attached_report = models.IntegerField(default=0)

    def __str__(self):
        return self.report.title

    def get_absolute_url(self):
        return reverse('Safety:report-details', args=[self.attached_report])


class UserNameDatabase(models.Model):
    username = models.CharField(max_length=30)

# class SafetyReport:
#     def __init__(self, id, title, description, location, author, date_posted, comment, like):
#         self.id = id
#         self.title = title
#         self.description = description
#         self.location = location
#         self.author = author
#         self.date_posted = date_posted
#         self.comment = comment
#         self.like = like
#
#
# report1 = SafetyReport(
#     1,
#     "Metal bracket protruding from pallet",
#     "Employee was walking through warehouse. As he walked past a pallet a metal bracket snagged his pants.",
#     "Warehouse",
#     "ssmith",
#     datetime.now(),
#     0,
#     0,
# )
#
# report2 = SafetyReport(
#     2,
#     "Moisture Analyzer leaking Nitrogen",
#     "During install of new equipment. Analyist noticed there was a leak. As an immediate action the instrument was shut down and lines closed.",
#     "Lab",
#     "Casey Stine",
#     "August 17, 2021",
#     0,
#     0,
# )
#
# report3 = SafetyReport(
#     3,
#     "Unlabelled Chemical",
#     "Found an unlabeled Chemical in the Lab. It is dangerous to leave samples unlabeled and unattended to.",
#     "Lab 2",
#     "Anonymous",
#     "August 17, 2021",
#     0,
#     0,
# )
#
#
# new_report = []

regular_user = {"username": "ssmith", "password": "Qwerty1a"}
admin_user = {"username": "admin", "password": "Adminpas1"}

