# Generated by Django 4.0.5 on 2022-07-10 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_products_available_alter_products_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]