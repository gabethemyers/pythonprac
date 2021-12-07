from requests_html import HTML, HTMLSession

# with open('simple.html') as html_file:
#     source = html_file.read()
#     html = HTML(html=source)

session = HTMLSession()
r = session.get('https://coreyms.com/')

articles = r.html.find('article')

for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    description = article.find('.entry-content p', first=True).text
    try:
        vid_src = article.find('iframe', first=True).attrs['src']
    except:
        pass
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(headline)
    print(description)
    print(yt_link)

# print(headline)
# print(description)
