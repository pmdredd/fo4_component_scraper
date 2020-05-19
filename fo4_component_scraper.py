"""Fallout 4 component scraper

This module contains functions that take the scraped data (as a BS4 object)
and return the relevant item/component data as a dictionary.
"""


def get_components(soup):
    """Get the name and ID of every component"""

    # The first table on the page contains the components and their IDs
    components_table = soup.find('table', class_='va-table')
    # Exclude the first 2 rows as they are headers
    component_rows = components_table.find_all('tr')[2:]

    components = {}
    for row in component_rows:
        name = row.a.text.lower()
        component_base_id = row.find('span', class_='va-formid').text.upper()
        components[name] = component_base_id
    return components


def get_junk_items(soup):
    """Get the name and constituent component(s) of every junk item"""

    # The third table on the page contains all junk items and their constituent components
    junk_table = soup.find_all('table', class_='va-table')[2]
    # Exclude the first row as it is a header
    junk_rows = junk_table.find_all('tr')[1:]

    junk_items = {}
    for row in junk_rows:
        cols = row.find_all('td')
        # The first column holds a link with the name of the junk item
        name = cols[0].a.text.lower()
        # The sixth column contains links with the names of the junk item's components
        components = [component.text.lower() for component in cols[5].find_all('a')]

        junk_items[name] = components
    return junk_items
