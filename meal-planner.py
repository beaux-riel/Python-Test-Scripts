"""
Meal Planner version 1.0
Creator: Beaux Walton
"""

# Import libraries and modules.
import random

# Single serve meals.
meals = [
	'Tofu Bowl', 'Salmon', 'Balls and Salad', 'Homemade Pizza', 'Random choice', 'Pasta', 'Cauliflower Tacos', 'Butter Cauliflower', 'Nachos', 'Stirfry', 'Wraps', 'Pulled Carrot', 'Mac and Cheese'
	]

# Meals that cover 2 nights.
bigMeals = [
	'Chicken Salad', 'Perogies', 'Veggie Burgers'
	]

# This option includes big meal.
def save():
	week = random.sample(meals, 5)
	for meal in week:
		print(meal)
	
	bigMeal = random.choice(bigMeals)
	print(f'{bigMeal} x 2')

# This option offers a different meal each night.
def variety():
	week = random.sample(meals, 7)
	for meal in week:
		print(meal)

# This randomly decides if a big meal is included.
def show():
	repeat = bool(random.getrandbits(1))

	if repeat:
		save()
	else:
		variety()

# Provides output based on number of weeks (variable i).
i = 1
while i <= 12:
	print(f'\nWeek {i}:')
	show()
	i += 1
