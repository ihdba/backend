# Generated by Django 4.2.1 on 2023-06-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_exercise_repetitions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
