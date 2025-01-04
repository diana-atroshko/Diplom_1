import unittest
import allure
from praktikum.bun import Bun

@allure.suite('Тесты булочек')
class TestBun(unittest.TestCase):

    @allure.description('Создает экземпляр Bun')
    def setUp(self):
        self.bun = Bun("black bun", 100.0)

    @allure.testcase('Тестирование получения имени булочки')
    @allure.step('Проверка, что метод get_name возвращает правильное имя булочки.')
    def test_get_name(self):
        assert self.bun.get_name() == "black bun"

    @allure.testcase('Тестирование получения цены булочки')
    @allure.step('Проверка, что метод get_price возвращает правильную цену булочки.')
    def test_get_price(self):
        assert self.bun.get_price() == 100.0

    @allure.testcase('Тестирование типа имени булочки')
    @allure.step('Проверка, что имя булочки является строкой.')
    def test_name_type(self):
        assert type(self.bun.get_name()) is str

    @allure.testcase('Тестирование типа цены булочки')
    @allure.step('Проверка, что цена булочки является числом (тип float).')
    def test_price_type(self):
        assert type(self.bun.get_price()) is float