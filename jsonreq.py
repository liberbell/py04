import requests
import json

def main():
    url = 'https://httpbin.org/json'
    result = requests.get(url)

if __name__ == '__main__':
    main()
