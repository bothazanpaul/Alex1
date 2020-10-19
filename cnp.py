# # from datetime import date
# #
# # S = {
# #     "01/01/1900 31/12/1999": {"M": "1", "F": "2"},
# #     "01/01/1800 31/12/1899": {"M": "3", "F": "4"},
# #     "01/01/2000 31/12/2099": {"M": "5", "F": "6"},
# #     "Rezident": {"M": "7", "F": "8"},
# # }
# #
# # JJ = {
# #     "Alba": "01",
# #     "Arad": "02",
# #     "Arges": "03",
# #     "Bacau": "04",
# #     "Bihor": "05",
# #     "Bistrita-Nasaud": "06",
# #     "Botosani": "07",
# #     "Brasov": "08",
# #     "Braila": "09",
# #     "Buzau": "10",
# #     "Caras-Severin": "11",
# #     "Cluj": "12",
# #     "Constanta": "13",
# #     "Covansa": "14",
# #     "Dambovita": "15",
# #     "Dolj": "16",
# #     "Galati": "17",
# #     "Gorj": "18",
# #     "Harghita": "19",
# #     "Hunedoara": "20",
# #     "Ialomita": "21",
# #     "Iasi": "22",
# #     "Ilfov": "23",
# #     "Maramures": "24",
# #     "Mehedinti": "25",
# #     "Mures": "26",
# #     "Neamt": "27",
# #     "Olt": "28",
# #     "Prahova": "29",
# #     "Satu Mare": "30",
# #     "Salaj": "31",
# #     "Sibiu": "32",
# #     "Suceava": "33",
# #     "Teleorman": "34",
# #     "Timis": "35",
# #     "Tulcea": "36",
# #     "Vaslui": "37",
# #     "Valcea": "38",
# #     "Vrancea": "39",
# #     "Bucuresti": "40",
# #     "Bucuresti Sectorul 1": "41",
# #     "Bucuresti Sectorul 2": "42",
# #     "Bucuresti Sectorul 3": "43",
# #     "Bucuresti Sectorul 4": "44",
# #     "Bucuresti Sectorul 5": "45",
# #     "Bucuresti Sectorul 6": "46",
# #     "Calarasi": "51",
# #     "Giurgiu": "52"
# # }
# # for x in cnp:
# #     x = int(x)
# #     cnp_arr.append(x)
# # val_cnp = [2,7,9,1,4,6,3,5,8,2,7,9]
# # y = 0
# # cnp_sum = 0
# # while y < len(val_cnp):
# #     cnp_sum += cnp_arr[y] * val_cnp[y]
# #     y += 1
# # c = cnp_sum % 11
# # if c == 10 :
# #     c = 1
# # if c == cnp_arr[len(cnp_arr)-1] :
# #     print('CNP-ul dvs este valid!')
# # else:
# #     print('CNP invalid')
#
# import datetime
#
# from stdnum.util import clean
#
#
# def compact(number):
#     """Convert the number to the minimal representation. This strips the
#     number of any valid separators and removes surrounding whitespace."""
#     return clean(number, ' -').upper().strip()
#
#
# def calc_check_digit(number):
#     """Calculate the check digit for personal codes. The number passed
#     should not have the check digit included."""
#     # note that this algorithm has not been confirmed by an independent source
#     weights = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
#     check = sum(weights[i] * int(n) for i, n in enumerate(number)) % 11
#     return '1' if check == 10 else str(check)
#
#
# def get_birth_date(number):
#     """Split the date parts from the number and return the birth date."""
#     centuries = {
#         '1': 1900, '2': 1900, '3': 1800, '4': 1800, '5': 2000, '6': 2000,
#     }  # we assume 1900 for the others in order to try to construct a date
#     year = int(number[1:3]) + centuries.get(number[0], 1900)
#     month = int(number[3:5])
#     day = int(number[5:7])
#     return datetime.date(year, month, day)
#
#
# def is_valid(number):
#     """Checks to see if the number provided is a valid VAT number. This checks
#     the length, formatting and check digit."""
#     try:
#         number = compact(number)
#     except:
#         return False
#     if len(number) != 13 or not number.isdigit():
#         return False
#     # first digit should be a known one (9=foreigner)
#     if number[0] not in '1234569':
#         return False
#     # check if birth date is valid
#     try:
#         birth_date = get_birth_date(number)
#         # TODO: check that the birth date is not in the future
#     except ValueError, e:
#         return False
#     # number[7:9] is the county, we ignore it for now, just check last digit
#     return calc_check_digit(number[:-1]) == number[-1]

numar_control = None
cnp1 = str(input('Introduceti Codul Numeric Personal:\t'))
cnp = [int(i) for i in str(cnp1)]
cod = [int(i) for i in str(cnp1)]
gresit = 'CNP-ul introdus este GRESIT'
control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
an = None
an1 = cnp1[1:3]
if int(an1) in range(25):
    an = '20'+an1
else:
    an = '19'+an1
luna = cnp1[3:5]
zi = cnp1[5:7]
data = an+'-'+luna+'-'+zi
print(' Data nasterii tale este:\t', data)
format = '%Y-%m-%d'
if cnp1.isdigit() == False or len(cnp) != 13 or int(cnp[0]) < 1 or int(cnp[0]) > 9:
    print(gresit)
elif int(cnp[7]) not in range(0, 5):
    print(gresit)
elif int(cnp[7]) == 4 and int(cnp[8]) not in range(0, 6):
    print(gresit)
elif int(cnp[7]) == 5 and int(cnp[8]) not in range(1, 2):
    print(gresit)
else:
    cod.pop()
    final_cod = [cod[i] * control[i] for i in range(len(cod))]
    adunare = sum(final_cod)
    rezultat = adunare / 11
    #rezultat = round(rezultat, 2)
    rest = str(rezultat)
    numar_control = rest[1:]
    k = float(numar_control)
    # def round_up(n, decimals=0):
    #     multiplier = 10 ** decimals
    # numar_control2 = round_up(k, 1)
    # numar_control_3_3 = str(numar_control2)
    # cifra_control_ok = numar_control_3_3[2:]
#     def _calculate_cifra_control(cls, cnp):
#         cnp_sum = 0
#         for x in range(12):
#             cnp_sum =+ cnp[x] * cls.control[x]
#         rest = cnp_sum % 11
#         if rest == 10:
#             return 1
#         return rest
#     print('Cifra de control este: ', rest)
#     raspunsul = None
# if rest == cnp1[12]:
#     print('CNP-ul este VALID')
# else:
#     print('CNP-ul NU este valid!')

def cnp():
    global cnp_list
    if cnp()==True:
        cnp_list = []
        for NNN in range(1, 999):
            NNN = str(NNN)
            if len(NNN) == 1:
                NNN = "00" + NNN
            elif len(NNN) == 2:
                NNN = "0" + NNN
            cn = S+AA+LL+ZZ+JJ+NNN
            suma = 0
            z = 0
            for x in "279146358279":
                suma = suma+int(x) * int(cn[z])
                z = z+1
            rest = suma%11
            if rest == 10:
                C = "1"
            else:
                C = str(rest)
            cnp = S+AA+LL+ZZ+JJ+NNN+C
            cnp_list.append(cnp)
        generate_list.configure(text_state="normal")
        generate_list.clear()