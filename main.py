from FO4ComponentScraper import FO4ComponentScraper

sc = FO4ComponentScraper()
HEADER_OFFSET = 7  # The vertical offset of the header columns
BODY_OFFSET = 16  # The vertical offset between the body columns


def main():
    print("Which crafting component(s) do you want to get the IDs for?")
    print("Enter 'all' for all components, or enter a components name for specific components")
    print("Enter 'q' or 'quit' to exit")
    query = input().lower()
    while True:
        if query == 'q' or query == 'quit':
            break
        elif query == 'all':
            print(f'Component {HEADER_OFFSET * " "}: ID #')
            for name, item_id in sc.components.items():
                print(f'{name} {(BODY_OFFSET - len(name)) * " "}: {item_id}')
            print("")
        else:
            if query not in sc.components:
                print("This is not a valid component\n")
            else:
                print(f'{query} : {sc.components[query]}\n')
        query = input().lower()


if __name__ == "__main__":
    main()
