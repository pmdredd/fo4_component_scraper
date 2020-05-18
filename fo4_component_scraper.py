# The scraper that gets item data from the FO4 wiki
import requests
from bs4 import BeautifulSoup

SOURCE_URL = "https://fallout.fandom.com/wiki/Fallout_4_junk_items"
page = requests.get(SOURCE_URL)
soup = BeautifulSoup(page.content, features="html.parser")


def get_components():
    # Get the first table on the page, which contains the components and their IDs
    components_table = soup.find('table', class_='va-table')
    # Get all the rows from the table, as a list, excluding first 2 rows as they are headers
    component_rows = components_table.find_all('tr')[2:]

    # Loop through each row and extract the component name and base ID
    components = {}
    for row in component_rows:
        name = row.a.text.lower()
        item_base_id = row.find('span', class_='va-formid').text.upper()
        components[name] = item_base_id
    return components


def get_junk_items():
    # The third table on the page contains all junk items and their constituent components
    junk_table = soup.find_all('table', class_='va-table')[2]
    # Exclude the first row as it is a header
    junk_rows = junk_table.find_all('tr')[1:]

    junk_items = {}
    for row in junk_rows:
        cols = row.find_all('td')
        # The first column is holds a link with the name of the junk item
        name = cols[0].a.text.lower()
        # The 6th column contains links with the names of the junk item's components, which we want as a list
        components = [component.text.lower() for component in cols[5].find_all('a')]

        junk_items[name] = components
    return junk_items
