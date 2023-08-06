import sys
print(f"numero de parametros:{len(sys.argv)}")
for n , p in enumerate(sys.argv):
    print(f"parametro {n} = {p}")