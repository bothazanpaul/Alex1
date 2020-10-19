def main():




def validator():
    state = True
    try:
        cnp = cnp_entry.get()
        if len(cnp) != 13:
            print("Lungime nevalida.")
        S, AA, LL, ZZ, JJ, NNN, C = (int(cnp[0:1]), int(cnp[1:3]), int(cnp[3:5]), int(cnp[5:7]),
                                     int(cnp[7:9]), int(cnp[9:12]), cnp[12:13]
                                     )
        cn = cnp_entry.get()[:-1]
        if not S in range(1, 10):
         print("Campul pentru sex nevalid.")
        if not LL in range(1, 13):
         print("Campul pentru luna nevalid.")
        if not ZZ in range(1, 32):
         print("Campul pentru ziua nevalid.")
        if not JJ in range(1, 53):
         print("Campul pentru judet nevalid.")
        suma = 0
        z = 0
        for x in "279146358279":
            suma = suma + int(x) * int(cn[z])
            z = z + 1
        rest = suma % 11
        if rest == 10:
            c = "1"
        else:
            c = str(rest)
        if not C == c:
            print("Cifra de control nevalida")
    except:
        state = False
    if state == True:
        info_valid_msgbox()
        AA, LL, ZZ, JJ, NNN, C = (cnp[1:3], cnp[3:5], cnp[5:7],
                                  cnp[7:9], cnp[9:12], cnp[12:13]
                                  )
        if S == 1:
            AA = "19" + AA
            text1 = "Persoana rezidenta in Romania de sex masculin nascuta in ziua: " + ZZ + " luna: " + LL + " anul: " + AA
        if S == 2:
            AA = "19" + AA
            text1 = "Persoana rezidenta in Romania de sex feminin nascuta in ziua: " + ZZ + " luna: " + LL + " anul: " + AA
        if S == 3:
            AA = "18" + AA
            text1 = "Persoana rezidenta in Romania de sex masculin nascuta in ziua: " + ZZ + " luna: " + LL + " anul: " + AA
        if S == 4:
            AA = "18" + AA
            text1 = "Persoana rezidenta in Romania de sex feminin nascuta in ziua: " + ZZ + " luna: " + LL + " anul: " + AA
        if S == 5:
            AA = "20" + AA
            text1 = "Persoana rezidenta in Romania de sex masculin nascuta in ziua: " + ZZ + " luna: " + LL + " anul: " + AA
        if S == 6:
            AA = "20" + AA
            text1 = "Persoana rezidenta in Romania de sex feminin nascuta in ziua: " + ZZ + " luna: " + LL + " anul: " + AA
        if S == 7:
            AA = "xx" + AA
            text1 = "Persoana straina rezidenta in Romania de sex masculin nascuta in ziua: " + ZZ + " luna: " + LL + " anul: " + AA
        if S == 8:
            AA = "xx" + AA
            text1 = "Persoana straina rezidenta in Romania de sex feminin nascuta in ziua: " + ZZ + " luna: " + LL + " anul: " + AA
        if S == 9:
            AA = "xx" + AA
            text1 = "Persoana straina de sex masculin/feminin nascuta in ziua: " + ZZ + " luna: " + LL + " anul: " + AA
        for text2 in judete.keys():
            if JJ == judete[text2]:
                break
        text = text1 + " in judetul: " + text2 + " cu numarul de evidenta: " + NNN + " si cifra de control: " + C + "."
    else:
        print("Nevalid")


def statement_callback(tag):
    global _statement
    _statement = tag


def sex_callback(tag):
    global _sex
    _sex = tag


def info_msgbox():
    print("About", info)


def error_msgbox():
    print("Error", "Setari nevalide!")


def info_valid_msgbox():
    print("Valid", "Felicitari, CNP-ul introdus/generat este valid!")


def warning_invalid_msgbox():
    print("Warning", "CNP-ul introdus/generat NU este valid.")


def county_list():
    global judete, judete_keys
    judete = {"Alba": "01", "Arad": "02", "Arges": "03", "Bacau": "04", "Bihor": "05",
              "Bistrita-Nasaud": "06", "Botosani": "07", "Brasov": "08", "Braila": "09", "Buzau": "10",
              "Caras-Severin": "11", "Cluj": "12", "Constanta": "13", "Covasna": "14", "Dambovita": "15",
              "Dolj": "16", "Galati": "17", "Gorj": "18", "Harghita": "19", "Hunedoara": "20",
              "Ialomita": "21", "Iasi": "22", "Ilfov": "23", "Maramures": "24", "Mehedinti": "25",
              "Mures": "26", "Neamt": "27", "Olt": "28", "Prahova": "29", "Satu Mare": "30",
              "Salaj": "31", "Sibiu": "32", "Suceava": "33", "Teleorman": "34", "Timis": "35",
              "Tulcea": "36", "Vaslui": "37", "Valcea": "38", "Vrancea": "39", "Bucuresti": "40",
              "Bucuresti S.1": "41", "Bucuresti S.2": "42", "Bucuresti S.3": "43", "Bucuresti S.4": "44",
              "Bucuresti S.5": "45",
              "Bucuresti S.6": "46", "Calarasi": "51", "Giurgiu": "52"
              }
    judete_keys = ()
    for x in judete.keys():
        judete_keys = judete_keys + (x,)
    judete_keys = sorted(judete_keys)



