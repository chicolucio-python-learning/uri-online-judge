from unittest import TestCase

from time_conversion import time_conversion, time_format

# Tests based on input and output samples from the problem description


class TestTimeConversion(TestCase):
    def test_556(self):
        self.assertEqual(time_conversion(556), (0, 9, 16))

    def test_1(self):
        self.assertEqual(time_conversion(1), (0, 0, 1))

    def test_140153(self):
        self.assertEqual(time_conversion(140153), (38, 55, 53))


class TestTimeFormat(TestCase):
    def test_0_9_16(self):
        self.assertEqual(time_format((0, 9, 16)), '0:9:16')

    def test_0_0_1(self):
        self.assertEqual(time_format((0, 0, 1)), '0:0:1')

    def test_38_55_53(self):
        self.assertEqual(time_format((38, 55, 53)), '38:55:53')
