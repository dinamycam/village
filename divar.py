import requests
import bs4
import re

DIVAR_BASE_URL = 'https://divar.ir'
# divar shiraz

divar_shz = requests.get(
    DIVAR_BASE_URL + '/shiraz/%D8%B4%DB%8C%D8%B1%D8%A7%D8%B2/browse/')
divar_soup = bs4.BeautifulSoup(divar_shz.content, 'lxml')

results = divar_soup.select('.post-card')

i = 0
links_to_product = list()
while i < len(results):
    links_to_product.append(results[i].select(
        '.post-card-link')[0].get('href'))
    i += 1

for link_to_product in links_to_product:
    # print(link_to_product)
    product = requests.get(DIVAR_BASE_URL+link_to_product)
    patterns = link_to_product.split('/')
    # print(patterns)
    # pid = pattern.match(link_to_product)
    # print(pid)
    # get phone number
    phone_number = requests.get(
        'https://api.divar.ir/v5/posts/{}/contact/'.format(patterns[-1]))
    print(phone_number.json()['widgets']['contact']['phone'])
