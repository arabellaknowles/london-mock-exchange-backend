# Generated by Django 3.1.4 on 2020-12-11 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20201210_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='balance',
        ),
    ]
