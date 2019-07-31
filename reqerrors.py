import requests
from requests import HTTPError

def main():
    try:
        url = 'https://httpbin.org/status/404'
        result = requests.get(url)
        printResults(result)
    except HTTPError as err:
        print('Error : {0}'.format(err))


def printResults(resData):
    print('Result data: {0}'.format(resData.status_code))
    print('\n')

    print('Returned data-------------')
    print(resData)


if __name__ == '__main__':
    main()
