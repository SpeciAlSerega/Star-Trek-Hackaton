# Generated by Django 3.1.2 on 2020-11-01 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pet', '0004_remove_petmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='petmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='user_photo'),
        ),
    ]
