import unittest
from search_address import search_address

class MyTestCase(unittest.TestCase):
    def test_郵便番号から住所を取得できる_0287111(self):
        postal_code ="0287111"
        address = search_address(postal_code)
        expect = "岩手県八幡平市大更"

        self.assertEqual(expect, address)

class MyTestCase(unittest.TestCase):
    def test_郵便番号から住所を取得できる_0028061(self):
        postal_code ="0028061"
        address = search_address(postal_code)
        expect = "北海道札幌市北区拓北一条"

        self.assertEqual(expect, address)

class MyTestCase(unittest.TestCase):
    def test_郵便番号から住所を取得できる_1620055(self):
        postal_code ="1620055"
        address = search_address(postal_code)
        expect = "東京都新宿区余丁町"

        self.assertEqual(expect, address)

if __name__ == '__main__':
    unittest.main()