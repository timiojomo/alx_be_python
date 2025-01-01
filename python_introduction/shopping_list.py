shopping_list = ["apple", "bread", "milk", "cheese"]
item_found = False

while not item_found:
    item = input("Search for an item in your list (or 'q' to quit): ")
    if item.lower() == "q":
        break
    if item.lower() in shopping_list:
        item_found = True
        print(f"{item} is on the shopping list")
    else:
        print(f"{item} is not on the shopping list")