import schedule
import time
import threading
import os
import sys
from constance import config
import logging
from threading import Thread


BASE_DIR = os.path.abspath('.')
logging.basicConfig(level=logging.INFO,
                    format='{asctime} {filename}[line:{lineno}] {levelname} {message}',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    style='{',
                    handlers=[logging.StreamHandler(), logging.FileHandler(BASE_DIR + "/logs/logs.log")]
                    )
log = logging.getLogger(__name__)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dalmorex.settings')
    import django
    django.setup()
    from dlm.managers import PollDeployStatus





def update_ldap_job():
    print("Start updating ldap info...")
    os.system('python3 manage.py syncldap')
    print("Update finished")


def send_git_email():
    print("Start sending git email...")
    os.system('python3 manage.py commitReport')
    print("Send finished")


def send_email_notification_for_unfinished_task():
    print("Start sending task email...")
    os.system('python3 manage.py pullOverDueTasks')
    print("Send finished")

def send_no_sign_off_manpower_email():
    print("Start sending no sign off manpower email...")
    os.system('python3 manage.py signoffManpower')
    print("Send finished")

def sign_off_project():
    print("Start sign off manpower...")
    os.system('python3 manage.py signoffProject')
    print("Sign off finished")


def send_process_task_remind():
    print("Start sending task remind...")
    os.system('python3 manage.py taskRemindAction')
    print("Send finished")


def update_deploy_status_job():
    log.info('start update deploy status')
    while True:
        PollDeployStatus.poll_status()
        time.sleep(5)


def auto_run():
    os.system('python3 manage.py pollRunAction')


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every().day.at("01:00").do(run_threaded, pull_cmdb_info_job)
schedule.every().day.at("02:00").do(run_threaded, update_ldap_job)
schedule.every().day.at("03:00").do(run_threaded, pull_pds_data_job)
schedule.every().day.at("04:00").do(run_threaded, update_org_user_data_wx_job)
schedule.every().day.at("06:00").do(run_threaded, send_git_email)
# schedule.every().day.at("10:00").do(run_threaded, send_email_notification_for_unfinished_task)
schedule.every().day.at("22:00").do(run_threaded, sign_off_project)
schedule.every().day.at("10:00").do(run_threaded, send_no_sign_off_manpower_email)
schedule.every().day.at("10:30").do(run_threaded, send_process_task_remind)
schedule.every(15).minutes.do(run_threaded, update_deploy_request_job)
schedule.every(15).minutes.do(run_threaded, auto_run)

# start thread to update deploy status
update_deploy_thread = threading.Thread(target=update_deploy_status_job)
update_deploy_thread.start()


while True:
    try:
        sys.stdout.flush()
        schedule.run_pending()
        time.sleep(5)
        if not update_deploy_thread.is_alive():
            log.info('deploy thread except terminate, now start a new thread')
            update_deploy_thread = threading.Thread(target=update_deploy_status_job)
            update_deploy_thread.start()
    except Exception as e:
        log.warning(e)

