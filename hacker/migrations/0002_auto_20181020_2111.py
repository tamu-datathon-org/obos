# Generated by Django 2.1.2 on 2018-10-20 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hacker',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='hacker',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='hacker',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]
