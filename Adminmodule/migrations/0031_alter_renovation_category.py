# Generated by Django 5.0.2 on 2024-04-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminmodule', '0030_renovation_category_alter_balance_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renovation',
            name='category',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]