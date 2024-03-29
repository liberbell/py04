import requests
from requests.auth import HTTPBasicAuth

def main():
    url = 'https://httpbin.org/basic-auth/usera/passwd'
    mycred = HTTPBasicAuth('usera', 'passwd')
    result = requests.get(url, auth=('usera', 'passw'))

    printResults(result)

def printResults(resData):
    print('Result data: {0}'.format(resData.status_code))
    print('\n')

    print('Returned data-------------')
    print(resData)

if __name__ == '__main__':
    main()
