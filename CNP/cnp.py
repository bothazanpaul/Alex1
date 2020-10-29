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
from datetime import date

from errors import *
from utils import *


class CNP(object):
    """
    CodNumericPersonal (CNP) class.
    """
    HASH_TABLE = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

    def __init__(self, cnp):
        """
        CNP class constructor. Parses the cnp and saves dates in self.
        :param cnp: The cnp to parse and check.
         :type cnp: basestring | str | unicode | list
        """
        self._S, self._AA, self._LL, self._ZZ, self._JJ, self._NNN, self._C = self._parse(cnp)
        self._cnp = str(cnp)
        self._lcnp = [int(ch) for ch in cnp]
        self._date = date(self._AA, self._LL, self._ZZ)
        self._control_digit = self._calculate_control_digit(self._lcnp)

    @classmethod
    def _check_integrity(cls, cnp):
        """
        Check the integrity of the CNP (meaning that it respects the following rules:
         - 13 chars long;
         - all chars are digits.
        :param cnp: The CNP to check.
         :type cnp: basestring | str | unicode | list
        :return: A boolean value showing if the CNP format is correct.
         :rtype: bool
        """
        if len(cnp) != 13:
            return False
        for dgt in cnp:
            try:
                dgt = int(dgt)
            except ValueError:
                return False
        return True

    @classmethod
    def _calculate_control_digit(cls, cnp):
        """
        Calculates and returns the correct control digit for the given cnp.
        :param cnp: The cnp used to calculate the control digit.
         :type cnp: list[int]
        :return: The correct control digit.
         :rtype: int
        """
        cnp_sum = 0
        for idx in range(12):
            cnp_sum += cnp[idx] * cls.HASH_TABLE[idx]
        rest = cnp_sum % 11
        if rest == 10:
            return 1
        return rest

    @classmethod
    def _parse(cls, cnp):
        """
        Parses the cnp string and returns values for all internal values (sex, date of birth, county etc.).
        :param cnp: The cnp to parse.
         :type cnp: basestring | str | unicode | list
        :return: A tuple of SEX, YEAR, MONTH, DAY, COUNTY, ORDER_NUMBER, CHECKSUM.
         :rtype: tuple[int, int, int, int, int, int, int]
        """
        if not cls._check_integrity(cnp):
            raise CNPError("The CNP format is not valid. It should be SAALLZZJJNNNC.")
        sex = int(cnp[0])
        if sex == 0:
            raise SexError("The 'sex' field cannot be 0 (zero).")
        year = S[sex]["start_year"] + int(cnp[1:3])
        month = int(cnp[3:5])
        day = int(cnp[5:7])
        try:
            _date = date(year, month, day)
        except ValueError as err:
            raise DateError(str(err))
        county = int(cnp[7:9])
        if county not in JJ:
            raise CountyError("This county is not valid (code: {}).".format(county))
        order_number = int(cnp[9:12])
        checksum = int(cnp[12])

        return sex, year, month, day, county, order_number, checksum

    def __str__(self):
        """
        Gets the CNP as string.
        :return: The cnp stored as string.
         :rtype: str
        """
        return self._cnp

    def __repr__(self):
        """
        Gets the CNP as string.
        :return: The cnp stored as string.
         :rtype: str
        """
        return self.__str__()

    def as_list(self):
        """
        Gets the CNP as a list of integers.
        :return: A list of 13 integers representing the CNP.
         :rtype: list[int]
        """
        return self._lcnp

    def valid(self):
        """
        Checks if the cnp is valid.
        :return: A boolean value telling if the cnp is valid.
         :rtype: bool
        """
        return self._C == self._control_digit

    @property
    def control_digit(self):
        """
        Gets the correct calculated control digit.
        :return: The calculated control digit.
         :rtype: int
        """
        return self._control_digit

    @property
    def date(self):
        """
        Gets the date from cnp.
        :return: The cnp date.
         :rtype: datetime.date
        """
        return self._date

    @property
    def sex(self):
        """
        Gets the sex from cnp.
        :return: The cnp sex.
         :rtype: str
        """
        return S[self._S]["sex"]

    @property
    def county(self):
        """
        Get the county from cnp.
        :return: The cnp county.
         :rtype: str
        """
        return JJ[self._JJ]

