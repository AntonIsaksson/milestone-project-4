# Generated by Django 2.1.5 on 2020-06-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0027_remove_designs_landscape_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='designs',
            name='type',
            field=models.CharField(choices=[('forest', 'Forest'), ('dessert', 'Dessert'), ('city', 'City'), ('mountains', 'Mountains'), ('other', 'Other')], default='Neutral', max_length=30),
        ),
    ]
