def get_shop_list_by_dishes(dishes, person_count):
    try:
        namefile = 'cook book.txt'
        with open(namefile) as file_object:
            cook_book = {}
            while True:
                name_dish = file_object.readline().strip()
                if name_dish == '':
                    break
                else:
                    amt_ing_dish = int(file_object.readline())
                    ingredients = []
                    for i in range(amt_ing_dish):
                        ing = file_object.readline().strip()
                        ingredient = ing.split('|')
                        ingredient_name, quantity, measure = ingredient
                        ingredients.append(dict(ingredient_name=ingredient_name,
                                                quantity=quantity,
                                                measure=measure))
                    idle_line = file_object.readline()
                    cook_book[name_dish] = ingredients

        dictionary_ingredients = {}
        for name, product in cook_book.items():
            if name in dishes:
                for p in product:
                    dictionary_ingredients[p['ingredient_name']] = {
                        'measure': p['measure'],
                        'quantity': int(p['quantity']) * person_count}
        print(dictionary_ingredients)
    except FileNotFoundError:
        msg = "Sorry, the file "+ namefile + " does not exist."
        print(msg)


get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински'], 5)