import math
def quad(val1, val2, val3):
    delta = (val2 * val2) - 4 * val1 * val3
    if val1 ==0:
        print("Equation is not Quadratic")
        return
        
    elif delta > 0:
        r1 =(-val2 + math.sqrt(delta)) /2 * val1
        r2 = (-val2 - math.sqrt(delta)) /2 * val1

        print("square roots of equation a^2 + b *r + c :- ", r1, r2)

    else:
        print("Roots are Complex")

if __name__ == '__main__':
    a = int(input("Enter value for variable a: "))
    b = int(input("Enter value for variable b: "))
    c = int(input("Enter value for variable c: "))

    quad(a,b,c)