import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import project_1 as pjt
import sympy

pq_arr = np.array([25,50,75,100])
lbl_p = np.array(['P25(x)','P50(x)','P75(x)','P100(x)'])

for n in range(4):
    x = pjt.xnj(pq_arr[n])
    y = pjt.function(x)

    poly = lagrange(x, y)

    plt.subplot(2,2,n+1)
    plt.plot(np.arange(-1,1,0.001), Polynomial(poly.coef[::-1])(np.arange(-1,1,0.001)),'-.',label=lbl_p[n]) #Polynomial from [-1,1]
    plt.plot(np.linspace(-1,1,15),pjt.function(np.linspace(-1,1,15)),'k.',label='f(x)') #Function Plotted from [-1,1]
    plt.title(lbl_p[n])
    plt.legend(loc='best')

plt.show()

#plt.plot(np.linspace(-1,1,15),pjt.function(np.linspace(-1,1,15)),'k.',label='f(x)') #Function Plotted from [-1,1]
for n in range(20,75,5):
    x = pjt.xnj(n)
    y = pjt.function(x)

    

    poly = lagrange(x, y)
    plt.plot(np.arange(-1,1,0.01), Polynomial(poly.coef[::-1])(np.arange(-1,1,0.01)),label=str(n)) #Polynomial from [-1,1]
    #print(pjt.isMonotonic(Polynomial(poly.coef[::-1])(np.arange(-1,1,0.001))))
   
    

plt.yscale('symlog')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Higher Order - Equal Points')
plt.legend(loc='best', ncol=4)
plt.show()
