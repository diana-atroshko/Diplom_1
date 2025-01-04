import unittest
import allure
from praktikum.ingredient import Ingredient


@allure.suite('Тесты ингредиентов')
class TestIngredient(unittest.TestCase):
    def setUp(self):
        self.ingredient = Ingredient('FILLING',"dinosaur", 200.0)

    @allure.testcase('Тестирование получения цены')
    @allure.step('Проверка цены ингредиента')
    def test_get_price(self):
        assert self.ingredient.get_price() == 200.0

    @allure.testcase('Тестирование типа цены')
    @allure.step('Проверка типа цены')
    def test_price_type(self):
        assert type(self.ingredient.get_price()) is float

    @allure.testcase('Тестирование получения имени')
    @allure.step('Проверка имени ингредиента')
    def test_get_name(self):
        assert self.ingredient.get_name() == "dinosaur"

    @allure.testcase('Тестирование типа имени')
    @allure.step('Проверка типа имени')
    def test_name_type(self):
        assert type(self.ingredient.get_name()) is str

    @allure.testcase('Тестирование получения типа')
    @allure.step('Проверка типа ингредиента')
    def test_get_type(self):
        assert self.ingredient.get_type() == 'FILLING'

    @allure.testcase('Тестирование типа типа')
    @allure.step('Проверка типа ингредиента')
    def test_type_type(self):
        assert type(self.ingredient.get_type()) is str

