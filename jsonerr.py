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

if __name__ == '__main__':
    main()
