import json
from json import JSONDecodeError

def main():
    jsonStr = '''{
        "sandwich": "Reuben",
        "toasted": true,
        "toppings": [
            "Thousand island Dressing",
            "Sauerkraut",
            "Pickles"
        ]
        "price": 8.99
    }'''

    try:
        data = json.loads(jsonStr)
    except JSONDecodeError as err:
        print('Ooops json decode error:')
        print(err.msg)
        print(err.lineno, err.colno)

    print('Sandwich: ' + data['sandwich'])
    if (data['toasted']):
        print('And it`s toasted.')

    for topping in data['toppings']:
        print('Topping: ' + topping)

if __name__ == '__main__':
    main()
