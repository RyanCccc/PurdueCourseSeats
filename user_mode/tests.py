"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from seats_check.models import Section
from user_mode.models import MyUser

class SimpleTest(TestCase):
    fixtures = [
        'user_mode.json'
    ]

    def test_remove_sec_when_deleting(self):
        """
        Tests remove empty sections when deleting
        """
        c = Client()
        resp = c.post(reverse('user_mode_login'),
                {'username':'test','password':'123456'}, follow=True)
        self.assertContains(resp, 'id="add_sec"')
        resp = c.post(reverse('user_mode_remove_crn'), {'crn':'10001'}, follow=True)
        self.assertNotContains(resp, 'Aeromechanics')
        sec_num = len(Section.objects.filter(crn='10001'))
        self.assertEqual(sec_num, 0)


    def test_add_sec(self):
        c = Client()
        resp = c.post(reverse('user_mode_login'),
                {'username':'test','password':'123456'}, follow=True)
        self.assertContains(resp, 'id="add_sec"')
        resp = c.post(reverse('user_mode_dashboard'), 
                {'crn':'58652', 'term':'Fall 2013'},
                follow=True)
        self.assertContains(resp, 'LM7')


    def test_login(self):
        c = Client()
        resp = c.post(reverse('user_mode_login'),
                {'username':'test','password':'123456'}, follow=True)
        self.assertContains(resp, 'id="add_sec"')
