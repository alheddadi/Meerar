# Generated by Django 3.0.5 on 2020-06-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0002_auto_20200624_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricess',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]