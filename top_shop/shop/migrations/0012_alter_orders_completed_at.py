# Generated by Django 5.0 on 2023-12-26 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_orders_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='completed_at',
            field=models.DateTimeField(),
        ),
    ]
