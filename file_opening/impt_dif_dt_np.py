import numpy as np

file = 'titanic_sub.csv'

d = np.recfromcsv(file, delimiter=',', names=True, dtype=None)
#printing first 3 cols
print(d[:3])