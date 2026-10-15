'''Pad Thai'''
def main():
    '''Pad Thai'''
    recipe = {
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
        "Bean Sprouts", "Noodle", "Chives", "Lime",
        "Egg", "Oil", "Peanuts"
    }
    required_tastes = {"Sweet", "Sour", "Salty"}

    user_ingredients = set()
    while True:
        item = input()
        if item == "Cook":
            break
        user_ingredients.add(item)

    user_tastes = set()
    while True:
        taste = input()
        if taste == "End":
            break
        user_tastes.add(taste)

    if not user_ingredients.issubset(recipe):
        print("This is not Pad Thai!!!")
    elif user_ingredients != recipe:
        print("This is bad!")
    elif user_tastes == required_tastes:
        print("Delicious!")
    else:
        print("Not Bad...")

main()
