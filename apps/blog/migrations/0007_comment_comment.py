# Generated by Django 4.2.1 on 2023-05-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_user_alter_article_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='Default'),
            preserve_default=False,
        ),
    ]
