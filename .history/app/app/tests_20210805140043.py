from django.test import TestCase

from app.calc import add

class CalcTest(TestCase):
	def test_two_numbers(self):
		'''Tests two numbers together'''
		self.assertEqual(add(2, 5), 7)