# Generated by Django 5.0.2 on 2024-03-24 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminmodule', '0026_alter_message_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='user_ids',
        ),
    ]