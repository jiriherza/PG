def bin_to_dec(binarni_cislo):
    s = str(binarni_cislo)        # pracujeme se stringem
    exponent = 0
    vysledek = 0

    # jdeme zprava doleva
    for cifra in reversed(s):
        bit = int(cifra)
        vysledek += bit * (2 ** exponent)
        exponent += 1

    return vysledek 

        
def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128