import unittest
from city_functions import city_country

class test(unittest.TestCase):
	def test_city_country(self):
		city_name = city_country('santiago', 'chile')
		self.assertEqual(city_name, 'Santiago, Chile')
		
	def test_city_country_population(self):
		city_name = city_country('santiago', 'chile', population = 5000000)
		self.assertEqual(city_name, 'Santiago, Chile - population 5000000')

unittest.main()

