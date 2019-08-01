import json
from random import *
import datetime
from time import *



temperatures = []
actTemp = 24.0

for i in range (1, 300):
    actDelta = uniform(-0.5, 2.0)
    date = str(datetime.datetime.now())
    temperatures.append((date, actTemp+actDelta))
    print (i)
    sleep(1)

#print(temperatures)

with open('data.json', 'w') as outfile:
    json.dump(temperatures, outfile)
