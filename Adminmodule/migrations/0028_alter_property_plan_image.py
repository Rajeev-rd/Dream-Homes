# Generated by Django 5.0.2 on 2024-04-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminmodule', '0027_remove_renovation_category_alter_balance_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='plan_image',
            field=models.ImageField(blank=True, null=True, upload_to='plan_images/'),
        ),
    ]