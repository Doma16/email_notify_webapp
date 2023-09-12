from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Tap(models.Model):

    added_on = models.DateTimeField(default=timezone.now, blank=True) 

    title = models.CharField(max_length=256, default='')
    message = models.TextField(default='')
    send_date = models.DateTimeField("send on date...", blank=True, null=True)
    
    email_to = models.EmailField(default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title}'

class Day(models.Model):

    _days = [
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday'),
    ]

    day = models.CharField(max_length=1, choices=_days)
    time = models.TimeField(editable=True, blank=True, null=True)
    tap = models.ForeignKey(Tap, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{int(self.day)+1}th day of week, at {self.time}'
