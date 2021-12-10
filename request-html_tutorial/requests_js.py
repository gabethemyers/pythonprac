from requests_html import HTML, HTMLSession
import os
os.chdir('request-html_tutorial')

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render(sleep=10, timeout=10)


match = html.find('#footer', first=True)
print(match.html)
