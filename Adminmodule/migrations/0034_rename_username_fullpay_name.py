# Generated by Django 5.0.2 on 2024-04-02 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminmodule', '0033_advancepay_fullpay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fullpay',
            old_name='username',
            new_name='name',
        ),
    ]