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
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13",
    "E": "14",
    "F": "15",
    "G": "16",
    "H": "17",
    "I": "18",
    "J": "19",
    "K": "20",
    "L": "21",
    "M": "22",
    "N": "23",
    "O": "24",
    "P": "25",
    "Q": "26",
    "R": "27",
    "S": "28",
    "T": "29",
    "U": "30",
    "V": "31",
    "W": "32",
    "X": "33",
    "Y": "34",
    "Z": "35",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
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
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
        16: "G",
        17: "H",
        18: "I",
        19: "J",
        20: "K",
        21: "L",
        22: "M",
        23: "N",
        24: "O",
        25: "P",
        26: "Q",
        27: "R",
        28: "S",
        29: "T",
        30: "U",
        31: "V",
        32: "W",
        33: "X",
        34: "Y",
        35: "Z",
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9"
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
    elif BASE > 36:
        print("New base is greater than thirty-six. Try again.")
    else:
        break

while True:
    NBASE = int(input("Input base to convert to: "))
    if not isinstance(NBASE, int) or NBASE > 36:
        print("New base must be an integer. Try again.")
    elif NBASE < 2:
        print("New base is less than two. Try again.")
    elif NBASE > 36:
        print("New base is greater than thirty-six. Try again.")
    else:
        break

while True:
    NUMBER = input("Input number to convert: ")
    if not digits_lower_than_base(NUMBER, BASE):
        print("A digit is higher than the base the number is. Try again.")
    else:
        break

print()
print(f"The converted number is: {main(NUMBER, BASE, NBASE)}")
