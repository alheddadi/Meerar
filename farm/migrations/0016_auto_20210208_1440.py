# Generated by Django 3.1.5 on 2021-02-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0015_auto_20210208_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
