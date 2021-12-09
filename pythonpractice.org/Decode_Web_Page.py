"""prompt: Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the
New York Times homepage. """

# importing requests to get html from nytimes
import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

# creating my soup
soup = BeautifulSoup(r_html, 'html.parser')

# for every word that soup finds i just print it
for word in soup.find_all('h3', {'class': re.compile(r'e1lsht870')}):
    print(word.get_text())
# notes: this is problem is outdated, it was make in 2014. Before, each story heading on nytimes had a class which
# was 'story-heading' now it is just random stuff but i noticed all of them ended in e1lsht870 so I used regex to see
# if that was at the end of a string.
