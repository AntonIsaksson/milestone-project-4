# Generated by Django 2.1.5 on 2020-06-05 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0014_creature_allowed_memberships'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='slug',
            field=models.SlugField(default='creature'),
        ),
    ]
