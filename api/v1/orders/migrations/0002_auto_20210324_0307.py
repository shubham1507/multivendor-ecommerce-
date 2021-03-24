# Generated by Django 2.2.13 on 2021-03-24 03:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cancelledOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 24, 3, 7, 20, 697490)),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(default=uuid.UUID('0c52ee22-8c4e-11eb-a16d-e726c1aceb31'), on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer'),
        ),
    ]
