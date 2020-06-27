# Generated by Django 2.2.10 on 2020-06-24 00:03

import application.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_application_physical_location_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='extra_links',
            field=models.TextField(blank=True, max_length=300, verbose_name="Is there anything else you'd like us to look at while considering your application?"),
        ),
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, help_text='Companies will use this resume to offer interviews for internships and full-time positions.', null=True, upload_to=application.models.uuid_generator, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Upload your resume (PDF only)'),
        ),
        migrations.AlterField(
            model_name='application',
            name='shirt_size',
            field=models.CharField(choices=[('XXS', 'Unisex XXS'), ('XS', 'Unisex XS'), ('S', 'Unisex S'), ('M', 'Unisex M'), ('L', 'Unisex L'), ('XL', 'Unisex XL'), ('XXL', 'Unisex XXL')], max_length=4, verbose_name='What size shirt do you wear?'),
        ),
        migrations.AlterField(
            model_name='application',
            name='volunteer',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Would you be interested in mentoring for part of the event?'),
        ),
    ]
