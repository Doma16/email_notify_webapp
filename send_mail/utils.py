from django.core.mail import send_mail
from tapa.models import Tap, Day

from tapatapa.settings import DEFAULT_FROM_EMAIL
from django.utils import timezone
import datetime
import pytz

def get_data(tap):
    return tap.title, tap.message, tap.email_to

DELTA = 16
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
    print(now)
    for tap in taps:
        
        title, message, to = get_data(tap)
        if to is None or to == '': continue
        
        date = tap.send_date
        if date:
            date = date.astimezone(tz=pytz.timezone('cet')).replace(tzinfo=None)
            diff = date - now.replace(tzinfo=None)

            if in_limits_timedelta(diff):
                sent_m = send_mail(
                    subject=title,
                    message=message,
                    from_email=DEFAULT_FROM_EMAIL,
                    recipient_list=[to],
                    fail_silently=True
                )
                print(f'{sent_m} : {to}')
                
        days = list(Day.objects.filter(tap=tap.pk))
        for day in days:
            
            if in_limits_daytime(now, day):
                sent_m = send_mail(
                    subject=title,
                    message=message,
                    from_email=DEFAULT_FROM_EMAIL,
                    recipient_list=[to],
                    fail_silently=True
                )
                print(f'{sent_m} : {to}')
