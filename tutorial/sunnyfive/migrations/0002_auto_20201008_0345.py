# Generated by Django 3.1.2 on 2020-10-08 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunnyfive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sunnyfive',
            name='title',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
