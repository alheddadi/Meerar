# Generated by Django 3.1.5 on 2021-02-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0008_reports_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reports',
            name='price',
            field=models.IntegerField(),
        ),
    ]
