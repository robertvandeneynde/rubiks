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
proba = PROBA[input("proba ? [c]ategory|[l]inear ").lower()]

filename = f"generated/comms_buffer_changed_{scheme}_buffer_{buffer}.json"
try:
    with open(filename) as file:
        data = json.load(file)
except FileNotFoundError as e:
    print("Not Found", e)
    sys.exit(1)

if proba == 'category':
    categories = list(set(d[2] for d in data))
    def pick_one():
        cat = random.choice(categories)
        return random.choice([d for d in data if d[2] == cat])
     
    def pick(n=1):
        return [pick_one() for i in range(n)]
        
elif proba == 'linear':
    def pick(n=1):
        return random.sample(data, n)

p = pick(10)
answers = input(' '.join(p[0] for p in p) + " ?\n")
correct_answers = ' '.join(p[2] for p in p)
print(correct_answers)
s = 0
for i, (p, a, c) in enumerate(zip(p, answers.split(), correct_answers.split())):
    if a.upper() == c.upper():
        print(p[0], "==", a.upper())
        s += 1
    else:
        print(p[0], "//", a.upper(), "==", c.upper())
print("{}/{}".format(s, 10))
