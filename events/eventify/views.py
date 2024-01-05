from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login,logout
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        password2 = request.POST.get('password2','')
        #print(username,email,password,password2) 
        if password != password2:
            return HttpResponse("your password is not same!")
        else:       
            data = User.objects.create_user(username,email,password)
            data.save()
            return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        #print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
          dj_login(request,user)
          return redirect('index')
        else:
            return HttpResponse("your username and password is incorrect")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

'''
@login_required
def payment(request, billing_form=None, payment_form=None):
    if request.method == 'POST':
        billing_form = BillingInformationForm(request.POST) if billing_form is None else billing_form
        payment_form = PaymentInformationForm(request.POST) if payment_form is None else payment_form

        if billing_form.is_valid() and payment_form.is_valid():
            billing_info = billing_form.save()
            payment_info = payment_form.save()

            event_registration = EventRegister(user=request.user)
            event_registration.save()

            # Redirect to the desired page (change as needed)
            return redirect('/')
        else:
            # Display form errors using messages
            messages.error(request, 'Form submission error. Please correct the errors.')

    # If forms are not valid or the request method is not POST, render the payment form page with errors
    return render(request, 'payment.html', {'billing_form': billing_form, 'payment_form': payment_form})

@login_required
def base(request, event_type):
    billing_form = BillingInformationForm()
    payment_form = PaymentInformationForm()
    event_form = EventRegistrationForm()

    if request.method == 'POST':
        event_form = EventRegistrationForm(request.POST)

        if event_form.is_valid():
            billing_form = BillingInformationForm(request.POST)
            payment_form = PaymentInformationForm(request.POST)

            if billing_form.is_valid() and payment_form.is_valid():
                return payment(request, billing_form=billing_form, payment_form=payment_form)
            else:
                messages.error(request, 'Form submission error. Please correct the errors.')

    return render(request, 'base.html', {'event_form': event_form, 'event_type': event_type, 'billing_form': billing_form, 'payment_form': payment_form})
'''


def base(request,event_type):
    event_form = EventRegistrationForm()
    if request.method == 'POST':
        event_form = EventRegistrationForm(request.POST)

        if event_form.is_valid():
            event_form.save()
            return redirect('payment')  # Corrected the redirect function
    else:
        print(event_form.errors)
    return render(request, 'base.html', {'event_form': event_form,'event_type':event_type})


def payment(request):
    billing_form = BillingInformationForm()
    payment_form = PaymentInformationForm()
    if request.method == 'POST':
        billing_form = BillingInformationForm(request.POST)
        payment_form = PaymentInformationForm(request.POST)

        if billing_form.is_valid() and payment_form.is_valid():
            billing_form.save()
            payment_form.save()
            return render(request,'payment_success.html')
    else:
        BillingInformationForm()
        PaymentInformationForm()
    return render(request,'payment.html',{'billing_form':billing_form,'payment_form':payment_form})            