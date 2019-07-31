import requests

def main():
    url = 'https://httpbin.org/status/404'
    result = requests.get(url)
    printResults(result)
