# Generated by Django 5.0.2 on 2024-03-23 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminmodule', '0023_notification_alter_message_reply_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='reply_to',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]