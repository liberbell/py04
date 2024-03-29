import requests
from lxml import etree

def main():
    url = 'https://httpbin.org/xml'
    result = requests.get(url)

    doc = etree.fromstring(result.content)
    # print(result.text)

    print(doc.tag)
    print(doc.attrib['title'])

    for elem in doc.findall('slide'):
        print(elem.tag)

    slideCount = len(doc.findall('slide'))
    print('There are {0} slide elements.'.format(slideCount))

    newSlide = etree.SubElement(doc, 'slide')
    newSlide.text = 'This is a new slide'

    slideCount = len(doc.findall('slide'))
    itemCount = len(doc.findall('.//slide'))

    print('There are {0} slide elements.'.format(slideCount))
    print('There are {0} item elements.'.format(itemCount))

    for elem in doc.findall('slide'):
        print(elem.tag)

if __name__ == '__main__':
    main()
