# Generated by Django 5.0.2 on 2024-03-19 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminmodule', '0014_alter_property_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminmodule.category'),
        ),
    ]
