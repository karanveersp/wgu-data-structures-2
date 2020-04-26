import sys, operator, random
from nutrition import Food, MealPlan

# Constants to be used by the greedy algorithm.
NUTRIENT_THRESHOLD = 0.001
FRACTION_THRESHOLD = 0.05
CALORIE_THRESHOLD = 0.1
MAX_CALORIES = 2000


def load_nutrient_data(filename):
    # Open file, read food items one line at a time,
    # create Food objects and append them to a list.
    # Return the list once the entire file is processed.
    foods = []
    with open(filename, "rt") as f:
        for line in f:
            name, nutrients = line.split(": ")
            p, c, f, total = list(map(float, nutrients.split(", ")))
            foods.append(Food(name, p, f, c, total))
    return foods

def sort_food_list(foods, nutrient):
    # Sort the food list based on the percent-by-calories of the
    # given nutrient ('protein', 'carbs' or 'fat')
    # The list is sorted in-place; nothing is returned.
    def percent_nutrient(food):
        return getattr(food, f"{nutrient}_calories")
    foods.sort(key=percent_nutrient, reverse=True)
    
def create_meal_plan(foods, nutrient, goal):
    # A greedy algorithm to create a meal plan that has MAX_CALORIES
    # calories and the goal amount of the nutrient (e.g. 30% protein)
    plan = MealPlan()
    sort_food_list(foods, nutrient)
    for f in foods:
        if is_empty(f, nutrient):
            continue
        
        nutrient_frac = plan.fraction_to_fit_nutrient_goal(f, nutrient, goal)
        calory_frac = plan.fraction_to_fit_calories_limit(f, MAX_CALORIES)

        entire_serving_can_be_added = nutrient_frac == 1.0 and calory_frac == 1.0

        if entire_serving_can_be_added:
            # print("Addding entire serving :", f)
            plan.add_food(f)
        elif nutrient_frac < 1.0:
            f.set_fraction(nutrient_frac)
            plan.add_food(f)
            # print("Added partial nutrient serving :", f)
        elif calory_frac < 1.0:
            f.set_fraction(calory_frac)
            plan.add_food(f)
            # print("Added partial calory serving :", f)
        else:
            continue
        if plan.meets_calorie_limit(MAX_CALORIES, CALORIE_THRESHOLD) and plan.meets_nutrient_goal(nutrient, goal, NUTRIENT_THRESHOLD):
            break
    return plan

def is_empty(food, nutrient):
    if food.calories < 0.1:
        return True
    if getattr(food, f"{nutrient}_calories") / food.calories < 0.001:
        return True
    return False
       
def print_menu():
    print()
    print("\t1 - Set maximum protein")
    print("\t2 - Set maximum carbs")
    print("\t3 - Set maximum fat")
    print("\t4 - Exit program")
    print()

if __name__ == "__main__":
    # 1. Load the food data from the file (change this to a user
    # prompt for the filename)
    filename = input("Enter name of food data file: ")
    foods = load_nutrient_data(filename)
    
    # 2. Display menu and get user's choice. Repeat menu until a
    # valid choice is entered by the user (1-4, inclusive).
    good_input = False
    print_menu()
    while not good_input:
        choice = input("Enter choice (1-4): ")
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice! Enter an integer from 1-4!")
            print_menu()
            continue
        choice = int(choice)
        good_input = True

    if choice == 4:
        exit(0)
    
    # 3. Prompt user for goal nutrient percent value. Repeat prompt
    # until a valid choice is entered by the user (0-100, inclusive)
    nutrients = {
        1: "protein",
        2: "carbs",
        3: "fat"
    }
    good_input = False
    while not good_input:
        percent = input(f"What percentage of calories from {nutrients[choice]} is the goal? ")
        try:
            goal = int(percent)
            if goal < 0 or goal > 100:
                continue
        except:
            continue
        goal = goal / 100
        good_input = True
    
    # 4. Run greedy algorithm to create the meal plan.
    plan = create_meal_plan(foods, nutrients[choice], goal)
    
    # 5. Display plan.
    print(plan)