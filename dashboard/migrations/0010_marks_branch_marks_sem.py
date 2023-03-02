# Generated by Django 4.0.5 on 2023-03-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_remove_marks_branch_remove_marks_sem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='branch',
            field=models.CharField(choices=[('CS', 'CS'), ('IT', 'IT'), ('EXTC', 'EXTC'), ('Mech', 'Mech'), ('Civil', 'Civil')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='marks',
            name='sem',
            field=models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI')], max_length=5, null=True),
        ),
    ]