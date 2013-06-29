from datetime import datetime
from datetime import time as TM

class Time_Interval: 
    def __str__(self):
        return self.time_raw
    def __unicode__(self):
        return self.time_raw + u''
    def __init__(self, time_raw):
        self.time_raw = time_raw
        start_raw, end_raw = time_raw.split(' - ')
        self.start_time = Class_Time(start_raw)
        self.end_time = Class_Time(end_raw)

class Class_Time(TM):
    def __new__(self, time_raw):
        return datetime.strptime(time_raw, '%I:%M %p').time()
