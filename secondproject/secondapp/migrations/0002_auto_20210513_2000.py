# Generated by Django 3.2.3 on 2021-05-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Class', models.IntegerField()),
                ('Major', models.CharField(max_length=100)),
                ('Hobby', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Object',
        ),
    ]
