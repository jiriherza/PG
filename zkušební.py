def cislo_text(cislo):
    if cislo < 20:
        return seznam_jednotky[cislo]
    elif cislo < 100:
        desitky = cislo // 10
        jednotky = cislo % 10
        if jednotky == 0
            return seznam_desitky
        else:
            return seznam_destiky



seznam_destiky = {
    2: "dvacet", 3: "třicet", 4: "čtyřicet", 5: "padesát",
    6: "šedesát", 7: "sedmdesát", 8: "osmdesát", 9: "devadesát"
}









seznam_jednotky = {
    0: "nula", 1: "jedna", 2: "dva", 3: "tři", 4: "čtyři",
    5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět",
    10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct",
    14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct",
    18: "osmnáct", 19: "devatenáct"
}






if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)