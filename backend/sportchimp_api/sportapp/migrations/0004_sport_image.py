# Generated by Django 3.2.10 on 2022-01-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0003_activity_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
