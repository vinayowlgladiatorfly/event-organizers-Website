# Generated by Django 4.2.5 on 2024-01-04 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0008_alter_eventregister_billing_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregister',
            name='payment_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_registrations', to='eventify.paymentinformation'),
        ),
    ]
