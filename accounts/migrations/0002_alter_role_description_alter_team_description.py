# Generated by Django 5.0.6 on 2024-05-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='description',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.CharField(max_length=256),
        ),
    ]
