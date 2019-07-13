# Generated by Django 2.1 on 2019-07-13 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myworks', '0007_remove_portfolio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.FilePathField(default='pathfile', path='/img'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='technology_used',
            field=models.CharField(max_length=15, verbose_name='tech'),
        ),
    ]
