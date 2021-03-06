# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-12 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accommodation_type', models.CharField(choices=[(b'C', b'Camping/RV'), (b'R', b'Rental Property'), (b'H', b'Hotel/Motel/BnB')], default=b'H', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.BooleanField(default=False)),
                ('family', models.BooleanField(default=False)),
                ('food', models.BooleanField(default=False)),
                ('shopping', models.BooleanField(default=False)),
                ('leisure', models.BooleanField(default=False)),
                ('nightlife', models.BooleanField(default=False)),
                ('park', models.BooleanField(default=False)),
                ('sports', models.BooleanField(default=False)),
                ('tourist', models.BooleanField(default=False)),
                ('hiking', models.BooleanField(default=False)),
                ('swimming', models.BooleanField(default=False)),
                ('beach', models.BooleanField(default=False)),
                ('outdoors', models.BooleanField(default=False)),
                ('adventure_sports', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name=b'startdate')),
                ('num_days', models.IntegerField()),
                ('price', models.FloatField(default=0)),
                ('paid', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(max_length=1024)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'uploads/')),
                ('url', models.URLField(blank=True, null=True)),
                ('accommodation_type', models.CharField(choices=[(b'C', b'Camping/RV'), (b'R', b'Rental Property'), (b'H', b'Hotel/Motel/BnB'), (b'N', b'None')], default=b'H', max_length=1)),
                ('activities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='CampingOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rv', models.BooleanField(default=False)),
                ('tent', models.BooleanField(default=False)),
                ('tent_drivein', models.BooleanField(default=False)),
                ('hotshower', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('handicap', models.BooleanField(default=False)),
                ('swimming', models.BooleanField(default=False)),
                ('cabin', models.BooleanField(default=False)),
                ('water', models.BooleanField(default=False)),
                ('group', models.BooleanField(default=False)),
                ('boat', models.BooleanField(default=False)),
                ('campfire', models.BooleanField(default=False)),
                ('horse', models.BooleanField(default=False)),
                ('pet', models.BooleanField(default=False)),
                ('others', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name=b'date from')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name=b'date to')),
                ('number_of_days', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('accommodation_type', models.CharField(choices=[(b'C', b'Camping/RV'), (b'R', b'Rental Property'), (b'H', b'Hotel/Motel/BnB')], default=b'H', max_length=1)),
                ('activities', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.Activity')),
                ('camping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.CampingOption')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegan', models.BooleanField(default=False)),
                ('vegetarian', models.BooleanField(default=False)),
                ('kosher', models.BooleanField(default=False)),
                ('halah', models.BooleanField(default=False)),
                ('organic', models.BooleanField(default=False)),
                ('fastfood', models.BooleanField(default=False)),
                ('meat', models.BooleanField(default=False)),
                ('seafood', models.BooleanField(default=False)),
                ('desserts', models.BooleanField(default=False)),
                ('glutenfree', models.BooleanField(default=False)),
                ('three_star_restaurant', models.BooleanField(default=False)),
                ('zagat', models.BooleanField(default=False)),
                ('family', models.BooleanField(default=False)),
                ('grocery', models.BooleanField(default=False)),
                ('cafe', models.BooleanField(default=False)),
                ('brewery', models.BooleanField(default=False)),
                ('raw', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HotelOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freewifi', models.BooleanField(default=False)),
                ('privatebath', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('restaurant', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('pool', models.BooleanField(default=False)),
                ('freebreakfast', models.BooleanField(default=False)),
                ('handicap', models.BooleanField(default=False)),
                ('others', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('lat_coord', models.FloatField(blank=True)),
                ('long_coord', models.FloatField(blank=True)),
                ('proximity', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('accommodation_type', models.CharField(choices=[(b'C', b'Camping/RV'), (b'R', b'Rental Property'), (b'H', b'Hotel/Motel/BnB')], default=b'H', max_length=1)),
                ('activities', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.Activity')),
                ('camping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.CampingOption')),
                ('food', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.Food')),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.HotelOption')),
                ('locations', models.ManyToManyField(blank=True, to='gotogether.Location')),
            ],
        ),
        migrations.CreateModel(
            name='RentalOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freewifi', models.BooleanField(default=False)),
                ('privatebath', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('restaurant', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('pool', models.BooleanField(default=False)),
                ('yard', models.BooleanField(default=False)),
                ('handicap', models.BooleanField(default=False)),
                ('others', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizer', models.BooleanField(default=False)),
                ('reply', models.CharField(choices=[(b'Y', b'Yes'), (b'N', b'No'), (b'U', b'Undecided')], default=b'U', max_length=1)),
                ('invited', models.DateTimeField(auto_now_add=True, verbose_name=b'invited on')),
                ('replied', models.DateTimeField(verbose_name=b'replied on')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotogether.Event')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=b'uploads/')),
                ('contacts', models.ManyToManyField(blank=True, to='gotogether.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserEventProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotogether.Event')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotogether.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotogether.User')),
            ],
        ),
        migrations.AddField(
            model_name='rsvp',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotogether.User'),
        ),
        migrations.AddField(
            model_name='profile',
            name='rental',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.RentalOption'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotogether.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='gotogether.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='food',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.Food'),
        ),
        migrations.AddField(
            model_name='event',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.HotelOption'),
        ),
        migrations.AddField(
            model_name='event',
            name='locations',
            field=models.ManyToManyField(blank=True, to='gotogether.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='particpants',
            field=models.ManyToManyField(blank=True, related_name='participants', through='gotogether.RSVP', to='gotogether.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='rental',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.RentalOption'),
        ),
        migrations.AddField(
            model_name='business',
            name='camping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.CampingOption'),
        ),
        migrations.AddField(
            model_name='business',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.Food'),
        ),
        migrations.AddField(
            model_name='business',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.HotelOption'),
        ),
        migrations.AddField(
            model_name='business',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotogether.Location'),
        ),
        migrations.AddField(
            model_name='business',
            name='rental',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gotogether.RentalOption'),
        ),
        migrations.AddField(
            model_name='booking',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotogether.Event'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotogether.User'),
        ),
        migrations.AddField(
            model_name='booking',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotogether.Business'),
        ),
    ]
