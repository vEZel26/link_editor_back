# Generated by Django 4.2 on 2023-04-05 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link_editor_app', '0004_alter_logic_answers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['id']},
        ),
    ]
