# Generated by Django 2.2.1 on 2019-11-03 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_roomno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='available',
        ),
    ]
