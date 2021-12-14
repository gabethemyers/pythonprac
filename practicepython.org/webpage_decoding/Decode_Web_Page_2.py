from requests_html import HTML, HTMLSession

session = HTMLSession()
r = session.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')

paragraphs = r.html.find('p')

for paragraph in paragraphs:
    print(paragraph.text)
    print()