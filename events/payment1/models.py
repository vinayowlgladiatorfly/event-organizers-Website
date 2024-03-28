# models.py

from django.db import models

class Payment(models.Model):
    card_number = models.CharField(max_length=16)
    cvc = models.CharField(max_length=3)
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, default="Paypal",choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')])
    full_name = models.CharField(max_length=100,null=True)
    name_on_card = models.CharField(max_length=100,default=full_name)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=100,null=True)
    date_of_birth = models.DateField(null=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='male')
