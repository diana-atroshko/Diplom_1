import unittest
import allure
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger

@allure.suite('Тесты бургеров')
class TestBurger(unittest.TestCase):

    @allure.description('Создает экземпляры Bun, Ingredient и Burger, чтобы использовать их в тестах.')
    def setUp(self):
        self.bun = Bun("black bun", 100.0)
        self.ingredient1 = Ingredient('FILLING',"cutlet", 100.0)
        self.ingredient2 = Ingredient('SAUCE',"sour cream", 200.0)
        self.burger = Burger()
        self.burger.set_buns(self.bun)

    @allure.testcase('Тестирование создания булочки')
    @allure.step('Проверка, что булочка была правильно создана.')
    def test_set_buns(self):
        assert self.burger.bun.get_name()== "black bun"
        assert self.burger.bun.get_price()== 100.0

    @allure.testcase('Тестирование добавления ингредиента')
    @allure.step('Проверка, что ингредиент добавляется в бургер.')
    def test_add_ingredient(self):
        self.burger.add_ingredient(self.ingredient1)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0].get_name()== "cutlet"

    @allure.testcase('Тестирование удаления ингредиента')
    @allure.step('Проверка, что ингредиент удаляется из бургера.')
    def test_remove_ingredient(self):
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0].get_name() == "sour cream"

    @allure.testcase('Тестирование перемещения ингредиента')
    @allure.step('Проверка, что ингредиент может быть перемещен в другой индекс.')
    def test_move_ingredient(self):
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[0].get_name() == "sour cream" and self.burger.ingredients[1].get_name()== "cutlet"

    @allure.testcase('Тестирование расчета цены бургера')
    @allure.step('Проверка, что цена бургера рассчитывается правильно с учетом булочки и ингредиентов.')
    def test_get_price(self):
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        expected_price = self.burger.bun.get_price()*2 + self.ingredient1.get_price() + self.ingredient2.get_price()
        assert expected_price == self.burger.get_price()

    @allure.testcase('Тестирование формирования чека')
    @allure.step('Проверка, что чек формируется правильно.')
    def test_get_receipt(self):
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        expected_receipt = (
            f'(==== {self.bun.get_name()} ====)\n'
            f'= {self.ingredient1.get_type().lower()} {self.ingredient1.get_name()} =\n'
            f'= {self.ingredient2.get_type().lower()} {self.ingredient2.get_name()} =\n'
            f'(==== {self.bun.get_name()} ====)\n'
            f'\n'
            f'Price: {self.burger.get_price()}'
        )
        assert expected_receipt == self.burger.get_receipt()