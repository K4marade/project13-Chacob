# Generated by Django 3.2 on 2021-04-20 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendar', '0004_event_mail_alert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='mail_alert',
            field=models.BooleanField(),
        ),
    ]
