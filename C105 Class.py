import math
import csv
import plotly.express as px
import pandas as pd

with open("data.csv") as f:
    data = csv.reader(f)
    data = list(data)

data = data[0]
mean = 0

for element in data:
    mean += int(element)

mean = mean / len(data)

all_elements = []
for element in data:
    element_calc = (int(element) - mean) ** 2
    all_elements.append(element_calc)

numerator_total = 0
for number in all_elements:
    numerator_total += int(number)


denominator_total = len(all_elements) - 1

result = numerator_total / denominator_total
result = math.sqrt(result)
print(result)
