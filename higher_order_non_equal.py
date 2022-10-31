import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import project_1 as pjt

pq_arr = np.array([25,50,75,100])
lbl_p = np.array(['Q25(x)','Q50(x)','Q75(x)','Q100(x)'])

for n in range(4):
    x = pjt.ynj(pq_arr[n])
    y = pjt.function(x)

    poly = lagrange(x, y)
    plt.subplot(2,2,n+1)
    plt.plot(np.arange(-1,1,0.001), Polynomial(poly.coef[::-1])(np.arange(-1,1,0.001)),'-.',label=lbl_p[n])
    plt.plot(np.linspace(-1,1,15),pjt.function(np.linspace(-1,1,15)),'k.',label='f(x)') #Function Plotted from [-1,1]
    plt.title(lbl_p[n])

plt.show()

for n in range(20,75,5):
    x = pjt.ynj(n)
    y = pjt.function(x)

    poly = lagrange(x, y)
    plt.plot(np.arange(-1,1,0.01), Polynomial(poly.coef[::-1])(np.arange(-1,1,0.01)),label=str(n)) #Polynomial from [-1,1]

plt.yscale('symlog')
plt.legend(loc='best', ncol=4)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Higher Order - Non-Equal Points')
plt.show()