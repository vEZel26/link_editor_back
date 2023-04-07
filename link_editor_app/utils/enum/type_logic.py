from django.db import models


class LogicType(models.TextChoices):

    ANY = 'ANY', 'Any_question'
    CER = 'CER', 'Certain',
