# Generated by Django 3.2.3 on 2021-05-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albamonapp', '0002_auto_20210522_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='information',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='job',
            field=models.TextField(max_length=200),
        ),
    ]
