import xml.dom.minidom
import requests

def main():
    url = 'https://httpbin.org/xml'
    result = requests.get(url)

    domtree = xml.dom.minidom.parseString(result.text)
    rootnode = domtree.documentElement

    print('The root element is {0}'.format(rootnode.nodeName))
    print('Title: {0}'.format(rootnode.getAttribute('title')))


if __name__ == '__main__':
    main()
