# Generated by Django 3.2.5 on 2021-07-26 18:54

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mypet', '0003_alter_pet_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
