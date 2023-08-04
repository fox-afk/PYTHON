L = [1,[2,3,4,[5,6,7]]]
for x in L:
    if type (x) is str:
        print(x)
    else:
        print("lista:",end="")
        for z in L:
            print(f"{z}", end="")
        print()