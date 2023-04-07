from django.db import models
from ..models.question import Question

class Answer(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True, related_name='answer')