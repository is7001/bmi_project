# Generated by Django 2.2 on 2019-04-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmi',
            name='bmi_score',
            field=models.FloatField(blank=True),
        ),
    ]
