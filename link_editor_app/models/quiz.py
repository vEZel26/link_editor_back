from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    date_of_ending = models.DateField(blank=True, null=True)