"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

   ��	���� with more a   priate tests for your application.
"""

from django.test import TestCase
import xml.etree.ElementTree as ET

from weixin.util import parse_xml, test_str, test_str_1, test_str_2


class SimpleTest(TestCase):
    def test_crn(self):
        """
        Tests crn
        """
        result = parse_xml(test_str)
        content = self._get_content_from_resp(result)
        self.assertTrue('CRN' in content)

    def test_base_class_search(self):
        """
        Tests class search
        """
        result = parse_xml(test_str_1)
        content = self._get_content_from_resp(result)
        self.assertTrue('===' in content)

    def test_timeout_class_search(self):
        """
        Tests class search cause timeout
        """
        result = parse_xml(test_str_2, 1)
        content = self._get_content_from_resp(result)
        print content
        self.assertTrue('large' in content)

    def _get_content_from_resp(self, in_str):
        root = ET.fromstring(in_str) 
        content =  root.find('Content').text
        return content
