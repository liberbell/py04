def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Cooking the first side')

def make_omlette(ingredient):
    mix_and_cook()
    omelette = 'a tasty omelette'.format(ingredient)
    return omelette

def make_pancake():
    mix_and_cook()
    pancake = 'a delicious pancake'
    return pancake
