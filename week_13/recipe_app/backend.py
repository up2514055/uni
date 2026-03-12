class Recipe:

    def __init__(self, name, cooking_time, steps):
        self.name = name
        self.cooking_time = cooking_time
        self.steps = steps


class RecipeBook:

    def __init__(self):
        self.recipes = []

    def add_recipe(self, name, cooking_time, steps):
        new_recipe = Recipe(name, cooking_time, steps)
        self.recipes.append(new_recipe)

    def get_recipe_at(self, index):
        return self.recipes[index]

    def get_num_recipes(self):
        return len(self.recipes)
