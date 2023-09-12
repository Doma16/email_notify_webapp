from django.core.mail import send_mail
from tapa.models import Tap, Day

from tapatapa.settings import DEFAULT_FROM_EMAIL

import datetime

def get_data(tap):
    return tap.title, tap.message, tap.email_to

DELTA = 151
def in_limits_timedelta(diff):
    tot_sec = diff.days * 24 * 60 * 60 + diff.seconds
    if abs(tot_sec) <= DELTA:
        return True
    return False

def in_limits_daytime(now, day):
    if day is None:
        return False
    if day.day is None:
        return False
    if day.time is None:
        return False

    if now.date().weekday() != int(day.day):
        return False

    time = now.time()
    time_sec = time.hour * 60 * 60 + time.minute * 60 + time.second
    day_sec = day.time * 60 * 60 + day.time * 60 + day.time.second

    if abs(time_sec - day_sec) <= DELTA:
        return True
    return False
    
def check_mail():
    
    now = datetime.datetime.now()
    taps = list(Tap.objects.all())    

    for tap in taps:
        
        title, message, to = get_data(tap)
        if to is None or to == '': continue
        
        date = tap.send_date
        if date:
            date = date.replace(tzinfo=None)
            diff = date - now
            if in_limits_timedelta(diff):
                send_mail(
                    subject=title,
                    message=message,
                    from_email=DEFAULT_FROM_EMAIL,
                    recipient_list=[to],
                    fail_silently=True
                )
                
        days = list(Day.objects.filter(tap=tap.pk))
        for day in days:
            
            if in_limits_daytime(now, day):
                send_mail(
                    subject=title,
                    message=message,
                    from_email=DEFAULT_FROM_EMAIL,
                    recipient_list=[to],
                    fail_silently=True
                )