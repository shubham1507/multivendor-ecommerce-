# Generated by Django 2.2.13 on 2021-03-24 04:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210324_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cancelledOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 24, 4, 3, 47, 859811)),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(default=uuid.UUID('ef3ae83c-8c55-11eb-b6a4-bf49158d9246'), on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer'),
        ),
    ]
