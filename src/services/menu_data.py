import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self._read_csv_file(source_path)

    def _read_csv_file(self, source_path: str):
        try:
            new_menu = set()
            with open(source_path, encoding="utf-8") as csvfile:
                rawdata = csv.reader(csvfile, delimiter=",", quotechar='"')
                next(rawdata)  # Ignorar o cabeçalho do CSV
                for row in rawdata:
                    (
                        dish_name,
                        dish_price,
                        ingredient_name,
                        ingredient_amount,
                    ) = row
                    dish = self._get_or_create_dish(
                        new_menu, dish_name, float(dish_price)
                    )
                    ingredient = Ingredient(ingredient_name)
                    dish.add_ingredient_dependency(
                        ingredient, int(ingredient_amount)
                    )
            return new_menu
        except FileNotFoundError:
            print("Arquivo inexistente")
            return set()

    def _get_or_create_dish(self, recipes, name, price):
        for dish in recipes:
            if dish.name == name and dish.price == price:
                return dish
        new_dish = Dish(name, price)
        recipes.add(new_dish)
        return new_dish
