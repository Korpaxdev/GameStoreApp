# Generated by Django 5.0.1 on 2024-01-31 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name="Цена"),
        ),
    ]
