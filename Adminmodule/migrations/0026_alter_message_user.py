# Generated by Django 5.0.2 on 2024-03-24 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminmodule', '0025_rename_timestamp_message_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.IntegerField(),
        ),
    ]
