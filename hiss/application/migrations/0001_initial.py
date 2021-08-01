# Generated by Django 2.2.10 on 2020-06-30 16:39

import application.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_s3_storage.storage
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Wave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('num_days_to_rsvp', models.IntegerField()),
                ('is_walk_in_wave', models.BooleanField(default=False, verbose_name='Is this wave for walk-ins?')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('datetime_submitted', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('P', 'Under Review'), ('R', 'Waitlisted'), ('A', 'Admitted'), ('C', 'Confirmed'), ('X', 'Declined'), ('I', 'Checked in'), ('E', 'Expired')], default='P', max_length=1)),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('extra_links', models.TextField(blank=True, max_length=500, verbose_name="Is there anything else you'd like us to look at while considering your application?")),
                ('prize_suggestions', models.TextField(blank=True, max_length=500, verbose_name='What prize(s) do you want to see at TD?')),
                ('workshop_suggestions', models.TextField(blank=True, max_length=500, verbose_name='What workshop(s) do you want to see at TD?')),
                ('ds_ml_classes', models.TextField(blank=True, max_length=500, verbose_name='What data science or machine learning related classes have you taken, if any?')),
                ('ds_ml_clubs', models.TextField(blank=True, max_length=500, verbose_name='What data science or machine learning related clubs on campus are you involved in, if any?')),
                ('ds_ml_jobs', models.TextField(blank=True, max_length=500, verbose_name='What data science or machine learning related jobs/internships have you had, if any?')),
                ('interesting_industries', models.TextField(blank=True, max_length=500)),
                ('industries_other', models.CharField(blank=True, max_length=255, null=True, verbose_name='other-industries')),
                ('resume', models.FileField(blank=True, help_text='Companies will use this resume to offer interviews for internships and full-time positions.', null=True, storage=django_s3_storage.storage.S3Storage(), upload_to=application.models.uuid_generator, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Upload your resume (PDF only)')),
                ('github_link', models.URLField(blank=True, max_length=255, null=True, verbose_name='Your GitHub')),
                ('linkedin_link', models.URLField(blank=True, max_length=255, null=True, verbose_name='Your Linkedin')),
                ('personal_website_link', models.URLField(blank=True, max_length=255, null=True, verbose_name='Your Personal Website')),
                ('instagram_link', models.URLField(blank=True, max_length=255, null=True, verbose_name='Your Instagram')),
                ('devpost_link', models.URLField(blank=True, max_length=255, null=True, verbose_name='Your Devpost')),
                ('school_other', models.CharField(blank=True, max_length=255, null=True)),
                ('majors', models.TextField(default=None, max_length=500)),
                ('minors', models.TextField(default=None, max_length=500)),
                ('classification', models.CharField(choices=[('Fr', 'Freshman'), ('So', 'Sophomore'), ('Jr', 'Junior'), ('Sr', 'Senior'), ('Ma', "Master's Student"), ('PhD', 'PhD Student'), ('O', 'Other')], max_length=3, verbose_name='What classification are you?')),
                ('gender', models.CharField(choices=[('', '---------'), ('NA', 'Prefer not to answer'), ('M', 'Male'), ('F', 'Female'), ('NB', 'Non-binary'), ('X', 'Prefer to self-describe')], default='NA', max_length=2, verbose_name="What's your gender?")),
                ('gender_other', models.CharField(blank=True, max_length=255, null=True, verbose_name='Self-describe')),
                ('age', models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(100)], verbose_name="What's your age?")),
                ('race', multiselectfield.db.fields.MultiSelectField(choices=[('AI', 'American Indian or Alaskan Native'), ('AS', 'Asian'), ('BL', 'Black or African-American'), ('HI', 'Hispanic or Latino'), ('NH', 'Native Hawaiian or other Pacific Islander'), ('WH', 'White'), ('NA', 'Prefer not to answer'), ('O', 'Prefer to self-describe')], max_length=41, verbose_name='What race(s) do you identify with?')),
                ('race_other', models.CharField(blank=True, max_length=255, null=True, verbose_name='Self-describe')),
                ('referral', models.CharField(choices=[('email', 'University Email'), ('social', 'Facebook / Instagram'), ('friend', 'Friend'), ('MLH', 'MLH Website / Newsletter'), ('MSC', 'MSC Open House'), ('campus', 'Campus Marketing (ex. Flyers, Posters, Whiteboards, etc)'), ('website', 'TAMU Datathon Website'), ('other', 'Other')], max_length=10, verbose_name='How did you hear about TAMU Datathon?')),
                ('volunteer', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Would you be interested in mentoring for part of the event?')),
                ('first_generation', models.BooleanField(default=False, verbose_name='I am a first generation college student.')),
                ('datascience_experience', models.CharField(default=None, max_length=2)),
                ('technology_experience', models.CharField(default=None, max_length=150)),
                ('grad_year', models.IntegerField(choices=[(2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], verbose_name='What is your anticipated graduation year?')),
                ('num_hackathons_attended', models.CharField(choices=[('0', 'This will be my first!'), ('1-3', '1-3'), ('4-7', '4-7'), ('8-10', '8-10'), ('10+', '10+')], max_length=22, verbose_name='How many hackathons have you attended?')),
                ('agree_to_mlh_policies', models.BooleanField(choices=[(True, 'Agree')], default=None, help_text='Being an MLH event, we need participants to be familiar with the MLH Code of Conduct and the MLH Contest Terms and Conditions.')),
                ('is_adult', models.BooleanField(choices=[(True, 'Agree')], default=None, help_text='Please note that freshmen under 18 must be accompanied by an adult or prove that they go to Texas A&M.', verbose_name='Please confirm you are 18 or older.')),
                ('physical_location', models.CharField(max_length=20, verbose_name='Where will you be participating from?')),
                ('physical_location_other', models.CharField(blank=True, max_length=20, null=True, verbose_name='other-physical-location')),
                ('confirmation_deadline', models.DateTimeField(blank=True, null=True)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.School', verbose_name='What school do you go to?')),
            ],
        ),
    ]
