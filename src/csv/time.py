import pytz
from datetime import datetime, timedelta

time_yesterday = (datetime.now(pytz.timezone('Asia/Jakarta'))-timedelta(1)).strftime("%Y-%m-%d %H:%M:%S")
time_now = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%Y-%m-%d %H:%M:%S")
time_now_email_subject = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%Y-%m-%d")
time_now_filename = datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%Y%m%d")

'''
if time_now >= f'{time_now_email_subject} 23:39:01' and time_now <= f'{time_now_email_subject} 16:00:00':
    time_from = f'{time_now_email_subject} 00:00:01'
elif time_now >= f'{time_now_email_subject} 16:00:01' and time_now <= f'{time_now_email_subject} 00:00:00':
    time_from = f'{time_now_email_subject} 09:00:01'
    print(time_from)
elif time_now >= f'{time_now_email_subject} 00:00:01' and time_now <= f'{time_now_email_subject} 09:00:00':
    time_from = time_yesterday
else:
    print('error')
'''