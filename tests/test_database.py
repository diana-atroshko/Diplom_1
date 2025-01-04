import unittest
import allure
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database

@allure.suite('Тесты базы данных')
class TestDatabase(unittest.TestCase):
    @allure.description('Создает экземпляр Database для тестирования.')
    def setUp(self):
        self.database = Database()

    @pytest.mark.parametrize("expected_bun, index", [
        ("black bun", 0),
        ("white bun", 1),
        ("red bun", 2),
    ])
    @allure.testcase('Тестирование доступных булочек')
    @allure.step('Проверка, что метод available_buns возвращает правильный список булочек.')
    def test_available_buns(self, expected_bun, index):
        buns = self.database.available_buns()
        assert len(buns) == 3
        assert buns[index].get_name() == expected_bun

    @pytest.mark.parametrize("expected_ingredient, index", [
        ("hot sauce", 0),
        ("sour cream", 1),
        ("chili sauce", 2),
        ("cutlet", 3),
        ("dinosaur", 4),
        ("sausage", 5),
    ])
    @allure.testcase('Тестирование доступных ингредиентов')
    @allure.step('Проверка, что метод available_ingredients возвращает правильный список ингредиентов.')
    def test_available_ingredients(self, expected_ingredient, index):
        ingredients = self.database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[index].get_name() == expected_ingredient

    @allure.testcase('Тестирование типов ингредиентов')
    @allure.step('Проверка, что типы ингредиентов соответствуют ожидаемым.')
    def test_ingredient_types(self):
        ingredients = self.database.available_ingredients()
        for ingredient in ingredients:
            if ingredient.get_name() in ["hot sauce", "sour cream", "chili sauce"]:
                assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
            else:
                assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

