class Dish:
	def __init__(self, name, ingridients):
		self.name = name 
		self.ingridients = ingridients

class IngridientsToDishDict: 
	def __init__(self):
		self.ingridients_to_dish = {}

	def add_new_mappings_between_ingridient_and_dish_name(self, ingridients, dish_name):
		for ingridient in ingridients: 
			if ingridient in self.ingridients_to_dish:
				self.ingridients_to_dish[ingridient].append(dish_name)
				self.ingridients_to_dish[ingridient].sort()
			else: 
				self.ingridients_to_dish[ingridient] = [dish_name]

class DictToArrayService: 
	def convert_dict_to_2d_array(self, d):
		a = []
		for key in d: 
			inner_a = [key]
			inner_a += d[key]
			a.append(inner_a)
		return a 

def remove_from_array_if_length_less_than_three(a):
	return [e for e in a if len(e) >= 3]

def groupingDishes(dishes):
	ingridients_to_dish = IngridientsToDishDict()
	dishes = [Dish(dish[0], dish[1:]) for dish in dishes]

	for dish in dishes: 
		ingridients_to_dish.add_new_mappings_between_ingridient_and_dish_name(dish.ingridients, dish.name)

	dishes_grouping_array = DictToArrayService().convert_dict_to_2d_array(ingridients_to_dish.ingridients_to_dish)
	return sorted(remove_from_array_if_length_less_than_three(dishes_grouping_array))



dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

print groupingDishes(dishes)