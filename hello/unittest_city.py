import unittest

from city import get_city_name


class CityUnitTest(unittest.TestCase):
    def test_get_city_name(self):
        formatedname = get_city_name('shanghai','china')
        self.assertEqual(formatedname,'Shanghai,China')

unittest.main()
