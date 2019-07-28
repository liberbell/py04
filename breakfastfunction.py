def mix_and_cook:
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Cooking the first side')

def make_omlette(ingredient):
    mix_and_cook()
    omlette = 'a tasty omlette'.format(ingredient)
    return omlette

def make_pancake():
    mix_and_cook()
    pancake = 'a delicious pancake'
    return pancake
