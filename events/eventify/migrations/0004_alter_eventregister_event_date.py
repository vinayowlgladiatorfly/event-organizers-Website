# Generated by Django 4.2.5 on 2023-12-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0003_alter_eventregister_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregister',
            name='event_date',
            field=models.DateField(),
        ),
    ]
