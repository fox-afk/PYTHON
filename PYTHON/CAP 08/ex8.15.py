L = [1,[2,3,4,[5,6,7]]]

for x in L:
    if type(x) is int:
        print(x)
    else:
        print("lista", end=[1])
        for z in x:
            print(f"{z}", end=[2])
        print()
