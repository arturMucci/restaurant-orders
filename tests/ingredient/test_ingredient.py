from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    name1 = "queijo mussarela"
    name2 = "farinha"
    ingredient1 = Ingredient(name1)
    ingredient2 = Ingredient(name1)
    ingredient3 = Ingredient(name2)

    assert ingredient1.name == name1
    assert ingredient1.__eq__(ingredient2)
    assert ingredient1.__hash__() == ingredient2.__hash__()
    assert ingredient1.__hash__() != ingredient3.__hash__()
    assert ingredient1.__repr__() == "Ingredient('queijo mussarela')"
    assert ingredient1.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
