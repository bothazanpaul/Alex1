# coding=utf-8
"""
This file contains util things for this module.
"""

SEX = {
    None: "STRAIN NEREZIDENT",
    True: "MASCULIN",
    False: "FEMININ"
}

S = {
    1: {"sex": SEX[True], "start_year": 1900, "end_year": 1999, "century": 20},
    3: {"sex": SEX[True], "start_year": 1800, "end_year": 1899, "century": 19},
    5: {"sex": SEX[True], "start_year": 2000, "end_year": 2099, "century": 21},
    7: {"sex": SEX[True], "start_year": 1900, "end_year": 1999, "century": 20},
    2: {"sex": SEX[False], "start_year": 1900, "end_year": 1999, "century": 20},
    4: {"sex": SEX[False], "start_year": 1800, "end_year": 1899, "century": 19},
    6: {"sex": SEX[False], "start_year": 2000, "end_year": 2099, "century": 21},
    8: {"sex": SEX[False], "start_year": 1900, "end_year": 1999, "century": 20},
    9: {"sex": SEX[None], "start_year": 1900, "end_year": 1999, "century": 20}
}

JJ = {
    1: "Alba",
    2: "Arad",
    3: "Arges",
    4: "Bacau",
    5: "Bihor",
    6: "Bistrita-Nasaud",
    7: "Botosani",
    8: "Brasov",
    9: "Braila",
    10: "Buzau",
    11: "Caras-Severin",
    12: "Cluj",
    13: "Constanta",
    14: "Covasna",
    15: "Dambovita",
    16: "Dolj",
    17: "Galati",
    18: "Gorj",
    19: "Harghita",
    20: "Hunedoara",
    21: "Ialomita",
    22: "Iasi",
    23: "Ilfov",
    24: "Maramures",
    25: "Mehedinti",
    26: "Mures",
    27: "Neamt",
    28: "Olt",
    29: "Prahova",
    30: "Satu Mare",
    31: "Salaj",
    32: "Sibiu",
    33: "Suceava",
    34: "Teleorman",
    35: "Timis",
    36: "Tulcea",
    37: "Vaslui",
    38: "Valcea",
    39: "Vrancea",
    40: "Bucuresti",
    41: "Bucuresti Sectorul 1",
    42: "Bucuresti Sectorul 2",
    43: "Bucuresti Sectorul 3",
    44: "Bucuresti Sectorul 4",
    45: "Bucuresti Sectorul 5",
    46: "Bucuresti Sectorul 6",
    51: "Calarasi",
    52: "Giurgiu"
}