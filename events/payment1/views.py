from .models import *
from django.shortcuts import render,redirect
from django.db import transaction
import logging
from django.http import HttpResponseServerError

logger = logging.getLogger(__name__)


def payment_form(request):
     if request.method == 'POST':
        try:
            with transaction.atomic():
                card_number = request.POST.get('card_number')
                cvc = request.POST.get('cvc')
                exp_month = request.POST.get('exp_month')
                exp_year = request.POST.get('exp_year')
                amount = request.POST.get('amount')
                full_name = request.POST.get('full_name')
                name_on_card = request.POST.get('name_on_card')
                email = request.POST.get('email')
                address = request.POST.get('address')
                city = request.POST.get('city')
                date_of_birth = request.POST.get('date_of_birth')
                gender = request.POST.get('gender')
                payment_method = request.POST.get('pay')

                payment = Payment(
                    card_number=card_number,
                    cvc=cvc,
                    exp_month=exp_month,
                    exp_year=exp_year,
                    amount=amount,
                    payment_method=payment_method,
                    full_name=full_name,
                    name_on_card=name_on_card,
                    email=email,
                    address=address,
                    city=city,
                    date_of_birth=date_of_birth,
                    gender=gender
                )
                payment.save()

                return redirect('payment_success')
        except Exception as e:
            logger.error(f"Error occurred while saving payment: {e}")
            return HttpResponseServerError("An error occurred while processing your payment. Please try again later.")


def payment_success(request):
    return render(request, 'payment_success.html')