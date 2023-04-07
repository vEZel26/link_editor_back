from django.db import models
from link_editor_app.utils.enum.type_logic import LogicType
from link_editor_app.models.question import Question
from django.contrib.postgres.fields import ArrayField

class Logic(models.Model):
    type = models.CharField(
        max_length=3,
        choices=LogicType.choices,
    )
    answers = ArrayField(
                models.IntegerField(blank=True),
                size=10,
            )
    question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.CASCADE, related_name='logic')
    for_question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.CASCADE, related_name='logic_question')