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


def sort_files(files):
    full_text = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as file_obj:
            text = []
            text.append(file)
            for line in file_obj:
                text.append(line.strip())
        full_text.append(text)
        sorted(full_text)
    return full_text


files = ['1.txt', '2.txt', '3.txt']
full_text = sort_files(files)


def resul_txt(full_text):
    with open('result.txt', 'w', encoding='utf-8') as file_obj:
        for text in full_text:
            file_obj.write(str(len(text)-1))
            file_obj.write('\n')
            for line in text:
                file_obj.write(line)
                file_obj.write('\n')


resul_txt(full_text)
