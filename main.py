from pprint import pprint


with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = []
        name = line.strip()
        number = int(file.readline())
        for item in range(number):
            data = file.readline().strip()
            ingredients = {}
            ingredients['ingredient_name'] = data.split(' | ')[0]
            ingredients['quantity'] = data.split(' | ')[1]
            ingredients['measure'] = data.split(' | ')[2]
            dish.append(ingredients)
        cook_book[name] = dish
        file.readline()
    pprint(cook_book)


def get_shop_list_by_dishes(dishes, person):
    num_of_ingred = {}
    for dish in dishes:
        recipe = cook_book.get(dish, None)
        if recipe:
            for name in recipe:
                if name['ingredient_name'] not in num_of_ingred:
                    pustoi_dict = {}
                    pustoi_dict['quantity'] = int(name.get('quantity')) * person
                    pustoi_dict['measure'] = name.get('measure')
                    num_of_ingred[name['ingredient_name']] = pustoi_dict
                else:
                    accum = num_of_ingred.get(name['ingredient_name']).get('quantity')
                    accum += int(name.get('quantity')) * person
                    num_of_ingred[name['ingredient_name']] = accum
    pprint(num_of_ingred)


get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)


with open('1.txt', 'r', encoding='utf-8') as file_obj:
    text1 = []
    for line in file_obj:
        text1.append(line.strip())


with open('2.txt', 'r', encoding='utf-8') as file_obj:
    text2 = []
    for line in file_obj:
        text2.append(line.strip())


with open('3.txt', 'r', encoding='utf-8') as file_obj:
    text3 = []
    for line in file_obj:
        text3.append(line.strip())


# def func(one, two, three):
#     with open('result.txt', 'a', encoding='utf-8') as file_obj:
#         result = [one, two, three]
#         for i in result:
#             maxim = max(result)
#             for item in maxim:
#                 file_obj.write(item)
#             result.remove(maxim)
#         file_obj.write('\n')
#
#
# func(text1, text2, text3)
