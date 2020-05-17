from FO4ComponentScraper import FO4ComponentScraper


def main():
    sc = FO4ComponentScraper()

    print("Which crafting component(s) do you want to get the IDs for?")
    print("Enter 'all' for all components, or enter a components name for specific components")
    print("Enter 'q' or 'quit' to exit")
    query = input().lower()
    while True:
        if query == 'q' or query == 'quit':
            break
        elif query == 'all':
            components = sc.all_components()
            print(f'Component {7 * " "}: ID #')
            for name, item_id in components.items():
                print(f'{name} {(16 - len(name)) * " "}: {item_id}')
            print("")
        else:
            if query not in sc.all_components():
                print("This is not a valid component")
            else:
                component = sc.get_component(query)
                print(f'{query} : {component[query]}')
        query = input().lower()


if __name__ == "__main__":
    main()
