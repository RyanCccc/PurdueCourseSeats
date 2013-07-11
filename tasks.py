# -*- coding: utf-8 -*-
import logging

import os
from celery import Celery
from celery.task import periodic_task
from datetime import timedelta
from os import environ

from django.conf import settings

#from seats_check.models import Section
#from seats_check import util

@periodic_task(run_every=timedelta(seconds=20))
def update_periodic():
    if not settings.configured:
        os.environ["DJANGO_SETTINGS_MODULE"] = "PCS.settings"
    from seats_check.models import Section
    from seats_check import util
    secs = Section.objects.all()
    for sec in secs:
        max_num, curr_num, name, code, number = util.get_all(sec.crn, sec.term)
        rem_num = max_num - curr_num
        seats_change = rem_num - sec.remain_seats_num
        sec.max_seats_num = max_num
        sec.current_seats_num = curr_num
        sec.remain_seats_num = rem_num
        sec.save()
        msg = '您订阅的课 %s ,课号 %s, Section Number是%s, CRN为%s, 一共有%d个位置, 现在还剩下%d' % (name, code, number, sec.crn, max_num, rem_num)
        if seats_change > 0:
            msg = 'Wow!!! 您的课号 %d 有新的位置啦！赶紧去抢下吧！！\n' % sec.crn + msg
        elif seats_change < 0:
            msg = 'Sorry!!! 您的课号 %d 的位置又在减少，要小心了哟。。\n' % sec.crn + msg
