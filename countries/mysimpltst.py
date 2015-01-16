import unittest

from countries.models import Country


# Create your tests here.
class BlogTests(unittest.TestCase):
    
    cty = Country;

    def setUp(self):
        
        self.cty.name = 'Khalistan'
        self.cty.code = 'KHL'
        
        
    def testUnicode(self):
        self.assertEqual(self.cty.__unicode__(), 'KHL - Khalistan')   
        
        
    if __name__ == '__main__':
        unittest.main()