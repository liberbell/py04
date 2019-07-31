import requests

def main():
    url = 'https://httpbin.org/status/404'
    result = requests.get(url)
    printResults(result)


def printResults(resData):
    print('Result data: {0}'.format(resData.status_code))
    print('\n')
