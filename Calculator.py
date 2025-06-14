import math

while True:
    operator = input("zadej operátor (+, -, *, /, %, min, max, pow, sqrt) nebo QUIT pro ukončení programu \n >")
#Ukončení programu

    if operator.lower() == "quit":
        print("Program se ukončí.")
        break

    elif operator.lower() == "sqrt":
        cislo = float(input("Číslo: "))
        vypocet = math.sqrt(cislo)
        print("")
        print(f"Tvoje číslo je: {vypocet}!")
        print("")
        continue

# Zapsání číslíček

    cislo_jenda = float(input("Číslo 1 :"))
    cislo_dva = float(input("Číslo 2 :"))

# Výpočty

    if operator == "+":
        vypocet = cislo_jenda + cislo_dva
        print("")
        print(f"Tvoje číslo je: {vypocet}!")  

    elif operator == "-":
        vypocet = cislo_jenda - cislo_dva
        print("")
        print(f"Tvoje číslo je: {vypocet}!")

    elif operator == "*":
        vypocet = cislo_jenda * cislo_dva
        print("")
        print(f"Tvoje číslo je: {vypocet}!")

    elif operator == "/":
        vypocet = cislo_jenda / cislo_dva
        print("")
        print(f"Tvoje číslo je: {vypocet}!")

    elif operator == "%":
        vypocet = cislo_jenda / cislo_dva
        print("")
        print(f"Tvoje číslo je: {vypocet}!")

    elif operator.lower() == "min": # Pro inteligentní jedince
        vypocet = min(cislo_jenda, cislo_dva)
        print("")
        print(f"Tvoje číslo je: {vypocet}!")


    elif operator.lower() == "max": # Pro inteligentní jedince
        vypocet = max(cislo_jenda, cislo_dva)
        print("")
        print(f"Tvoje číslo je: {vypocet}!")


    elif operator.lower() == "pow": # GOATED
        vypocet = pow(cislo_jenda, cislo_dva)
        print("")
        print(f"Tvoje číslo je: {vypocet}!")

# holy air ball

    else:
        print("Špatný imput ):")

    print("")