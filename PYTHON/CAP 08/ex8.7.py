3 # Programa de calcule o maior divisor comun  entre dois  numeros a e b, em que a >b

def mdc(a,b):
    if a >b or b==0:
        return a
    else:
        return mdc(b,a%b)