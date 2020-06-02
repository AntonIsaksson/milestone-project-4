# Generated by Django 2.1.5 on 2020-06-01 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0007_landscape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('AC', 'Animated Creatures'), ('AO', 'Animated Objects'), ('L', 'Landscapes')], default='Animated Creatures', max_length=20),
        ),
        migrations.AlterField(
            model_name='creature',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/creatures'),
        ),
        migrations.AlterField(
            model_name='landscape',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/landscapes'),
        ),
        migrations.AlterField(
            model_name='object',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/objects'),
        ),
    ]