import requests
from bs4 import BeautifulSoup as bs
from html5print import HTMLBeautifier
import lxml
import webbrowser


reqses = requests.session()

google_main = reqses.get(url='http://google.com')

google_main.headers

print(HTMLBeautifier.beautify(google_main.content, 'lxml'))

soup = bs(google_main.content, 'html.parser')
print(soup.prettify())
