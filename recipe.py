import sys

cookbook = {'sandwich' : {'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'], 'meal' : 'lunch', 'prep_time' : '10'},
    'cake' : {'ingredients' : ['flour', 'sugar', 'eggs'], 'meal' : 'dessert', 'prep_time' : '60'},
    'salad' : {'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal' : 'lunch', 'prep_time' : '15'}}

options = [str(i) for i in range(1, 6)]

def print_recipe(r):
    if r not in cookbook.keys():
        print ('\nThe recipe for %s does not exist' % r)
        return
    print ('\nRecipe for %s:' % r)
    print ('Ingredients list: ', cookbook[r]['ingredients'])
    print ('To be eaten for %s.' % cookbook[r]['meal'])
    print ('Takes %s minutes of cooking.' % cookbook[r]['prep_time'])

print ('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit')
x = '0'
while (x != '5'):
    x = input()
    if x not in options:
        print ('This option does not exist, please type the corresponding number.\nTo exit, enter 5.')
    elif x == '1':
        x = '0'
        while (x == '0'):
            name = input('Please enter the name of the recipe: ')
            if name in cookbook.keys():
                print ('The recipe for %s already exists' % name)
            else:
                x = '1'
        ing = input('Please enter the ingredients separated by \', \': ').split(", ")
        meal = input('Please enter the meal type: ')
        time = input('Please enter the preparation time in minutes (careful here, I will not verify if you do not use numbers): ')
        cookbook[name] = {'ingredients' : ing, 'meal' : meal, 'prep_time' : time}
    elif x == '2':
        name = input('Please enter the name of the recipe you want to remove: ')
        cookbook.pop(name, "None")
    elif x == '3':
        r = input('Please enter the recipe\'s name to get its details: ')
        print_recipe(r)
    elif x == '4':
        for r in cookbook.keys():
            print_recipe(r)
    elif x == '5':
        sys.exit()
    if x in options:
        print ('\nCan I help you with anything else?\nTo exit, enter 5.')
    
