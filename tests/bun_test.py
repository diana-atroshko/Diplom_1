import unittest


from praktikum.bun import Bun


class TestBun(unittest.TestCase):

    def setUp(self):
        self.bun = Bun("Краторная булка N-200i", 1255.5)

    def test_get_name(self):
        assert self.bun.get_name() == "Краторная булка N-200i"

    def test_get_price(self):
        assert self.bun.get_price() == 1255.5

    def test_name_type(self):
        assert type(self.bun.get_name()) is str

    def test_price_type(self):
        assert type(self.bun.get_price()) is float