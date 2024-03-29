# Generated by Django 5.0.2 on 2024-03-27 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminmodule', '0017_property_plan_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.TextField(max_length=100, null=True)),
                ('receiver', models.TextField(max_length=100, null=True)),
                ('msg', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
