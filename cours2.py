
def main():
    # première note
    note1 = int(input("entré la première note"))
    # deuxieme note
    note2 = int(input("entré la deuxieme note"))
    #troisieme note
    note3 = int(input("entré la troisieme note"))
    # calcule de la moyenne
    resultat = (note1 + note2 + note3) / 3
    # afffiche le résultat
    print ("le résultat est" + str(resultat))

if __name__ == '__main__':
    main()