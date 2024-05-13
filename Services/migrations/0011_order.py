# Generated by Django 5.0.3 on 2024-04-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0010_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('spname', models.CharField(max_length=100)),
                ('service_id', models.CharField(max_length=100)),
                ('phno', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('pay_method', models.CharField(max_length=100)),
                ('add1', models.CharField(max_length=255)),
                ('add2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=20)),
                ('message', models.TextField(blank=True, null=True)),
                ('qty', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('placed_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
