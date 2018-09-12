from SALib.sample import saltelli
from SALib.analyze import sobol
from sklearn import preprocessing
import numpy as np

problem = {
'num_vars': 10,
'names': ['AOD', 'SO2', 'NO2', 'CO', 'O3', 'AIR', 'RH', 'WS', 'P', 'WD'],
'bounds': [[0.01758, 3.49483],
[1,461.5],
[1, 299.5],
[0.001, 30.322],
[1.33333, 336.33333],
[251.31099, 308.61063],
[4.4534,96.90216],
[0.02431, 11.81973],
[87639.78125,101532.9141],
[0.02211, 360]]
}

Y = np.loadtxt("Y.txt", float)

# Perform analysis
Si = sobol.analyze(problem, Y, print_to_console=True)
# Print the first-order sensitivity indices
print Si

