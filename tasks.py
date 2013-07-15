# -*- coding: utf-8 -*-
import logging

import os
from celery import Celery
from celery import task
from celery.task import periodic_task
from datetime import timedelta
from os import environ

from django.core.mail import send_mail

from seats_check.models import Section
from seats_check import util

@periodic_task(run_every=timedelta(seconds=20))
def update_periodic():
    secs = Section.objects.all()
    count = len(secs)
    for i in range(0, count, 30):
        process_secs = secs[i:i+30]
        update_secs.delay(process_secs)

@task
def update_secs(secs):
    for sec in secs:
        max_num, curr_num, name, code, number = util.get_all(sec.crn, sec.term)
        rem_num = max_num - curr_num
        seats_change = rem_num - sec.remain_seats_num
        sec.max_seats_num = max_num
        sec.current_seats_num = curr_num
        sec.remain_seats_num = rem_num
        sec.save()
        msg = 'Your subscribed class %s, class code is %s, class number is %s, section number is %s, maximun seats %s, there are %s seats left' % (name, code, number, sec.crn, max_num, rem_num)
        if seats_change > 0:
            msg = 'Wow! your class %s has new seats released!!\n Remain seats change from %s to %s' % (
                      sec.crn, 
                      str(rem_num - seats_change),
                      str(rem_num)
                   )
            users = sec.myuser_set.all()
            emails = [user.user.email for user in users]
            send_email.delay(emails, msg)
        elif seats_change < 0:
            msg = 'Sorry!!! You class\n %s \nSeats are decreasing!!\n' % sec.crn
            msg += 'Remain seats change from %s to %s' % (
                      str(rem_num - seats_change),
                      str(rem_num)
                    )
<<<<<<< HEAD
            #users = sec.myuser_set.all()
            #emails = [user.user.email for user in users]
            #send_email.delay(emails, msg)
=======
            users = sec.myuser_set.all()
            emails = [user.user.email for user in users]
            send_email.delay(emails, msg)
>>>>>>> d3f7491698355126aef433b42507e553dd93d99d


@task
def send_email(emails, msg):
    send_mail('Purdue Seats Report', msg, 'purdueseats@gmail.com', emails)
