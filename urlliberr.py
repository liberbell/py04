import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError

def main():
    url = "https://no-such-server.org/html"
    # url = "https://httpbin.org/status/404"
    # url = "https://httpbin.org/html"
    try:
        result = urllib.request.urlopen(url)
        print("Result code: {0}".format(result.status))
        if (result.getcode() == HTTPStatus.OK):
            print(result.read().decode("UTF-8"))
    except HTTPError as err:
        print("Error: {0}".format(err.code))
    except URLError as err:
        print("That server is bank. {0}".format(err.reason))

if __name__ == '__main__':
    main()
