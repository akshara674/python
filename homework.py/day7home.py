
inventory = []


def add_item(item):
    """Adds a single item to the inventory list."""
    inventory.append(item)


def count_items(items):
    """Recursively counts the number of items in the list."""
    
    if not items:
        return 0
    
    return 1 + count_items(items[1:])


show_item = lambda item: print(f"Item in Stock: {item}")


def main():
    
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    
    for item in inventory:
        show_item(item)

    
    total = count_items(inventory)
    print(f"\nTotal number of items in stock: {total}")


main()
