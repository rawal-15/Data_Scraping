

import requests

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)
#
# print(page.text)
import requests
from bs4 import BeautifulSoup
from DataScraping2 import save_to_database

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
# print(results.prettify())
job_elements = results.find_all("div", class_="card-content")
# for job_element in job_elements:
#     print(job_element, end="\n"*2)
for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(f"Insert in db : job_name = {title_element.text}, company_name = {str(company_element.text).replace(',',' ')}, location = {str(location_element.text).replace(' ', '').replace(',','')}")
        save_to_database(title_element.text, str(company_element.text).replace(',',' '), str(location_element.text).replace(' ', '').replace(',',''))




