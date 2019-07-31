import requests

def main():
    url = 'https://httpbin.org/status/404'
    result = requests.get(url)
    printResults(result)


def printResults(resData):
    print('Result data: {0}'.format(resData.status_code))
    print('\n')

    print('Returned data-------------')
    print(resData)


if __name__ == '__main__':
    main()
