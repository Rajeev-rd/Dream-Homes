# Generated by Django 5.0.2 on 2024-04-02 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminmodule', '0031_alter_renovation_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renovation',
            name='name',
        ),
    ]