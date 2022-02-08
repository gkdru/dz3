import math
def cv():
    a,b,c=int(input()),int(input()),int(input())
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return ("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        return("x = %.2f" % x)
    else:
        return("Корней нет")


def sredarif(lst):
    a, n = 0, 0
    for i in lst:
        a = (a * n + i) / (n + 1)
        n += 1
    return a
 
def abc():
    a,b=input('1цифра=  '),input("2цифра= ")
    try: a=int(a); b=int(b)
    except: a=str(a); b=str(b)
    return (a+b)