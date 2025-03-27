def AsciiSetter (Pix):
    if Pix <= 1:
        return '"'
    elif Pix >= 1 and Pix <= 3:
        return ">"
    elif Pix >= 3 and Pix <= 5:
        return "_"
    elif Pix >= 5 and Pix <= 7:
        return "i"
    elif Pix >= 7 and Pix <= 9:
        return "?"
    elif Pix >= 9 and Pix <= 11:
        return "["
    elif Pix >= 11 and Pix <= 13:
        return "{"
    elif Pix >= 13 and Pix <= 15:
        return ")"
    elif Pix >= 15 and Pix <= 17:
        return "/"
    elif Pix >= 17 and Pix <= 19:
        return "r"
    elif Pix >= 19 and Pix <= 21:
        return "v"
    elif Pix >= 21 and Pix <= 23:
        return "Y"
    elif Pix >= 23 and Pix <= 25:
        return "L"
    elif Pix >= 25 and Pix <= 27:
        return "Z"
    elif Pix >= 27 and Pix <= 29:
        return "p"
    elif Pix >= 29 and Pix <= 31:
        return "h"
    elif Pix >= 31 and Pix <= 33:
        return "*"
    elif Pix >= 33 and Pix <= 35:
        return "#"
    elif Pix >= 35 and Pix <= 37:
        return "M"
    elif Pix >= 37 and Pix <= 39:
        return "W"
    elif Pix >= 39 and Pix <= 41:
        return "&"
    elif Pix >= 41 and Pix <= 43:
        return "8"
    elif Pix >= 43 and Pix <= 45:
        return "%"
    elif Pix >= 45 and Pix <= 47:
        return "B"
    elif Pix >= 47 and Pix <= 50:
        return "@"
    elif Pix >= 50:
        return '$'
    
def AsciiSetter1 (Pix):
    if Pix <= 1:
        return '.'
    elif Pix >= 1 and Pix <= 2:
        return "_"
    elif Pix >= 2 and Pix <= 3:
        return ":"
    elif Pix >= 3 and Pix <= 4:
        return ","
    elif Pix >= 4 and Pix <= 5:
        return "="
    elif Pix >= 5 and Pix <= 6:
        return ";"
    elif Pix >= 6 and Pix <= 7:
        return "<"
    elif Pix >= 7 and Pix <= 8:
        return "!"
    elif Pix >= 8 and Pix <= 9:
        return "c"
    elif Pix >= 9 and Pix <= 10:
        return "/"
    elif Pix >= 10 and Pix <= 11:
        return "?"
    elif Pix >= 11 and Pix <= 12:
        return "L"
    elif Pix >= 12 and Pix <= 13:
        return "v"
    elif Pix >= 13 and Pix <= 14:
        return "J"
    elif Pix >= 14 and Pix <= 15:
        return "("
    elif Pix >= 15 and Pix <= 16:
        return "F"
    elif Pix >= 16 and Pix <= 17:
        return "{"
    elif Pix >= 17 and Pix <= 18:
        return "}"
    elif Pix >= 18 and Pix <= 19:
        return "I"
    elif Pix >= 19 and Pix <= 20:
        return "1"
    elif Pix >= 20 and Pix <= 21:
        return "t"
    elif Pix >= 21 and Pix <= 22:
        return "u"
    elif Pix >= 22 and Pix <= 23:
        return "n"
    elif Pix >= 23 and Pix <= 24:
        return "o"
    elif Pix >= 24 and Pix <= 25:
        return "5"
    elif Pix >= 25 and Pix <= 26:
        return "x"
    elif Pix >= 26 and Pix <= 27:
        return "y"
    elif Pix >= 27 and Pix <= 28:
        return "L"
    elif Pix >= 28 and Pix <= 29:
        return "E"
    elif Pix >= 29 and Pix <= 30:
        return "w"
    elif Pix >= 30 and Pix <= 31:
        return "k"
    elif Pix >= 31 and Pix <= 32:
        return "6"
    elif Pix >= 32 and Pix <= 33:
        return "9"
    elif Pix >= 33 and Pix <= 34:
        return "4"
    elif Pix >= 34 and Pix <= 35:
        return "p"
    elif Pix >= 35 and Pix <= 36:
        return "G"
    elif Pix >= 36 and Pix <= 37:
        return "U"
    elif Pix >= 37 and Pix <= 38:
        return "K"
    elif Pix >= 38 and Pix <= 39:
        return "S"
    elif Pix >= 39 and Pix <= 40:
        return "H"
    elif Pix >= 40 and Pix <= 41:
        return "D"
    elif Pix >= 41 and Pix <= 42:
        return "R"
    elif Pix >= 42 and Pix <= 43:
        return "#"
    elif Pix >= 43 and Pix <= 44:
        return "M"
    elif Pix >= 44 and Pix <= 45:
        return "W"
    elif Pix >= 45 and Pix <= 46:
        return "&"
    elif Pix >= 46 and Pix <= 47:
        return "8"
    elif Pix >= 47 and Pix <= 48:
        return "%"
    elif Pix >= 48 and Pix <= 40:
        return "B"
    elif Pix >= 49 and Pix <= 50:
        return "@"    
    elif Pix >= 50:
        return '$'
    
CharLookUpTable = {
    0: '.',
    1: "_",
    2: ":",
    3: ",",
    4: "=",
    5: ";",
    6: "<",
    7: "!",
    8: "c",
    9: "/",
    10: "?",
    11: "L",
    12: "v",
    13: "J",
    14: "(",
    15: "F",
    16: "{",
    17: "}",
    18: "I",
    19: "1",
    20: "t",
    21: "u",
    22: "n",
    23: "o",
    24: "5",
    25: "x",
    26: "y",
    27: "L",
    28: "E",
    29: "w",
    30: "k",
    31: "6",
    32: "9",
    33: "4",
    34: "p",
    35: "G",
    36: "U",
    37: "K",
    38: "S",
    39: "H",
    40: "D",
    41: "R",
    42: "#",
    43: "M",
    44: "W",
    45: "&",
    46: "8",
    47: "%",
    48: "B",
    49: "@",
    50: "$",
}

def AsciiSetter2(Pix):
    for i in range(50):
        if Pix == i:
            return CharLookUpTable[i] 
