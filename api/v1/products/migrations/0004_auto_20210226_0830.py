# Generated by Django 2.2.13 on 2021-02-26 08:30

from django.db import migrations, models
import django_postgres_extensions.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210226_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='more_prop',
            field=django_postgres_extensions.models.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, null=True, size=None),
        ),
    ]
