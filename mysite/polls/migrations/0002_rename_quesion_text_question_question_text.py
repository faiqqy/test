# Generated by Django 5.0.7 on 2024-08-06 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quesion_text',
            new_name='question_text',
        ),
    ]
