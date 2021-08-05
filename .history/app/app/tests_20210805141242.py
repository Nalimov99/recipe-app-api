from django.test import TestCase

from app.calc import add, subtract

class CalcTest(TestCase):
    def test_two_numbers(self):
        '''Tests two numbers together'''
        self.assertEqual(add(2, 5), 7)
    
    def test_subtract_numbers(self):
        self.assertEqual(subtract(5, 10), 5)
