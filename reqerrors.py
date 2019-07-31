import requests
from requests import HTTPError, Timeout

def main():
    try:
        # url = 'https://httpbin.org/status/404'
        url = 'https://httpbin.org/delay/5'
        result = requests.get(url, timeout=2)
        result.raise_for_status()
        printResults(result)
    except HTTPError as err:
        print('Error : {0}'.format(err))
    except Timeout as err:
        print('Request Timeout: {0}'.format(err))

def printResults(resData):
    print('Result data: {0}'.format(resData.status_code))
    print('\n')

    print('Returned data-------------')
    print(resData)


if __name__ == '__main__':
    main()
