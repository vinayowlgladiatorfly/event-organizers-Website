# Generated by Django 4.2.5 on 2024-01-01 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0007_billinginformation_paymentinformation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregister',
            name='billing_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventify.billinginformation'),
        ),
    ]
