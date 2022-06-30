import random
import unittest

# Create your tests here.
from numpy.testing._private.parameterized import parameterized

from scraper import get_information_localitate


def get_tests():
    with open("testData/localitati.txt") as f:
        cities = [city.strip() for city in f.readlines()]
    with open("testData/cod_matrici.txt") as f:
        matrix_codes = [code.strip() for code in f.readlines()]
    print([[code, random.choice(cities)] for code in matrix_codes])
    return [[code, random.choice(cities)] for code in matrix_codes]


class APITests(unittest.TestCase):
    @parameterized.expand(get_tests())
    def test_no_errors(self, matrix_name, localitate):
        get_information_localitate(matrix_name, localitate)
