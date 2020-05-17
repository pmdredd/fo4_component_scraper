# The scraper that gets item data from the FO4 wiki
import requests
from bs4 import BeautifulSoup


class FO4ComponentScraper:
    SOURCE_URL = "https://fallout.fandom.com/wiki/Fallout_4_junk_items"
    scraped = False
    soup = None
    components = {}

    def __init__(self):
        self.__scrape_page()
        self.__get_all_components()

    def __scrape_page(self):
        if self.scraped:  # Check if we have already scraped this page
            pass
        else:
            page = requests.get(self.SOURCE_URL)
            self.soup = BeautifulSoup(page.content, features="html.parser")
            self.scraped = True

    def __get_all_components(self):
        # Get the first table on the pages (which contains the components and their IDs)
        components_table = self.soup.find('table', class_='va-table')
        # Get all the rows from the table in a list
        components_rows = components_table.find_all('tr')

        # Loop through each table row and extract the component name and base ID,
        # excluding first 2 rows as they are headers
        for component in components_rows[2:]:
            name = component.a.text.lower()
            item_base_id = component.find('span', class_='va-formid').text.upper()
            self.components[name] = item_base_id

        return self.components

    def all_components(self):
        return self.components

    def get_component(self, name):
        name = name.lower()
        return {name: self.components[name]}
