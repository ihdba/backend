# Generated by Django 4.2.1 on 2023-06-29 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='repetitions',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
