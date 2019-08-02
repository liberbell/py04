import json

def main():
    jsonStr = '''{
        "sandwich": "Reuben",
        "toasted": true,
        "toppings": [
            "Thousand island Dressing",
            "Sauerkraut",
            "Pickles"
        ],
        "price": 8.99
    }'''

    data = json.loads(jsonStr)

    print('Sandwich: ' + data['sandwich'])
    if (data['toasted']):
        print('And it`s toasted.')

    for topping in data['toppings']:
        print('Topping: ' + topping)

if __name__ == '__main__':
    main()
