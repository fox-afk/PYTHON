fruits={
    "apple":130,
    "avocado":50,
    "sweet cherries":100,
}

fruit_asked=input("Item: ")
for key in fruits:
    if key == fruit_asked.lower():
        print("calories:", fruits[key])