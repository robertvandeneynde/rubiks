import json
import random

SCHEME = {
    "s": "speffz",
    "k": "klise",
    '': "speffz",
}

PROBA = {
    "l": "linear",
    "linear": "linear",
    "c": "category",
    "category": "category",
    "": "category",
}

scheme = SCHEME[input("[s]peffz|[k]klise ").lower()]
buffer = input("Buffer ? (Letter) ").upper()
proba = PROBA[input("proba ? [c]ategory|[l]inear").lower()]

filename = f"generated/comms_buffer_changed_{scheme}_buffer_{buffer}.json"
try:
    with open(filename) as file:
        data = json.load(file)
except FileNotFoundError as e:
    print("Not Found", e)
    sys.exit(1)

if proba == 'category':
    categories = list(set(d[2] for d in data))
    def pick(n=1):
        cat = random.choice(categories)
        if n == 1:
            return random.choice([d for d in data if d[2] == cat])
        else:
            return [pick(1) for i in range(n)]
        
elif proba == 'linear':
    def pick(n=1):
        return random.sample(data, n)

p = pick(1)
answer = input(p[0] + "? ")
correct_answer = p[2]
if answer.upper() == answer.upper():
    print("Correct")
else:
    print("False")
