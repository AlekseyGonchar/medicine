# Generated by Django 3.0.7 on 2020-06-23 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosevariant',
            name='course_interval',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='dosevariant',
            name='dose_interval',
            field=models.DurationField(),
        ),
    ]