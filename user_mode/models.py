from django.db import models

from seats_check.models import Section
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    sections = models.ManyToManyField(Section)

    def change_pwd(self, pwd):
        self.password = pwd
        self.save()

    def change_email(self, email):
        self.email = email
        self.save()

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
                raise sec

def authenticate(username, password):
    user = None
    try:
        user = User.objects.get(username = username, password = password)
    except:
        pass
    return user
