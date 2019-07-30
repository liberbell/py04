import urllib.request
import urllib.parse

def main():
    url = "https://httpbin.org/get"

    args = {
    "name": "tanaka takeshi",
    "is_author": "True"
    }

    result = urllib.request.urlopen(url)

if __name__ == '__main__':
    main()
