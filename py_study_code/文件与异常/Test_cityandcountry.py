import unittest
from city_functions import fun
class CitysTestCase(unittest.TestCase):
    def test_city_country(self):
        cit=fun('santiago','chile')
        self.assertEqual(cit,'Santiago Chile')
    def test_popilation(self):
        popu=fun('santiago','chile',5000000)
        self.assertEqual(popu,'Santiago,Chile-population 5000000')


if __name__ == '__main__':
    unittest
