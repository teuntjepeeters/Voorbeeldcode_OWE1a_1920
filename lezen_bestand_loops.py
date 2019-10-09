def lezen_bestand_while(bestand):
    """Lees het bestand met een while loop

    Input:
    bestand - str, naam bestand

    Output:
    -
    """
    open_bestand = open(bestand, "r")
    
    regel = open_bestand.readline()
    while regel != "":
        print(regel.strip())
        regel = open_bestand.readline()

    open_bestand.close()
    return


def lezen_bestand_for(bestand):
    """Lees het bestand met een for loop

    Input:
    bestand - str, naam bestand

    Output:
    -
    """
    open_bestand = open(bestand, "r")
    
    for regel in open_bestand:
        print(regel.strip())
        
    open_bestand.close()
    return


if __name__ == "__main__":
    bestand = "combination.fa"
    lezen_bestand_while(bestand)
    lezen_bestand_for(bestand)
