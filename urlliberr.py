import urllib.request
from http import HTTPStatus

def main():
    # url = "https://no-such-server.org/html"
    url = "https://httpbin.org/status/404"
    # url = "https://httpbin.org/html"

    result = urllib.request.urlopen(url)
    print("Result code: {0}".format(result.status))
    if (result.getcode() == HTTPStatus.OK):
        print(result.read().decode("UTF-8"))

if __name__ == '__main__':
    main()
