# Generated by Django 4.2.5 on 2024-01-04 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0009_alter_eventregister_payment_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventregister',
            name='billing_info',
        ),
        migrations.RemoveField(
            model_name='eventregister',
            name='payment_info',
        ),
    ]
