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

@periodic_task(run_every=timedelta(seconds=60))
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
        old_remain = sec.remain_seats_num
        seats_change = rem_num - sec.remain_seats_num
        sec.max_seats_num = max_num
        sec.current_seats_num = curr_num
        sec.remain_seats_num = rem_num
        sec.save()
        if seats_change > 0:
            msg = 'Wow! your class %s has new seats released!!\n Remain seats change from %s to %s' % (
                      sec.crn, 
                      str(old_remain),
                      str(rem_num)
                   )
            msg += ('\n\n Once you don\'t need this section any more, '
                    'you can log in purdue-class.chenrendong.com to remove this'
                    ' section.')
            users = sec.myuser_set.all()
            restricts = sec.send_restrict.all()
            if not old_remain:
                emails = [user.user.email for user in users]
            else:
                emails = [user.user.email for user in users if user not in restricts]
            if emails:
                send_email.delay(emails, msg)
        elif seats_change < 0:
            msg = 'Sorry!!! You class\n %s \nSeats are decreasing!!\n' % sec.crn
            msg += 'Remain seats change from %s to %s' % (
                      str(rem_num - seats_change),
                      str(rem_num)
                    )
            #users = sec.myuser_set.all()
            #emails = [user.user.email for user in users]
            #send_email.delay(emails, msg)

@task
def send_email(emails, msg):
    send_mail('Purdue Seats Report', msg, 'purdueseats@gmail.com', emails)
