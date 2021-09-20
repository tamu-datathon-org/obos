# Generated by Django 2.2.10 on 2021-08-03 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_application_attending_with'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='attending_with',
            field=models.TextField(blank=True, help_text='Keep in mind they will also need to apply and fill out this form.', max_length=1000, verbose_name="If you're planning on attending with other people, please list their full names here."),
        ),
    ]