import requests
import pprint
from bs4 import BeautifulSoup, element

source = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&txtLocation=&cboWorkExp1=-1').text

soup = BeautifulSoup(source, 'lxml')

jobs_ = soup.find_all('div', class_='srp-job-bx')

name = []
c_name = []
loc = []
skilss = []
compact = {}

for job in jobs_:
    title = job.find('h3').text
    name.append(title)

    c_name.append(job.find('h4').text)
    loc.append(job.find('div', class_="srp-loc").text)
    skilss.append(job.find('div', class_='srp-keyskills').text)


compact['names'] = name
compact['company'] = c_name
compact['location'] = loc
compact['skills'] = skilss

print(compact['company'])