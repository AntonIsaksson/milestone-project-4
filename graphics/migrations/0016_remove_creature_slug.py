# Generated by Django 2.1.5 on 2020-06-05 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0015_creature_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creature',
            name='slug',
        ),
    ]