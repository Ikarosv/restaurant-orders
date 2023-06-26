from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    assert ingredient1.name == "queijo mussarela"
    assert ingredient1.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    ingredient2 = Ingredient("farinha")
    assert repr(ingredient2) == "Ingredient('farinha')"

    ingredient3 = Ingredient("bacon")
    ingredient4 = Ingredient("bacon")
    ingredient5 = Ingredient("queijo provolone")

    assert ingredient3 == ingredient4
    assert ingredient3 != ingredient1
    assert ingredient1 != ingredient5
    assert hash(ingredient3) == hash(ingredient4)
    assert hash(ingredient4) != hash(ingredient1)

    assert ingredient3.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    ingredient6 = Ingredient("massa de lasanha")
    assert ingredient6.name == "massa de lasanha"
    assert ingredient6.restrictions == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
    }
