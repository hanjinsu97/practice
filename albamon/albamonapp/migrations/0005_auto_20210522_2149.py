# Generated by Django 3.2.3 on 2021-05-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albamonapp', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='applicant',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pay',
            field=models.PositiveIntegerField(default=8720),
        ),
    ]
