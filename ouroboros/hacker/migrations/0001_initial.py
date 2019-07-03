# Generated by Django 2.2.2 on 2019-07-03 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hacker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into the admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('rsvp_deadline', models.DateTimeField(null=True)),
                ('cant_make_it', models.BooleanField(default=False)),
                ('checked_in', models.NullBooleanField()),
                ('checked_in_datetime', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, help_text="Please let us know if there's anything else we can do to make Howdy Hack an amazing experience for you!", max_length=300, verbose_name='Anything else you want us to know?')),
                ('date_rsvped', models.DateField(auto_now_add=True)),
                ('hacker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('adult', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, help_text='NOTE: We are able to admit minors only if they are accompanied by a college student (18+) who is planning on participating in the hackathon', verbose_name='Are you at least 18 or older?')),
                ('major', models.CharField(choices=[('Accounting', 'Accounting'), ('Actuarial Science', 'Actuarial Science'), ('Advertising', 'Advertising'), ('Agriculture', 'Agriculture'), ('Agricultural and Biological Engineering', 'Agricultural and Biological Engineering'), ('Agricultural Business Management', 'Agricultural Business Management'), ('Agriculture Economics', 'Agriculture Economics'), ('Animal Bioscience', 'Animal Bioscience'), ('Animal Sciences', 'Animal Sciences'), ('Anthropology', 'Anthropology'), ('Applied Mathematics', 'Applied Mathematics'), ('Archaeology', 'Archaeology'), ('Architectural Engineering', 'Architectural Engineering'), ('Architecture', 'Architecture'), ('Art History', 'Art History'), ('Studio Art', 'Studio Art'), ('Art Education', 'Art Education'), ('Biobehavioral Health', 'Biobehavioral Health'), ('Biochemistry', 'Biochemistry'), ('Bioengineering', 'Bioengineering'), ('Biology', 'Biology'), ('Biophysics', 'Biophysics'), ('Biotechnology', 'Biotechnology'), ('Business Administration and Management', 'Business Administration and Management'), ('Business Logistics', 'Business Logistics'), ('Chemical Engineering', 'Chemical Engineering'), ('Chemistry', 'Chemistry'), ('Children', 'Children'), ('Civil Engineering', 'Civil Engineering'), ('Computer Engineering', 'Computer Engineering'), ('Computer Science', 'Computer Science'), ('Crime, Law, and Justice', 'Crime, Law, and Justice'), ('Dance', 'Dance'), ('Earth Sciences', 'Earth Sciences'), ('Economics', 'Economics'), ('Electrical Engineering', 'Electrical Engineering'), ('Elementary and Kindergarten Education', 'Elementary and Kindergarten Education'), ('Engineering Science', 'Engineering Science'), ('English', 'English'), ('Environmental Systems Engineering', 'Environmental Systems Engineering'), ('Environmental Sciences', 'Environmental Sciences'), ('Environmental Resource Management', 'Environmental Resource Management'), ('Film and Video', 'Film and Video'), ('Finance', 'Finance'), ('Food Science', 'Food Science'), ('Forest Science', 'Forest Science'), ('Forest Technology', 'Forest Technology'), ('General Science', 'General Science'), ('Geography', 'Geography'), ('Geosciences', 'Geosciences'), ('Graphic Design and Photography', 'Graphic Design and Photography'), ('Health and Physical Education', 'Health and Physical Education'), ('Health Policy and Administration', 'Health Policy and Administration'), ('History', 'History'), ('Horticulture', 'Horticulture'), ('Hotel, Restaurant, and Institutional Management', 'Hotel, Restaurant, and Institutional Management'), ('Human Development and Family Studies', 'Human Development and Family Studies'), ('Individual and Family Studies', 'Individual and Family Studies'), ('Industrial Engineering', 'Industrial Engineering'), ('Information Sciences and Technology', 'Information Sciences and Technology'), ('Journalism', 'Journalism'), ('Kinesiology', 'Kinesiology'), ('Landscape Architecture', 'Landscape Architecture'), ('Law Enforcement and Correction', 'Law Enforcement and Correction'), ('Marine Biology', 'Marine Biology'), ('Marketing', 'Marketing'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Media Studies', 'Media Studies'), ('Meteorology', 'Meteorology'), ('Microbiology', 'Microbiology'), ('Mineral Economics', 'Mineral Economics'), ('Modern Languages', 'Modern Languages'), ('Music Education', 'Music Education'), ('Nuclear Engineering', 'Nuclear Engineering'), ('Nursing', 'Nursing'), ('Nutrition', 'Nutrition'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Physiology', 'Physiology'), ('Political Science', 'Political Science'), ('Pre-medicine', 'Pre-medicine'), ('Psychology', 'Psychology'), ('Public Relations', 'Public Relations'), ('Real Estate', 'Real Estate'), ('Recreation and Parks', 'Recreation and Parks'), ('Rehabilitation Services', 'Rehabilitation Services'), ('Religious Studies', 'Religious Studies'), ('Secondary Education', 'Secondary Education'), ('Sociology', 'Sociology'), ('Social Work', 'Social Work'), ('Special Education', 'Special Education'), ('Speech Communication', 'Speech Communication'), ('Speech Pathology and Audiology/Communication Disorder', 'Speech Pathology and Audiology/Communication Disorder'), ('Statistics', 'Statistics'), ('Telecommunications', 'Telecommunications'), ('Theater', 'Theater'), ('Wildlife and Fishery Science', 'Wildlife and Fishery Science'), ('Wildlife Technology', 'Wildlife Technology'), ("Women's Studies", "Women's Studies")], max_length=50, verbose_name="What's your major?")),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non-binary'), ('NA', 'Prefer not to disclose')], max_length=2, verbose_name="What's your gender?")),
                ('race', multiselectfield.db.fields.MultiSelectField(choices=[('American Indian', 'American Indian or Alaskan Native'), ('Asian', 'Asian'), ('Black', 'Black or African-American'), ('Hispanic', 'Hispanic or Latino White'), ('Native Hawaiian', 'Native Hawaiian or other Pacific Islander'), ('White', 'White or Caucasian'), ('NA', 'Decline to self-identify')], max_length=41, verbose_name='What race(s) do you identify with?')),
                ('classification', models.CharField(choices=[('Fr', 'Freshman'), ('So', 'Sophomore'), ('Jr', 'Junior'), ('Sr', 'Senior'), ('Ot', 'Other')], max_length=2, verbose_name='What classification are you?')),
                ('grad_year', models.CharField(choices=[('Fall 2019', 'Fall 2019'), ('Spring 2020', 'Spring 2020'), ('Fall 2020', 'Fall 2020'), ('Spring 2021', 'Spring 2021'), ('Fall 2021', 'Fall 2021'), ('Spring 2022', 'Spring 2022'), ('Fall 2022', 'Fall 2022'), ('Spring 2023', 'Spring 2023'), ('Other', 'Other')], max_length=11, verbose_name='What is your anticipated graduation date?')),
                ('dietary_restrictions', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Halal', 'Halal'), ('Kosher', 'Kosher'), ('Food Allergies', 'Food Allergies')], max_length=44, verbose_name='Do you have any dietary restrictions that we should know about?')),
                ('num_hackathons_attended', models.CharField(choices=[('0', 'This will be my first!'), ('1-3', '1-3'), ('4-7', '4-7'), ('8-10', '8-10'), ('10+', '10+')], max_length=22, verbose_name='How many hackathons have you attended?')),
                ('previous_attendant', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Have you attended Howdy Hack before?')),
                ('tamu_student', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Are you a Texas A&M student?')),
                ('shirt_size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3, verbose_name='Shirt size?')),
                ('extra_links', models.CharField(help_text='Links to LinkedIn, GitHub, Devpost, Personal Website, etc.', max_length=200, verbose_name="Point us to anything you'd like us to look at while considering your application")),
                ('programming_joke', models.TextField(max_length=500, verbose_name='Tell us your best programming joke')),
                ('unlimited_resource', models.TextField(max_length=500, verbose_name="What is the one thing you'd build if you had unlimited resources?")),
                ('cool_prize', models.TextField(max_length=500, verbose_name="What is a cool prize you'd like to win at Howdy Hack?")),
                ('notes', models.TextField(blank=True, help_text='Provide any additional notes and/or comments in the text box provided', max_length=300)),
                ('resume', models.FileField(upload_to='', verbose_name='Provide us a copy of your most recent resume so we can get you connected with companies.')),
                ('approved', models.NullBooleanField()),
                ('hacker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hacker.Wave')),
            ],
        ),
    ]
