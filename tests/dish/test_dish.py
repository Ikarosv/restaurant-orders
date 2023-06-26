from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish1 = Dish("Lasanha", 25.99)
    assert dish1.name == "Lasanha"
    assert dish1.price == 25.99
    assert dish1.recipe == {}
    assert repr(dish1) == "Dish('Lasanha', R$25.99)"

    dish2 = Dish("Lasanha", 25.99)
    dish3 = Dish("Ravioli", 18.5)

    assert dish1 == dish2
    assert dish1 != dish3
    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("carne")

    dish1.add_ingredient_dependency(ingredient1, 200)
    dish1.add_ingredient_dependency(ingredient2, 300)

    assert dish1.recipe == {ingredient1: 200, ingredient2: 300}

    assert dish1.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert dish1.get_ingredients() == {ingredient1, ingredient2}

    with pytest.raises(TypeError):
        Dish("Lasanha", "25.99")
    with pytest.raises(ValueError):
        Dish("Lasanha", -10)
    dish1.add_ingredient_dependency(ingredient1, 200)

    with pytest.raises(KeyError):
        dish2.recipe[ingredient1]
