# Generated by Django 3.2.10 on 2022-01-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0004_sport_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
