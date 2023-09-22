from apscheduler.schedulers.background import BackgroundScheduler
from send_mail.utils import check_mail, DELTA

from django_q.tasks import schedule

def start():

    minutes = int( (DELTA-1)*2/60 )
    print('Minutes: ',minutes)
    schedule('send_mail.utils.check_mail',
            schedule_type='I',
            minutes=minutes)
    '''
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_mail,'interval', seconds=(DELTA-1)*2)
    scheduler.start()
    '''