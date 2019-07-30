import requests

def main():
    url = "https://httpbin.org/xml"
    result = requests.get(url)
    printResults(result)

def printResults(resData):
    print("Result data: {0}".format(resData.status_code))
    print('\n')

    print('Headers:------------')
    print(resData.headers)
    print('\n')

    print('Returned data-------')
    print(resData.content)

if __name__ == '__main__':
    main()
