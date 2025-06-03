import numpy as np
arr = np.array(['red', 'blue', 'red', 'green', 'blue'])
unique_vals, inv = np.unique(arr, return_inverse=True)
print(unique_vals)
print(inv)
