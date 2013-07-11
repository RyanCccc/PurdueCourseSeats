from django.db import models

from seats_check.util import get_all
from seats_check.util import ParserException
# Create your models here.
class SectionManager(models.Manager):
    def create_section(self, crn, max_num, curr_num, term, name, code, number):
        sec = self.create(
                crn = crn, 
                max_seats_num = max_num, 
                current_seats_num = curr_num,
                remain_seats_num = (max_num - curr_num),
                term = term,
                name = name,
                code = code,
                number = number)
        return sec

    def create_new_section(self, crn, term):
        try:
            max_num, curr_num, name, code, number = get_all(crn, term)
            return self.create_section(
                        crn, 
                        max_num,
                        curr_num,
                        term,
                        name,
                        code,
                        number
                    )
        except ParserException as e:
            return e

class Section(models.Model):
    crn = models.CharField(max_length=10)
    max_seats_num = models.IntegerField()
    current_seats_num = models.IntegerField()
    remain_seats_num = models.IntegerField()
    term = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    objects = SectionManager()
