from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(BillingInformation)
admin.site.register(PaymentInformation)
admin.site.register(EventRegister)