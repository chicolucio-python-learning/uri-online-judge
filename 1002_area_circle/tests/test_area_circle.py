from unittest import TestCase

from area_circle import area_circle

# Tests based on input and output samples from the problem description


class TestAreaCircle(TestCase):
    def test_R_2_00(self):
        self.assertEqual(area_circle(2.00), '12.5664')

    def test_R_100_64(self):
        self.assertEqual(area_circle(100.64), '31819.3103')

    def test_R_150_00(self):
        self.assertEqual(area_circle(150.00), '70685.7750')
