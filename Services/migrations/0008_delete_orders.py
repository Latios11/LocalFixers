# Generated by Django 5.0.3 on 2024-04-07 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0007_alter_orders_total_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
