# Generated by Django 5.0.2 on 2024-04-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminmodule', '0035_rename_advanceamound_advancepay_advanceamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancepay',
            name='AdvanceAmount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='fullpay',
            name='Amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
