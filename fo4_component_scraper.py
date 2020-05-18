# The scraper that gets item data from the FO4 wiki
import requests
from bs4 import BeautifulSoup


SOURCE_URL: str = "https://fallout.fandom.com/wiki/Fallout_4_junk_items"
page = requests.get(SOURCE_URL)
soup = BeautifulSoup(page.content, features="html.parser")


def get_components():
    # Get the first table on the page (which contains the components and their IDs)
    components_table = soup.find('table', class_='va-table')
    # Get all the rows from the table, as a list
    components_rows = components_table.find_all('tr')

    # Loop through each row and extract the component name and base ID,
    # excluding first 2 rows as they are headers
    components = {}
    for component in components_rows[2:]:
        name = component.a.text.lower()
        item_base_id = component.find('span', class_='va-formid').text.upper()
        components[name] = item_base_id
    return components
