# Generated by Django 3.2 on 2021-04-29 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypet', '0004_alter_pet_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
