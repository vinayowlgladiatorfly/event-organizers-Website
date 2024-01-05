# Generated by Django 4.2.5 on 2023-12-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregister',
            name='estimated_guests',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eventregister',
            name='event_date',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='eventregister',
            name='event_duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eventregister',
            name='event_signpage_preference',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='eventregister',
            name='event_venue',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='eventregister',
            name='full_name',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='eventregister',
            name='members_required',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='eventregister',
            name='mobile_number',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='eventregister',
            name='seating_arrangement',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
