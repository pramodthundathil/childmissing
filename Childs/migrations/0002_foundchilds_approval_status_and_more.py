# Generated by Django 5.0.1 on 2024-02-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Childs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foundchilds',
            name='approval_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='missingchilds',
            name='approval_status',
            field=models.BooleanField(default=False),
        ),
    ]
