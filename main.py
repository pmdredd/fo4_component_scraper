"""Fallout 4 component scraper

This small utility runs in the terminal and allows you to query information relating to crafting components
and junk items from Fallout 4.

Entering 'all' or 'a' returns all crafting components and their values.
Entering the name of a component e.g. wood returns that component and its ID.
Entering the name of a junk item returns that item and the components is produces when scrapped.
Entering 'q' or 'quit' exits the program.
"""

import fo4_component_scraper as fo4_sc
import requests
from bs4 import BeautifulSoup

HEADER_OFFSET = 7  # The vertical offset of the header columns, used to make the spacing consistent
BODY_OFFSET = 16  # The vertical offset between the body columns, used to make the spacing consistent
SOURCE_URL = "https://fallout.fandom.com/wiki/Fallout_4_junk_items"

page = requests.get(SOURCE_URL)
soup = BeautifulSoup(page.content, features="html.parser")

components = fo4_sc.get_components(soup)
junk_items = fo4_sc.get_junk_items(soup)


def main():
    print("Fallout 4 junk item and component tool")
    print("Enter 'all' or 'a' for all components, or enter a components name for a specific")
    print("Enter the name of a junk item to see its breakdown components")
    print("Enter 'q' or 'quit' to exit")
    query = input().lower()
    while True:
        if query == 'quit' or query == 'q':
            break
        elif query == 'all' or query == 'a':
            print(f'Component {HEADER_OFFSET * " "}: ID #')
            for name, item_id in components.items():
                # We need to get the length of the component name and take it away from the offset
                # in order to make the 'column' consistently spaced for every component
                print(f'{name} {(BODY_OFFSET - len(name)) * " "}: {item_id}')
            print("")
        else:
            if query in components:
                print(f'{query} (component)  |  ID: {components[query]}\n')
            elif query in junk_items:
                print(f'{query} (junk)  |  components: {", ".join(junk_items[query])}\n')
            else:
                print("This is not a valid component\n")

        query = input().lower()


if __name__ == "__main__":
    main()
