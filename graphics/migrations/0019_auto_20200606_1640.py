# Generated by Django 2.1.5 on 2020-06-06 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('graphics', '0018_auto_20200606_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landscape',
            old_name='main_color',
            new_name='color',
        ),
        migrations.AddField(
            model_name='landscape',
            name='allowed_memberships',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Membership'),
        ),
        migrations.AddField(
            model_name='object',
            name='allowed_memberships',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Membership'),
        ),
        migrations.AlterField(
            model_name='landscape',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='object',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
