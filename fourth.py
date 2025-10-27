


def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    
    pozice = figurka["pozice"]
    cil_radek, cil_sloupec = cilova_pozice


    if not cil_radek >= 1 and cil_radek <= 8 and cil_sloupec >= 1 and cil_sloupec <= 8:
        return False

    if pozice == cilova_pozice:
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    typ = figurka["typ"]

    if typ == "pěšec":
        return je_tah_mozny_pesec(pozice, cilova_pozice)
    elif typ == "jezdec":
        return je_tah_mozny_jezdec(pozice, cilova_pozice)
    elif typ == "věž":
        return je_tah_mozny_vez(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "střelec":
        return je_tah_mozny_strelec(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "dáma":
        return je_tah_mozny_dama(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "král":
        return je_tah_mozny_kral(pozice, cilova_pozice)
    else:
        return False



def je_tah_mozny_pesec(pozice, cilova_pozice):
    radek, sloupec = pozice
    cil_radek, cil_sloupec = cilova_pozice

    if cil_sloupec != sloupec:
        return False

    if cil_radek == radek + 1:
        return True
    return False


def je_tah_mozny_jezdec(pozice, cilova_pozice):
    radek, sloupec = pozice
    cil_radek, cil_sloupec = cilova_pozice

    rozdil_radku = abs(radek - cil_radek)
    rozdil_sloupcu = abs(sloupec - cil_sloupec)

    if (rozdil_radku, rozdil_sloupcu) in [(2,1), (1,2)]:
        return True
    else:
        return False


def je_tah_mozny_vez(pozice, cilova_pozice, obsazene_pozice):
    radek, sloupec = pozice
    cil_radek, cil_sloupec = cilova_pozice

    if radek != cil_radek and sloupec != cil_sloupec:
        return False

    if radek == cil_radek:
        start = min(sloupec, cil_sloupec)
        end = max(sloupec, cil_sloupec)
        for i in range(start + 1, end):  
            if (radek, i) in obsazene_pozice:
                return False
        return True
    elif sloupec == cil_sloupec:   
        start = min(radek, cil_radek)
        end = max(radek, cil_radek)
        for ii in range(start + 1, end):
            if (ii, sloupec) in obsazene_pozice:
                return False
        return True
    else:
        return False


def je_tah_mozny_strelec(pozice, cilova_pozice, obsazene_pozice):
    radek, sloupec = pozice
    cil_radek, cil_sloupec = cilova_pozice

    if abs(cil_radek - radek) != abs(cil_sloupec - sloupec):
        return False
    
    
    if cil_radek > radek:
        krok_radek = 1
    else:
        krok_radek = -1
    if cil_sloupec > sloupec:
        krok_sloupec = 1
    else:
        krok_sloupec = -1

    pohyb_radek = radek + krok_radek
    pohyb_sloupec = sloupec + krok_sloupec
    while (pohyb_radek, pohyb_sloupec) != (cil_radek, cil_sloupec):
        if (pohyb_radek, pohyb_sloupec) in obsazene_pozice:
            return False
        pohyb_radek += krok_radek
        pohyb_sloupec += krok_sloupec

    return True


def je_tah_mozny_dama(pozice, cilova_pozice, obsazene_pozice):
    return je_tah_mozny_vez(pozice, cilova_pozice, obsazene_pozice) or je_tah_mozny_strelec(pozice, cilova_pozice, obsazene_pozice)


def je_tah_mozny_kral(pozice, cilova_pozice):
    radek, sloupec = pozice
    cil_radek, cil_sloupec = cilova_pozice
    if abs(cil_radek - radek) <= 1 and abs(cil_sloupec - sloupec) <= 1:
        return True




if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True    
    
