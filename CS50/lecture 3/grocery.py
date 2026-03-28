grocery_items = {}

while True:

    try:

        item = input().upper()

        if item not in grocery_items:

            grocery_items[item] = 1
        else:

            grocery_items[item] +=1

    except EOFError:

        break

sorted_grocery = dict(sorted(grocery_items.items()))


for key, value in sorted_grocery.items():

    print(f"{value} {key}")

