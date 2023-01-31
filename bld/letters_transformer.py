corners_KS = dict(zip(
    "UTRS" "ABIJ" "GHOP" "CDKL" "EFMN" "VWZY",
    "ABDC" "IJLK" "EFHG" "MNPO" "QRTS" "UVXW"
    ))
corners_SK = {y:x for x,y in corners_ES.items()}

corners_S3L = {
    "A": "UBL",
    "B": "UBR",
    "C": "URF",
    "D": "UFL",
    "E": "LBU",
    "F": "LUF",
    "G": "LFD",
    "H": "LDB",
    "I": "FLU",
    "J": "FUR",
    "K": "FRD",
    "L": "FDL",
    "M": "RFU",
    "N": "RUB",
    "O": "RBD",
    "P": "RDF",
    "Q": "BRU",
    "R": "BUL",
    "S": "BLD",
    "T": "BDR",
    "U": "DLF",
    "V": "DFR",
    "W": "DRB",
    "X": "DBL",
}

edges_S2L = {
    "A": "U",
    "B": "U",
    "C": "U",
    "D": "U",
    "E": "L",
    "F": "L",
    "G": "L",
    "H": "L",
    "I": "F",
    "J": "F",
    "K": "F",
    "L": "F",
    "M": "R",
    "N": "R",
    "O": "R",
    "P": "R",
    "Q": "B",
    "R": "B",
    "S": "B",
    "T": "B",
    "U": "D",
    "V": "D",
    "W": "D",
    "X": "D",
}

def map_corners_KS(s):
    """From Klise to Speffz"""
    return ''.join(corners_ES[x] for x in s)
    
def map_corners_SK(s):
    """From Speffz to Klise"""
    return ''.join(corners_SE[x] for x in s)

if __name__ == '__main__':
    letters = input("Letters ?").upper()
    is_klise = input("[K]lise or [S]peffz ?").lower() == 'k'
    is_corners = input("[C]orner or [E]dge ?").lower() == 'c'

    if is_corners:
        func = map_corners_KS if is_klise else map_corners_SK
    else:
        raise ValueError("Not Implemented yet")

    print(func(letters))
