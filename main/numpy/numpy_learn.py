import numpy as np


# Zeros

arr = np.zeros(4)

print(arr)

arr1 = np.zeros((3,4))

print(arr1)

# Ones

arr_one = np.ones((3,4))

print(arr_one)

# Empty

arr_empt = np.empty(4)

print(arr_empt)

# Range

arr_range = np.arange(4)

print(arr_range)

# Diagonal elements filled with 1's

arr_dia = np.eye(5,5)

print(arr_dia)

# Array with separated values of spaced linearly line (linspace)

ar_lin = np.linspace(3, 30, num=10)

print(ar_lin)
