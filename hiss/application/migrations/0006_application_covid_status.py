# Generated by Django 2.2.10 on 2021-08-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20210801_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='covid_status',
            field=models.CharField(choices=[('fully_vaccinated', 'Fully vaccinated for COVID-19'), ('not_vaccinated', 'Not vaccinated for COVID-19')], default='prefers_in_person', max_length=24, verbose_name='What is your COVID-19 vaccination status?'),
        ),
    ]
