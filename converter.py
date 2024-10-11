#DECLARATIONS
base = 8
nbase = 16
number = "137357"

# [A -> 10], [B -> 11], so on and so forth
def letter_to_number(number):
    number_list = []
    for digit in number.lower():
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


def number_to_decimal(number, base):
    str_digit_list = letter_to_number(number)
    digit_list = []
    for digit in str_digit_list:
        digit_list.append(int(digit))
    place_digit_list = digit_list[::-1] # flip the list around
    decimal = 0
    incrementer = 0
    for digit in place_digit_list:
        decimal += digit * base ** incrementer
        incrementer += 1
    return decimal

def decimal_to_base(number, nbase):
    number = int(number)
    if nbase == 10:
        return number
    reversed_nbase_digits = []
    while number > 0:
        remainder = number % nbase
        number = number // nbase
        reversed_nbase_digits.append(remainder)
    nbase_digits = reversed_nbase_digits[::-1]
    return number_to_letter(nbase_digits)


def main(number, base, nbase):
    ntd = number_to_decimal(number, base)
    dtb = decimal_to_base(ntd, nbase)
    return dtb

print(main(number, base, nbase))