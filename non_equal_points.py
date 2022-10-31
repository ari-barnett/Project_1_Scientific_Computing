import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import project_1 as pjt

pq_arr = np.array([4,8,12,16])
lbl_p = np.array(['Q4(x)','Q8(x)','Q12(x)','Q16(x)'])
lbl_color = np.array(['b','r','c','g'])

for n in range(4):
    x = pjt.ynj(pq_arr[n])
    y = pjt.function(x)

    poly = lagrange(x, y)
    plt.plot(np.arange(-1,1,0.001), Polynomial(poly.coef[::-1])(np.arange(-1,1,0.001)),lbl_color[n] + '-.',label=lbl_p[n])
    

plt.plot(np.linspace(-1,1,15),pjt.function(np.linspace(-1,1,15)),'k.',label='f(x)') #Function Plotted from [-1,1]

#Stylistic Options
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Project 1 - Non-Equal Spaced Points (iv)")
plt.legend(loc='best')
plt.show()

for n in range(4):
    x = pjt.ynj(pq_arr[n])
    y = pjt.function(x)

    poly = lagrange(x, y)
    plt.subplot(2,2,n+1)
    plt.plot(np.arange(-1,1,0.001), Polynomial(poly.coef[::-1])(np.arange(-1,1,0.001)),lbl_color[n] + '-.',label=lbl_p[n])
    plt.plot(np.linspace(-1,1,15),pjt.function(np.linspace(-1,1,15)),'k.',label='f(x)') #Function Plotted from [-1,1]
    plt.legend(loc='best')
    plt.title(lbl_p[n])      


plt.show()

