import urllib.request

def main():
    url = "https://httpbin.org/html"
    url = "https://httpbin.org/html"
    url = "https://httpbin.org/html"

    result = urllib.request.urlopen(url)
    print("Result code: {0}".format(result.status))
    if (result.getcode() == 200):
        print(result.read().decode("UTF-8"))
