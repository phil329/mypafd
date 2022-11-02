import schedule
import time
import random
from main import main

def job():
    time.sleep(random.randint(0,1000))
    try:
        main()
        content = 'check in successfully !'
        email = Email()
        email.sendemail(False,content)
    except:
        # 中间有任何一个环节出现问题都要发邮件通知我
        content = 'There are some mistakes happened ！'
        email = Email()
        email.sendemail(False,content)

#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)

#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

if __name__ == '__main__':
    schedule.every().day.at("10:30").do(job)
    # schedule.every(10).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(60)
