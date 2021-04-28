# Generated by Django 3.2 on 2021-04-29 10:50

from django.db import migrations, models
import mypet.models


class Migration(migrations.Migration):

    dependencies = [
        ('mypet', '0003_alter_pet_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[mypet.models.validate_image]),
        ),
    ]
