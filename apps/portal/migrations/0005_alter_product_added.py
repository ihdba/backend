# Generated by Django 4.2.1 on 2023-07-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_remove_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
