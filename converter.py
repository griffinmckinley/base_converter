"""
Change one base to another.

Parameters
----------
base   : int
    starting base
nbase  : int
    base to convert to
number : str
    number to convert

Returns
-------
str
    Returns converted number.
"""



def digits_lower_than_base(num_unsanitized, base_to_check):
    """
    Check if the given number is valid in the given base.

    Parameters
    ----------
    num_unsanitized : str
        Number to check.
    base_to_check : int
        Base to check the number against.

    Returns
    -------
    bool
        Returns True if the number is valid in the given base, False otherwise.
    """
    num_unsanitized = letter_to_number(num_unsanitized)
    return all(int(num) < base_to_check for num in num_unsanitized)

def letter_to_number(num):
    """
    Change letters to the number associated with them.

    Parameters
    ----------
    num : str
        Number with letters to convert.
    
    Returns
    -------
    finished_list : list
        Returns list with each digit converted.
    """

    ltn_dict = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "a": "10",
    "b": "11",
    "c": "12",
    "d": "13",
    "e": "14",
    "f": "15",
    "g": "16",
    "h": "17",
    "i": "18",
    "j": "19",
    "k": "20",
    "l": "21",
    "m": "22",
    "n": "23",
    "o": "24",
    "p": "25",
    "q": "26",
    "r": "27",
    "s": "28",
    "t": "29",
    "u": "30",
    "v": "31",
    "w": "32",
    "x": "33",
    "y": "34",
    "z": "35",
    "A": "36",
    "B": "37",
    "C": "38",
    "D": "39",
    "E": "40",
    "F": "41",
    "G": "42",
    "H": "43",
    "I": "44",
    "J": "45",
    "K": "46",
    "L": "47",
    "M": "48",
    "N": "49",
    "O": "50",
    "P": "51",
    "Q": "52",
    "R": "53",
    "S": "54",
    "T": "55",
    "U": "56",
    "V": "57",
    "W": "58",
    "X": "59",
    "Y": "60",
    "Z": "61"
    }
    number_list = []
    for digit in num.upper():
        number_list.append(digit)
    finished_list = []
    for digit in number_list:
        finished_list.append(ltn_dict[digit])
    return finished_list

def number_to_letter(number_list):
    """
    Change letters to the number associated with them.

    Parameters
    ----------
    number_list : list
        List with numbers to convert to their associated letters.
    
    Returns
    -------
    finished_string : str
        String with letters if associated.
    """

    ntl_dict = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f",
        16: "g",
        17: "h",
        18: "i",
        19: "j",
        20: "k",
        21: "l",
        22: "m",
        23: "n",
        24: "o",
        25: "p",
        26: "q",
        27: "r",
        28: "s",
        29: "t",
        30: "u",
        31: "v",
        32: "w",
        33: "x",
        34: "y",
        35: "z",
        36: "A",
        37: "B",
        38: "C",
        39: "D",
        40: "E",
        41: "F",
        42: "G",
        43: "H",
        44: "I",
        45: "J",
        46: "K",
        47: "L",
        48: "M",
        49: "N",
        50: "O",
        51: "P",
        52: "Q",
        53: "R",
        54: "S",
        55: "T",
        56: "U",
        57: "V",
        58: "W",
        59: "X",
        60: "Y",
        61: "Z",
    }
    finished_list = []
    for digit in number_list:
        finished_list.append(ntl_dict[int(digit)])
    finished_string = "".join(finished_list)
    return finished_string


def number_to_decimal(num, base_converted_from):
    """
    Change a number in one base to decimal.

    Parameters
    ----------
    num : str
        Number to convert to decimal.
    base_converted_from : int
        Base of num to convert from.
    
    Returns
    -------
    int
        Returns converted number in decimal.
    """

    str_digit_list = letter_to_number(num)
    digit_list = []
    for digit in str_digit_list:
        digit_list.append(int(digit))
    place_digit_list = digit_list[::-1] # flip the list around
    decimal = 0
    incrementer = 0
    for digit in place_digit_list:
        decimal += digit * base_converted_from ** incrementer
        incrementer += 1
    return decimal

def decimal_to_base(num, new_base):
    """
    Change a number in decimal to another base.

    Parameters
    ----------
    num : int
        Number to convert to the new base.
    new_base : int
        Base to convert the number to.
    
    Returns
    -------
    int
        Returns converted number in the new base.
    """

    num = int(num)
    if new_base == 10:
        return num
    reversed_nbase_digits = []
    while num > 0:
        remainder = num % new_base
        num = num // new_base
        reversed_nbase_digits.append(remainder)
    nbase_digits = reversed_nbase_digits[::-1]
    return number_to_letter(nbase_digits)


def main(num, base_converted_from, new_base):
    """
    Change a number in one base to another base.

    Parameters
    ----------
    num : str
        Number to convert to the new base.
    base_converted_from : int
        Base of num to convert from.
    new_base : int
        Base to convert the number to.
    
    Returns
    -------
    int
        Returns converted number in the new base.
    """

    ntd = number_to_decimal(num, base_converted_from)
    dtb = decimal_to_base(ntd, new_base)
    return dtb

#DECLARATIONS
while True:
    BASE = int(input("Input base to be converted from: "))
    if not isinstance(BASE, int):
        print("Base must be an integer. Try again.")
    elif BASE < 2:
        print("New base is less than two. Try again.")
    elif BASE > 62:
        print("New base is greater than thirty-six. Try again.")
    else:
        break

while True:
    NBASE = int(input("Input base to convert to: "))
    if not isinstance(NBASE, int):
        print("New base must be an integer. Try again.")
    elif NBASE < 2:
        print("New base is less than two. Try again.")
    elif NBASE > 62:
        print("New base is greater than thirty-six. Try again.")
    else:
        break

print()
print("Lowercase letters range from 10 to 35. Uppercase letters range from 36 to 61.")
print()

while True:
    NUMBER = input("Input number to convert: ")
    if not digits_lower_than_base(NUMBER, BASE):
        print("A digit is higher than the base the number is. Try again.")
    else:
        break

print()
print(f"The converted number is: {main(NUMBER, BASE, NBASE)}")
