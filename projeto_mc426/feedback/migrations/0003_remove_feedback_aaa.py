# Generated by Django 4.2 on 2023-12-13 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedback_aaa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='aaa',
        ),
    ]