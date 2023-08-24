s = "AABBEFAATT"
p = 0 
while(p>-1):
    p=s.find("BE",p)
    if p >=0:
        print(f"posição:{p}")
        p+=1