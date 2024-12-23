import unittest
import allure
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database

@allure.suite('Тесты базы данных')
class TestDatabase(unittest.TestCase):
    @allure.description('Создает экземпляр Database для тестирования.')
    def setUp(self):
        self.database = Database()

    @allure.testcase('Тестирование доступных булочек')
    @allure.step('Проверка, что метод available_buns возвращает правильный список булочек.')
    def test_available_buns(self):
        buns = self.database.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    @allure.testcase('Тестирование доступных ингредиентов')
    @allure.step('Проверка, что метод available_ingredients возвращает правильный список ингредиентов.')
    def test_available_ingredients(self):
        ingredients = self.database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[5].get_name() == "sausage"

    @allure.testcase('Тестирование типов ингредиентов')
    @allure.step('Проверка, что типы ингредиентов соответствуют ожидаемым.')
    def test_ingredient_types(self):
        ingredients = self.database.available_ingredients()
        for ingredient in ingredients:
            if ingredient.get_name() in ["hot sauce", "sour cream", "chili sauce"]:
                assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
            else:
                assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

