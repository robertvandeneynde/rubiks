import json
J = json.load(open('generated/comms_buffer_changed_speffz_buffer_E.json'))

from collections import Counter
counter = Counter(J[-1] for J in J)

import matplotlib.pyplot as plt

colors_mapping = {
    "PC" : "#9BBB59",
    "A9" : "#FFC301",
    "PS" : "#FFCCCC",
    "CS" : "#FFFF00",
    "OR" : "#DB7267",
    "CO" : "#5FC0FB",
}

labels = sorted(colors_mapping.keys(), key=lambda x:counter[x], reverse=True)
values = [counter[x] for x in labels]
colors = [colors_mapping[x] for x in labels]

plt.figure(1)
plt.bar(labels, values, color=colors)
plt.savefig('comms_barchart.svg')
plt.savefig('comms_barchart.png', dpi=512)

plt.figure(2)
plt.pie(values, labels=labels, colors=colors, autopct='%.2f%%')
plt.savefig('comms_piechart.svg')
plt.savefig('comms_piechart.png', dpi=512)
