from django.db import models
from link_editor_app.models.quiz import Quiz

class Question(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    quiz = models.ForeignKey(Quiz, null=True, blank=True, related_name='question', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']