from tkinter import Tk, Frame, Label, Button, Toplevel, Text
from backend import RecipeBook


class RecipeBookApp:

    def __init__(self, recipe_book):
        self.recipe_book = recipe_book

        self.root = Tk()
        self.root.title("Digital Recipe Book")

        self.main_frame = Frame(self.root)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20)

    def run(self):
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        num_recipes = self.recipe_book.get_num_recipes()

        for i in range(num_recipes):
            recipe = self.recipe_book.get_recipe_at(i)

            name_label = Label(
                self.main_frame,
                text=f"{recipe.name} ({recipe.cooking_time} mins)"
            )
            name_label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            view_button = Button(
                self.main_frame,
                text="View Recipe",
                command=lambda index=i: self.open_recipe_window(index)
            )
            view_button.grid(row=i, column=1, padx=10, pady=10)

    def open_recipe_window(self, index):
        recipe = self.recipe_book.get_recipe_at(index)

        new_win = Toplevel(self.root)
        new_win.title(recipe.name)

        title_label = Label(new_win, text=recipe.name)
        title_label.pack(pady=5)

        time_label = Label(new_win, text=f"Cooking Time: {recipe.cooking_time} mins")
        time_label.pack(pady=5)

        steps_text = Text(new_win, height=10, width=50)
        steps_text.pack(pady=10)

        steps_text.insert("1.0", recipe.steps)

        steps_text.config(state="disabled")


def main():
    book = RecipeBook()

    book.add_recipe(
        "Spaghetti Bolognese",
        30,
        "1. Cook pasta.\n2. Cook mince.\n3. Add sauce.\n4. Combine and serve."
    )

    book.add_recipe(
        "Pancakes",
        15,
        "1. Mix flour and eggs.\n2. Add milk.\n3. Fry in pan.\n4. Serve with syrup."
    )

    app = RecipeBookApp(book)
    app.run()


if __name__ == "__main__":
    main()
