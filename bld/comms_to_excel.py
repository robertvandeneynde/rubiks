import random
import os

def reverse_dict(D):
    return {D[x]:x for x in D}

def dict_from_cycles(cycles):
    D = {}
    for cycle in cycles:
        for i in range(len(cycle)-1):
            D[cycle[i]] = cycle[i+1]
        D[cycle[-1]] = cycle[0]
    return D

def compose_dict(D1,D2):
    return {x:D1[D2[x]] for x in D2}

def apply_dict(D, L):
    return list(map(D.__getitem__, L))

corners_KS = dict(zip(
    "UTRS" "ABIJ" "GHOP" "CDKL" "EFMN" "VWZY",
    "ABDC" "IJLK" "EFHG" "MNPO" "QRTS" "UVXW"
))
corners_SK = reverse_dict(corners_KS)

corners_S3L = {
    "A": "UBL",
    "B": "URB",
    "C": "UFR",
    "D": "ULF",
    "E": "LUB",
    "F": "LFU",
    "G": "LDF",
    "H": "LBD",
    "I": "FUL",
    "J": "FRU",
    "K": "FDR",
    "L": "FLD",
    "M": "RUF",
    "N": "RBU",
    "O": "RDB",
    "P": "RFD",
    "Q": "BUR",
    "R": "BLU",
    "S": "BDL",
    "T": "BRD",
    "U": "DFL",
    "V": "DRF",
    "W": "DBR",
    "X": "DLB",
}
corners_3LS = reverse_dict(corners_S3L)

corners_E3L = compose_dict(corners_S3L, corners_KS)
corners_3LE = reverse_dict(corners_E3L)

rotation_moves = {}

rotation_moves["x"] = {
    "U": "F",
    "B": "U", 
    "D": "B",
    "F": "D",
    "L": "L",
    "R": "R",
}
assert rotation_moves["x"] == dict_from_cycles(["UFDB", "L", "R"])

rotation_moves["y"] = {
    "R": "B",
    "B": "L", 
    "L": "F",
    "F": "R",
    "U": "U",
    "D": "D",
}
assert rotation_moves["y"] == dict_from_cycles(["RBLF", "U", "D"])
rotation_moves["z"] = {
    "L": "U",
    "D": "L",
    "R": "D",
    "U": "R",
    "B": "B",
    "F": "F",
}
assert rotation_moves["z"] == dict_from_cycles(["LURD", "B", "F"])

for s in "xyz":
    for x in list(rotation_moves["y"]):
        rotation_moves[s][x + "'"] = rotation_moves[s][x] + "'"
        rotation_moves[s][x + "2"] = rotation_moves[s][x] + "2"

    rotation_moves[s + "'"] = reverse_dict(rotation_moves[s])
    rotation_moves[s + "2"] = compose_dict(rotation_moves[s], rotation_moves[s])

rotation_letters = {}
rotation_letters["x"] = dict_from_cycles(["CQWK", "BTVJ", "ASUI", "DRXL", "HGFE", "MNOP"])
rotation_letters["y"] = dict_from_cycles(["DCBA", "IMQE", "JNRF", "LPTH", "KOSG", "UVWX"])
rotation_letters["z"] = dict_from_cycles(["IJKL", "ANWH", "BOXE", "CPUF", "DMVG", "TSRQ"])

for s in "xyz":
    rotation_letters[s + "'"] = reverse_dict(rotation_letters[s])
    rotation_letters[s + "2"] = compose_dict(rotation_letters[s], rotation_letters[s])

simplify_cases_1 = {
    'A9': 'A9',
    'Columns': 'CO',
    'Cyclic Shift': 'CS',
    'Orthogonals': 'OR',
    'Per Special': 'PS',
    
    'Direct Insert': 'DI',
    'Drop and Catch': 'DC',
    'Toss Up': 'TU'
}

simplify_cases_2 = {
    'A9': 'A',
    'Columns': 'C',
    'Cyclic Shift': 'Y',
    'Orthogonals': 'O',
    'Per Special': 'S',
    
    'Direct Insert': 'I',
    'Drop and Catch': 'H',
    'Toss Up': 'T'
}

simplify_cases_3 = {
    'A9': 'A9',
    'Columns': 'CO',
    'Cyclic Shift': 'CS',
    'Orthogonals': 'OR',
    'Per Special': 'PS',
    
    'Direct Insert': 'PC',
    'Drop and Catch': 'PC',
    'Toss Up': 'PC'
}

simplify_cases_4 = {
    'A9': 'A',
    'Columns': 'C',
    'Cyclic Shift': 'Y',
    'Orthogonals': 'O',
    'Per Special': 'S',
    
    'Direct Insert': 'P',
    'Drop and Catch': 'P',
    'Toss Up': 'P'
}

simplify_cases = simplify_cases_3
rotation = "y'"
output_type = ["excel", "json"][1]

with open('data/comms.txt') as file:
    commutators = [list(map(str.strip, c.strip().split("\t"))) for c in file]
    del commutators[0]

for letter_scheme in ["speffz", "klise"]:

    if output_type == "excel":
        import openpyxl
        wb = openpyxl.Workbook()
        ws = wb.active
    elif output_type == "json":
        json_list = []
    else:
        raise ValueError("Wrong output_type {output_type!r}")

    first_letters = set()
    for x,y,z in commutators:
        letters = apply_dict(corners_3LS, x.strip('()').split())
        letters = apply_dict(rotation_letters[rotation], letters)
        
        if "speffz" == letter_scheme:
            pass
        elif "klise" == letter_scheme:
            letters = apply_dict(corners_SK, letters)
        else:
            raise ValueError(f"Wrong letter_scheme : {letter_scheme!r}")
        
        alg = y[:y.index('(')].split()
        alg = apply_dict(rotation_moves[rotation], alg)
        
        case = simplify_cases[z]
        
        first_letter, *other_letters = letters
        first_letters.add(first_letter)
        
        if output_type == "excel":
            ws.append((''.join(other_letters), ' '.join(alg), case))
        elif output_type == "json":
            json_list.append([''.join(other_letters), ' '.join(alg), case])
        else:
            raise ValueError
        
    assert len(first_letters) == 1
    buffer, = first_letters
    print(f"Letter scheme {letter_scheme!r} First letter {buffer!r}")
    file_name = f"generated/comms_buffer_changed_{letter_scheme}_buffer_{buffer}"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    if output_type == "excel":
        wb.save(file_name + ".xlsx")
    elif output_type == "json":
        import json
        with open(file_name + ".json", "w") as file:
            json.dump(json_list, file)
    else:
        raise ValueError
