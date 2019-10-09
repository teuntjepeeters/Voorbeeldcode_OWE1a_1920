def invoer():
    """Voer uw leeftijd in

    Return:
    getal - str, leeftijd
    """
    getal = input("Voer uw leeftijd in (jaren): ")
    return getal


def main():
    try:
        jaren = int(invoer())
        print("U bent "+ str(jaren) + " jaren oud")
        print("Dat is "+ str(jaren*12) + " maanden")
    except ValueError:
        print("U heeft geen leeftijd ingevoerd")
    

main()
