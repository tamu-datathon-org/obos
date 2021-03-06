# Generated by Django 2.2.10 on 2021-08-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20210801_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='covid_status',
            field=models.CharField(blank=True, choices=[('fully_vaccinated', 'Fully vaccinated for COVID-19'), ('not_vaccinated', 'Not vaccinated for COVID-19')], default='', max_length=24, verbose_name='What is your COVID-19 vaccination status?'),
        ),
    ]
