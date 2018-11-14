import requests
import bs4

MAKTAB_URL = 'https://maktabkhooneh.org'
maktab = requests.get(MAKTAB_URL+'/courses/')

maktab_soup = bs4.BeautifulSoup(maktab.content, 'html.parser')

courses = maktab_soup.select('.pic-contianer')

course_links = [MAKTAB_URL+course.get('href') for course in courses]

first_course = requests.get(course_links[0])
first_soup = bs4.BeautifulSoup(first_course.content, 'lxml')
# exercise: get demo video link :)
