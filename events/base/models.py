from django.db import models

# Create your models here.
class EventRegister(models.Model):
    EVENT_TYPES=[
        ('birthday', 'Birthday'),
        ('wedding', 'Wedding'),
        ('concert', 'Concert'),
        ('others', 'Others'),
    ]
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES, default = 'birthday')
    full_name = models.CharField(max_length=255)
    event_venue = models.CharField(max_length=255,null=True)
    mobile_number = models.CharField(max_length=15,null=True)
    members_required = models.IntegerField(null=True)
    seating_arrangement = models.CharField(max_length=255,null=True)
    event_signpage_preference = models.CharField(max_length=255,null=True)
    event_duration = models.IntegerField(null=True)
    estimated_guests = models.IntegerField(default=0,null=True)
    event_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} - {self.event_type} Event'