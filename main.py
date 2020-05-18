import fo4_component_scraper as fo4_sc

HEADER_OFFSET = 7  # The vertical offset of the header columns
BODY_OFFSET = 16  # The vertical offset between the body columns

components = fo4_sc.get_components()
junk_items = fo4_sc.get_junk_items()


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
