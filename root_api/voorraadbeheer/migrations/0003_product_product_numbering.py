# Generated by Django 4.0.7 on 2023-05-14 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voorraadbeheer', '0002_product_product_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_numbering',
            field=models.IntegerField(default=0),
        ),
    ]