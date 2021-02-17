import sys
from functions import arithmetics
from functions import geo

# negativ Beispiele: könnte Konflikt mit anderen Funtkionen geben:
# from functions import summe
# from functions.arithmetics import *

# Konstanten in Python werden groß geschreiben. Konvention!
OPERATIONS = {
    '+': arithmetics.summe,
    '*': arithmetics.multiplikation,
    '-': arithmetics.substraktion,
    '/': arithmetics.division,
    '**': arithmetics.hoch,
    'dist': geo.distance
}


def parse_user_input(user_input):
    """Zerlege den user-input in seine Bestandteile
    Beispiel unser-input: + 3 43
    Args:
        user-input(str): die Usereingabe
    Returns:
        tuple: (operator, operand, operand)
    """
    user_input = user_input.split()  # ['+', '3', '43']
    operator = user_input.pop(0)
    a, b = float(user_input[0]), float(user_input[1])

    return operator, a, b


def controller(operator,a, b):
    op = OPERATIONS.get(operator)
    if op:
        return op(a, b)
    raise NotImplementedError("Diese Operation ist nicht implementiert")


def main():
    """ Hauptprogramm. Hier wird der User-Input verarbeitet. Abruch mit _quit"""
    while True:
        # + 3 43
        user_input = input("Bitte Berechnung eingeben (Operator und 2 Operanden): ")

        if user_input in ["_quit", "_exit"]:
            print("Danke. Programm beendet")
            break

        operator, a, b = parse_user_input(user_input)
        result = controller(operator, a, b)
        print("Ergebnis: ", result)


if __name__ == '__main__':
    main()
