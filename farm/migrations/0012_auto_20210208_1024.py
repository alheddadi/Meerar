# Generated by Django 3.1.5 on 2021-02-08 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0011_auto_20210206_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='gobolka',
            new_name='number',
        ),
    ]
