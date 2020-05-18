import fo4_component_scraper as fo4_sc

HEADER_OFFSET = 7  # The vertical offset of the header columns
BODY_OFFSET = 16  # The vertical offset between the body columns
components = fo4_sc.get_components()


def main():
    print("Which crafting component(s) do you want to get the IDs for?")
    print("Enter 'all' or 'a' for all components, or enter a components name for specific components")
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
            if query not in components:
                print("This is not a valid component\n")
            else:
                print(f'{query} : {components[query]}\n')
        query = input().lower()


if __name__ == "__main__":
    main()
