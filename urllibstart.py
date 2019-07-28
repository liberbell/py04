import urllib.request

def main:
    url = "https://httpbin.org/xml"

    result = urllib.result.urlopen(url)
    print("Result code: {0}".format(result.satus))

    print("Headers:----------")

    print("Returned data:----")
