# Generated by Django 4.2.5 on 2024-03-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregister',
            name='event_venue',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
