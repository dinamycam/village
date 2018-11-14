'''
sample barebone scraper to search in arch linux packages and get some fields
'''
import requests
from bs4 import BeautifulSoup

arch_pack = requests.get('https://www.archlinux.org/packages/')

print(arch_pack.status_code)

package_soup = BeautifulSoup(arch_pack.content, 'html.parser')

package_soup.select('td')
package_table = package_soup.select('td')
print(package_table)

result = []
result_final = list()
i = 0
for package in package_table:
    if i % 7 == 2 or i % 7 == 3 or i % 7 == 5:
        result.append(package.get_text())
    if i % 7 == 5:
        result_final.append(result)
        result = list()
    i += 1
