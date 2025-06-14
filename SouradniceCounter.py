# Výpočet souŕadnic. 
# How to use: 
# x - budu počítat pouze Xové souřadnice
# y - budu počítat pouze Yové souřadnice
# xy, yx - budu počítat X, Y souřadnice
# quit, vypne program.
print("Pojďme vypočítat souřadnice")
souradnice_x = int(input("Jaké jsou tvoje X souřadnice: \n >"))
souradnice_y = int(input("Jaké jsou tvoje Y souřadnice \n >"))
print(f"Tvoje souřadnice jsou {souradnice_x} z {souradnice_y}")
print("") # Mezera
while True:
    co_pocitat = input("Jaké souřadnice chceš vypočítat? \n >")
    # Ukončení programu ):
    if co_pocitat.lower() == "quit":
        print("Program ukončen.")
        break # Ukončí program

    # Xová souřadnice
    elif co_pocitat.lower() == "x":
        plusminus = input("Posouváš se do: \n plusu - 1 mínusu - 2 \n >")
        kolik_x = int(input("O kolik X souřadnic se chceš posunout? \n >"))
        if plusminus == "1":
            vypocet = souradnice_x + kolik_x
            print(f"Vypočítané souřadnice jsou {vypocet} z {souradnice_y}")
        elif plusminus == "2":
            vypocet = souradnice_x - kolik_x
            print(f"Vypočítané souřadnice jsou {vypocet} z {souradnice_y}")
        else:
            print("Wrong input ):")

    # Yová souřadnice 
    elif co_pocitat.lower() == "y":
        plusminus = input("Posouváš se do: \n plusu - 1 mínusu - 2 \n >")
        kolik_y = int(input("O kolik Y souřadnic se chceš posunout? \n >"))
        if plusminus == "1":
            vypocet = souradnice_y + kolik_y
            print(f"Vypočítané souřadnice jsou {souradnice_x} z {vypocet}")
        elif plusminus == "2":
            vypocet = souradnice_y - kolik_y
            print(f"Vypočítané souřadnice jsou {souradnice_x} z {vypocet}")
        else:
            print("Wrong input ):")


    # XYová souřadnice
    elif co_pocitat.lower() in ("xy", "yx"):
        print(f"Budeme počítat {co_pocitat.upper()} souřadnice")

        #Xová
        vypocetx = 0
        plusminusx = input("X posouváš  do: \n plusu - 1 mínusu - 2 \n >")
        kolik_x = int(input("O kolik X souřadnic se chceš posunout? \n >"))
        if plusminusx == "1":
            vypocetx = souradnice_x + kolik_x
        elif plusminusx == "2":
            vypocetx = souradnice_x - kolik_x
        else:
            print("Wrong input ):")

        #Yová
        vypocety = 0
        plusminusy = input("Y posouváš  do: \n plusu - 1 mínusu - 2 \n >")
        kolik_y = int(input("O kolik Y souřadnic se chceš posunout? \n >"))
        if plusminusy == "1":
            vypocety = souradnice_y + kolik_y
        elif plusminusy == "2":
            vypocety = souradnice_y - kolik_y
        else:
            print("Wrong input ):")

        print(f"Vypočítané souřadnice jsou {vypocetx} z {vypocety}")

    # Holy fkn air ball
    else:
        print("Špatný input!!!")
