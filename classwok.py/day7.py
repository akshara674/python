
grocery_list = ["milk", "bread", "eggs"]


def add_item(item):
    """Adds a given item to the grocery list."""
    grocery_list.append(item)


def remove_last_item():
    """Removes the last item from the grocery list, if it exists."""
    if grocery_list:
        grocery_list.pop()
    else:
        print("The grocery list is already empty!")


show_item = lambda item: print(f"Item: {item}")


def count_characters(items):
    """Recursively counts total characters in all item names."""
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])


def main():
    
    print("Initial Grocery List:")
    for item in grocery_list:
        show_item(item)

    
    add_item("butter")
    print("\nAfter adding 'butter':")
    for item in grocery_list:
        show_item(item)

    
    remove_last_item()
    print("\nAfter removing the last item:")
    for item in grocery_list:
        show_item(item)

    
    total_chars = count_characters(grocery_list)
    print(f"\nTotal number of characters in all item names: {total_chars}")


main()
