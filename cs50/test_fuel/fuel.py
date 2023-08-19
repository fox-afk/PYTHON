def main():
    fraction= input("Fraction: ")
    fraction_converted=converted(fraction)
    output= gauge(fraction_converted)
    print(output)
def converted(fraction):

    while True:
    
        try:
            numerator, denominator= fuel.split("/")
            new_numerator= int(numerator)
            new_denominator= int (denominator)
            f = new_numerator / new_denominator

            if f <= 1:
                p= int(f*100)
                return p
            else:
                fraction=input("Fraction: ")
                pass
        except(ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <=1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return str(percentage) +"%"

if __name__=="__main__":
    main()