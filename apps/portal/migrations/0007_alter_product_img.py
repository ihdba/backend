# Generated by Django 4.2.1 on 2023-07-03 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_alter_product_description_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.FileField(upload_to='products'),
        ),
    ]
