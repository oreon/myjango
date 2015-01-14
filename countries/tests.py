import unittest

import django
from django.test.testcases import SimpleTestCase

from countries.models import Country


# Create your tests here.
class BlogTests(SimpleTestCase):
    
    cty = Country();

    def setUp(self):
        #django.setup()
        
        self.cty.name = 'Khalistan'
        self.cty.code = 'KHL'
        #Country.objects.create(name = self.cty.name, code = self.cty.code)
        
        
    def testUnicode(self):
        self.assertEqual(self.cty.__unicode__(), 'KHL - Khalistan')   
        
        
    if __name__ == '__main__':
        unittest.main()