# Generated by Django 4.2 on 2023-04-04 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('link_editor_app', '0002_alter_logic_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='link_editor_app.question'),
        ),
        migrations.AlterField(
            model_name='logic',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logic', to='link_editor_app.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='link_editor_app.quiz'),
        ),
    ]
