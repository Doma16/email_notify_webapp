from apscheduler.schedulers.background import BackgroundScheduler
from send_mail.utils import check_mail, DELTA

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_mail,'interval', seconds=(DELTA-1)*2)
    scheduler.start()