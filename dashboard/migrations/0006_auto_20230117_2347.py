# Generated by Django 3.1.13 on 2023-01-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20230117_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='file',
            field=models.FileField(upload_to='marksheets'),
        ),
    ]
