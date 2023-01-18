# Generated by Django 3.1.13 on 2023-01-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_bulletin_delete_order_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('CS', 'CS'), ('IT', 'IT'), ('EXTC', 'EXTC'), ('Mech', 'Mech'), ('Civil', 'Civil')], max_length=5, null=True)),
                ('sem', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI')], max_length=5, null=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]