# Generated by Django 3.1.5 on 2021-02-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0010_reports_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]