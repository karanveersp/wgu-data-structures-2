from greedy_mealplan import Food, MealPlan

def get_egg():
    return Food("Egg", 6, 5, 0, 72)

def get_lettuce():
    return Food("Lettuce", 1, 0, 2, 8)

def get_avocado():
    return Food("Avocado", 4, 29, 17, 322)

def get_banana():
    return Food("Banana", 1, 0, 27, 105)

def test_fraction_to_fit_calories_works():
    # Arrange
    food = get_egg()
    mp = MealPlan()

    # Act
    fraction = mp.fraction_to_fit_calories_limit(food, 36)

    # Assert
    assert fraction == 0.5

def test_fraction_to_fit_calories_is_one():
    # Arrange
    food = get_egg()
    mp = MealPlan()

    # Act
    fraction = mp.fraction_to_fit_calories_limit(food, 100)

    assert fraction == 1.0


def test_fraction_to_fit_nutrient_includes_whole():
    # Arrange
    food = get_egg()
    mp = MealPlan()

    # Act
    fraction = mp.fraction_to_fit_nutrient_goal(food, "protein", 0.4)

    # Assert
    # Since an egg has 33% protein, 40% goal would include the whole egg.
    assert fraction == 1.0


def test_fraction_to_fit_nutrient_is_partial():
    # Arrange
    food = get_egg()
    mp = MealPlan()

    # Act
    fraction = mp.fraction_to_fit_nutrient_goal(food, "protein", 0.3)

    # Assert
    # Since an egg has 33% protein, 30% goal would include the partial egg.
    assert fraction == 0.89


def test_mp_meets_calorie_limit_threshold():
    mp = MealPlan()
    mp.add_food(get_egg())

    for total_calories in (1999.9, 2000, 2000.1):
        mp.total_calories = total_calories
        assert mp.meets_calorie_limit(2000, 0.2)


def test_mp_meets_nutrient_goal_threshold():
    mp = MealPlan()
    mp.add_food(get_egg())

    for goal in (33.2, 33.3, 33.4):
        assert mp.meets_nutrient_goal("protein", goal/100, 0.001)
