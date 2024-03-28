from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def base(request):
    event_types = [
        ('birthday', 'Birthday'),
        ('wedding', 'Wedding'),
        ('concert', 'Concert'),
        ('others', 'Others'),
    ]
    event_type = 'birthday'

    if request.method == 'POST':
        event_type = request.POST.get('event_type', 'birthday')
        full_name = request.POST.get('full_name')
        event_venue = request.POST.get('event_venue')
        mobile_number = request.POST.get('mobile_number')
        members_required = request.POST.get('members_required')
        seating_arrangement = request.POST.get('seating_arrangement')
        event_signpage_preference = request.POST.get('event_signpage_preference')
        event_duration = request.POST.get('event_duration')
        estimated_guests = request.POST.get('estimated_guests')
        event_date = request.POST.get('event_date')

        data_save = EventRegister(
            event_type=event_type,
            full_name=full_name,
            event_venue=event_venue,
            mobile_number=mobile_number,
            members_required=members_required,
            seating_arrangement=seating_arrangement,
            event_signpage_preference=event_signpage_preference,
            event_duration=event_duration,
            estimated_guests=estimated_guests,
            event_date=event_date
        )
        data_save.save()
        return render(request,'payment.html')

    return render(request, 'base.html', {"event_types": event_types, "event_type": event_type})