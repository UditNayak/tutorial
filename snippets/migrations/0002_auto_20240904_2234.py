# Generated by Django 3.2.25 on 2024-09-04 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='highlighted',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
    ]
