# Generated by Django 4.2 on 2023-04-05 08:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link_editor_app', '0003_alter_answer_question_alter_logic_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logic',
            name='answers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=10),
        ),
    ]
