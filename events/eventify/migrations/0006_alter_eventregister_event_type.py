# Generated by Django 4.2.5 on 2023-12-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0005_eventregister_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregister',
            name='event_type',
            field=models.CharField(choices=[('birthday', 'Birthday'), ('wedding', 'Wedding'), ('concert', 'Concert'), ('others', 'Others')], default='birthday', max_length=10),
        ),
    ]
