# unser erstes Modul

def summe(a, b):
    return a + b


def multiplikation(a, b):
    return a * b


def substraktion(a , b):
    return a - b


def division(a, b):
    if b != 0:
        result = a / b
    else:
        result = 0
    return result


def hoch(a, b):
    return a ** b


if __name__ == '__main__':
    print("Test")
    print(hoch(5, 5))