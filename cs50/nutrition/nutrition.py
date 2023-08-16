fruits={
    "apple":130,
    "avocado":50,
    "sweet cherries":100,
}

fruit_asked=input("item: ")
for key in fruits:
    if key == fruit_asked:
        print("calories:", fruits[key])