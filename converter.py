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

#DECLARATIONS
BASE = 8
NBASE = 16
NUMBER = "137357"


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

    number_list = []
    for digit in num.lower():
        number_list.append(digit)
    finished_list = []
    for digit in number_list:
        match digit:
            case "a":
                finished_list.append("10")
            case "b":
                finished_list.append("11")
            case "c":
                finished_list.append("12")
            case "d":
                finished_list.append("13")
            case "e":
                finished_list.append("14")
            case "f":
                finished_list.append("15")
            case "g":
                finished_list.append("16")
            case "h":
                finished_list.append("17")
            case "i":
                finished_list.append("18")
            case "j":
                finished_list.append("19")
            case "k":
                finished_list.append("20")
            case "l":
                finished_list.append("21")
            case "m":
                finished_list.append("22")
            case "n":
                finished_list.append("23")
            case "o":
                finished_list.append("24")
            case "p":
                finished_list.append("25")
            case "q":
                finished_list.append("26")
            case "r":
                finished_list.append("27")
            case "s":
                finished_list.append("28")
            case "t":
                finished_list.append("29")
            case "u":
                finished_list.append("30")
            case "v":
                finished_list.append("31")
            case "w":
                finished_list.append("32")
            case "x":
                finished_list.append("33")
            case "y":
                finished_list.append("34")
            case "z":
                finished_list.append("35")
            case _:
                finished_list.append(digit)
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

    finished_list = []
    for digit in number_list:
        match digit:
            case 10:
                finished_list.append("A")
            case 11:
                finished_list.append("B")
            case 12:
                finished_list.append("C")
            case 13:
                finished_list.append("D")
            case 14:
                finished_list.append("E")
            case 15:
                finished_list.append("F")
            case 16:
                finished_list.append("G")
            case 17:
                finished_list.append("H")
            case 18:
                finished_list.append("I")
            case 19:
                finished_list.append("J")
            case 20:
                finished_list.append("K")
            case 21:
                finished_list.append("L")
            case 22:
                finished_list.append("M")
            case 23:
                finished_list.append("N")
            case 24:
                finished_list.append("O")
            case 25:
                finished_list.append("P")
            case 26:
                finished_list.append("Q")
            case 27:
                finished_list.append("R")
            case 28:
                finished_list.append("S")
            case 29:
                finished_list.append("T")
            case 30:
                finished_list.append("U")
            case 31:
                finished_list.append("V")
            case 32:
                finished_list.append("W")
            case 33:
                finished_list.append("X")
            case 34:
                finished_list.append("Y")
            case 35:
                finished_list.append("Z")
            case _:
                finished_list.append(str(digit))
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


print(main(NUMBER, BASE, NBASE))
