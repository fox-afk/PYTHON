names=[]
p=inflect.engine()
while True:
    try:
        name=input("name: ")
        names.append(name)
    except EOFError:
        print()
        break
output=p.join(names)
print("adieu,adieu,to"+ output)