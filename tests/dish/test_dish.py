from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from pytest import raises


# Req 2
def test_dish():
    name1 = "Batata recheada"
    price1 = 9.99
    dish1 = Dish(name1, price1)
    ingredient1 = Ingredient("bacon")

    name2 = "Canelone"
    price2 = 15.99
    dish2 = Dish(name2, price2)
    # ingredient2 = Ingredient("manteiga")

    assert dish1.name == name1
    assert dish2.name == name2
    assert hash(dish1) == hash(dish1)
    assert hash(dish1) != hash(dish2)
    assert dish1.__eq__(dish1) is True
    assert dish1.__eq__(dish2) is False
    assert dish1.__repr__() == f"Dish('{name1}', R${price1:.2f})"

    dish1.add_ingredient_dependency(ingredient1, 10)
    assert dish1.get_ingredients() == {ingredient1}

    teste = dish1.get_restrictions()
    assert dish1.get_restrictions()
    assert isinstance(teste, set)

    with raises(TypeError):
        Dish("Nome do Prato", "preço inválido")

    with raises(ValueError):
        Dish("Nome do Prato", 0)
