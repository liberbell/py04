import requests

def main():
    url = "https://httpbin.org/xml"
    result = requests.get(url)
    printResults(result)

    url = "https://httpbin.org/get"
    dataValues = {
        "key1": "value1",
        "key2": "value2"
    }
    result = requests.get(url, params=dataValues)
    printResults(result)

    url = "https://httpbin.org/post"
    dataValues = {
        "postkey1": "post1",
        "postkey2": "post2"
    }
    result = requests.post(url, data=dataValues)
    printResults(result)

def printResults(resData):
    print("Result data: {0}".format(resData.status_code))
    print('\n')

    print('Headers:------------')
    print(resData.headers)
    print('\n')

    print('Returned data-------')
    print(resData.text)

if __name__ == '__main__':
    main()
