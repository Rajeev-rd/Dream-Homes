# Generated by Django 5.0.2 on 2024-03-15 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminmodule', '0007_alter_status_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.TextField(null=True)),
                ('location', models.TextField(null=True)),
            ],
        ),
    ]