import xml.dom.minidom
import requests

def main():
    url = 'https://httpbin.org/xml'
    result = requests.get(url)

    domtree = xml.dom.minidom.parseString(result.text)
    rootnode = domtree.documentElement


if __name__ == '__main__':
    main()
