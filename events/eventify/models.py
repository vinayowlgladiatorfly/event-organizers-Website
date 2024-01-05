from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class BillingInformation(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, choices=[
        ('Rajasthan', 'Rajasthan'),
        ('Maharashtra', 'Maharashtra'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Delhi', 'Delhi'),
    ])
    zipcode = models.IntegerField()

    def __str__(self):
        return self.full_name



class PaymentInformation(models.Model):
    card_number = models.CharField(max_length=16)
    exp_month = models.CharField(max_length=2)
    exp_year = models.CharField(max_length=4)
    cvv = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Card ending in {self.card_number[-4:]}'
    

class EventRegister(models.Model):
    EVENT_TYPES=[
        ('birthday', 'Birthday'),
        ('wedding', 'Wedding'),
        ('concert', 'Concert'),
        ('others', 'Others'),
    ]
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES, default = 'birthday')
    full_name = models.CharField(max_length=255)
    event_venue = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    members_required = models.IntegerField()
    seating_arrangement = models.CharField(max_length=255)
    event_signpage_preference = models.CharField(max_length=255)
    event_duration = models.IntegerField()
    estimated_guests = models.IntegerField(default=0)
    event_date = models.DateField()

    def __str__(self):
        return f'{self.full_name} - {self.event_type} Event'
