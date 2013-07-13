from django.db import models
from django.contrib.auth.models import User as Auth_User
from seats_check.models import Section
# Create your models here.


class MyUserManager(models.Manager):
    def create_user(self, username, email, password, firstname, lastname):
        user = Auth_User.objects.create_user(
                username, 
                email,
                password,
                first_name = firstname,
                last_name = lastname
                )
        my_user = self.create(
            user = user,
            pwd = password
        )
        return my_user

class MyUser(models.Model):
    user = models.OneToOneField(Auth_User, primary_key=True)
    pwd = models.CharField(max_length=100)
    sections = models.ManyToManyField(Section)

    def add_section(self, crn, term):
        sec = None
        try:
            sec = Section.objects.get(crn = crn, term = term)
        except:
            sec = Section.objects.create_new_section(crn, term)
        if not isinstance(sec, Exception):
            if not sec in self.sections.all():
                self.sections.add(sec)
        else:
            err = sec
            raise sec

    def add_sections(self, **secs):
        for crn, term in secs.iteritems():
            sec = None
            try:
                sec = Section.objects.get(crn, term)
            except:
                sec = Section.objects.create_new_section(crn, term)
            if not isinstance(sec, Exception):
                if not sec in self.sections.all():
                    self.sections.add(sec)
            else:
                err = sec
                raise err

    objects = MyUserManager()
