# Generated by Django 2.1 on 2019-07-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myworks', '0005_auto_20190712_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.FilePathField(path='img'),
        ),
    ]