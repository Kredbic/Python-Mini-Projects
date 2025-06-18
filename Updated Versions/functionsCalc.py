import math


# Kalkulačka s funkcemi (lepší usage, readability)
# ---------------------
# Funkce:


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def devide(x, y):
    return x / y


def modulo(x, y):
    return x % y


def minimum(x, y):
    return min(x, y)


def maximum(x, y):
    return max(x, y)


def power(x, y):
    return pow(x, y)


def square_root(x):
    return math.sqrt(x)

# While loop
while True:
    operator = input(
        "zadej operátor (+, -, *, /, %, min, max, pow, sqrt) nebo QUIT pro ukončení programu \n >")

# Ukončení while loopu :)
    if operator.lower() == "quit":
        print("Program se ukončuje!")
        break

# Ify, výpočet samotného příkladu. Podle toho kolik je potřeba inputů operátor se na ně zeptá a následně vypočítá.
    elif operator.lower() == "+":
        x = int(input("X = "))
        print("+")
        y = int(input("Y = "))

        print(f"\nTvůj výsledek je: {add(x, y)}! \n")

    elif operator.lower() == "-":
        x = int(input("X = "))
        print("-")
        y = int(input("X = "))

        print(f"\nTvůj výsledek je: {subtract(x, y)}! \n")

    elif operator.lower() == "*":
        x = int(input("X = "))
        print("*")
        y = int(input("X = "))

        print(f"\nTvůj výsledek je: {multiply(x, y)}! \n")

    elif operator.lower() == "/":
        x = int(input("X = "))
        print("/")
        y = int(input("X = "))

        print(f"\nTvůj výsledek je: {devide(x, y)}! \n")

    elif operator.lower() == "%":
        x = int(input("X = "))
        print("%")
        y = int(input("X = "))

        print(f"\nTvůj výsledek je: {modulo(x, y)}! \n")

    elif operator.lower() == "min":
        x = int(input("X = "))
        y = int(input("X = "))

        print(f"\nTvůj výsledek je: {minimum(x, y)}! \n")

    elif operator.lower() == "max":
        x = int(input("X = "))
        y = int(input("X = "))

        print(f"\nTvůj výsledek je: {maximum(x, y)}! \n")

    elif operator.lower() == "pow":
        x = int(input("X = "))
        print("pow")
        y = int(input("X = "))

        print(f"\nTvůj výsledek je: {power(x, y)}! \n")

    elif operator.lower() == "sqrt":
        x = int(input("X = "))

        print(f"\nTvůj výsledek je: {square_root(x)}! \n")

    # Špatný input? :O
    else:
        print("Špatný input! :()")
