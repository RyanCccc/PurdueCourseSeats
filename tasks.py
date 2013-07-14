# -*- coding: utf-8 -*-
import logging

import os
from celery import Celery
from celery.task import periodic_task
from datetime import timedelta
from os import environ

from seats_check.models import Section
from seats_check import util
from django.conf import settings

@periodic_task(run_every=timedelta(seconds=20))
def update_periodic():
    secs = Section.objects.all()
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
            msg = 'Wow! your class %s has new seats released!!\n' % sec.crn + msg
        elif seats_change < 0:
            msg = 'Sorry!!! You class %s seats are decreasing!!\n' % sec.crn + msg
        print msg
