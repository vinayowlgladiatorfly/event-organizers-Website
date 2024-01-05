from django import forms
from .models import *

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegister
        fields = '__all__'
class BillingInformationForm(forms.ModelForm):
    class Meta:
        model = BillingInformation
        fields = '__all__'

class PaymentInformationForm(forms.ModelForm):
    class Meta:
        model = PaymentInformation
        fields = '__all__'  

