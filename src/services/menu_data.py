import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self._load_dishes(source_path)

    def _load_dishes(self, source_path: str):
        try:
            with open(source_path, encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=",", quotechar='"')
                _, *data = reader
        except FileNotFoundError:
            print("File not found.")
            return set()
        dishes = set()
        for row in data:
            dishes = self._add_dish_by_row(dishes, row)
        return dishes

    def _add_dish_by_row(self, dishes_set, row):
        name, price, ingredient_name, ingredient_amount = row[:4]

        dish = next((dish for dish in dishes_set if dish.name == name), None)
        if dish is None:
            dish = Dish(name, float(price))
            dishes_set.add(dish)

        ingredient = Ingredient(ingredient_name)
        dish.add_ingredient_dependency(ingredient, int(ingredient_amount))
        return dishes_set
