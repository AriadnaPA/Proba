import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, norm

n = 1000
p = 0.3

# PMF DE X
valor = np.arange(0, n+1)
pmf = binom.pmf(valor, n, p)
plt.figure(figsize=(10, 6))
plt.stem(valor, pmf, markerfmt='.', linefmt='pink', basefmt=" ")
plt.title( 'PMF DE X')
plt.xlabel('X')
plt.ylabel('P')
plt.show()

# PMF DE Y
y = (valor - 300) / np.sqrt(210)
plt.figure(figsize=(10, 6))
plt.stem(y, pmf, markerfmt='.', linefmt='blue', basefmt=" ")
plt.title('PMF DE Y')
plt.xlabel('Y')
plt.ylabel('P')
plt.show()

# PMF DE Z
valores = np.linspace(-5, 5, 1000)
x = norm.pdf(valores, 0, 1)
plt.figure(figsize=(10, 6))
plt.plot(valores, x, color='blue')
plt.title('PMF de Z ')
plt.xlabel('Z')
plt.ylabel('P')
plt.show()
