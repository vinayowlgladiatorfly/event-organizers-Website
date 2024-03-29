# Generated by Django 4.2.5 on 2024-01-04 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0010_remove_eventregister_billing_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregister',
            name='billing_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventify.billinginformation'),
        ),
        migrations.AddField(
            model_name='eventregister',
            name='payment_info',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='eventify.paymentinformation'),
        ),
    ]
