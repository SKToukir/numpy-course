import numpy as np

# Rand() function, generate random numbers

var = np.random.rand(2)

print(var)

var1 = np.random.rand(2,4)

print(var1)

# Randn() function, generate random numbers

var2 = np.random.randn(5)

print(var2)

var3 = np.random.ranf((2,1))
print()
print(var3)

# Randint() function, generate random numbers

var4 = np.random.randint(5, 20, 5)
print(var4)