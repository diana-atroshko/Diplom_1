import unittest
import allure
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger

@allure.suite('Тесты ингредиентов')
class TestIngredient(unittest.TestCase):
    def setUp(self):
        self.ingredient = Ingredient("начинка","Говяжий метеорит", 3000.0)

    @allure.testcase('Тестирование получения цены')
    @allure.step('Проверка цены ингредиента')
    def test_get_price(self):
        assert self.ingredient.get_price() == 3000.0

    @allure.testcase('Тестирование типа цены')
    @allure.step('Проверка типа цены')
    def test_price_type(self):
        assert type(self.ingredient.get_price()) is float

    @allure.testcase('Тестирование получения имени')
    @allure.step('Проверка имени ингредиента')
    def test_get_name(self):
        assert self.ingredient.get_name() == 'Говяжий метеорит'

    @allure.testcase('Тестирование типа имени')
    @allure.step('Проверка типа имени')
    def test_name_type(self):
        assert type(self.ingredient.get_name()) is str

    @allure.testcase('Тестирование получения типа')
    @allure.step('Проверка типа ингредиента')
    def test_get_type(self):
        assert self.ingredient.get_type() == "начинка"

    @allure.testcase('Тестирование типа типа')
    @allure.step('Проверка типа ингредиента')
    def test_type_type(self):
        assert type(self.ingredient.get_type()) is str

