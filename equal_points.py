import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import project_1 as pjt

pq_arr = np.array([4,8,12,16]) #Specify the nth order of the polynomial desired
lbl_p = np.array(['P4(x)','P8(x)','P12(x)','P16(x)']) #Plot labels
lbl_color = np.array(['b','r','c','g']) #Plot color selections

for n in range(4):
    x = pjt.xnj(pq_arr[n]) #Designated equally spaced points to be evaluated 
    y = pjt.function(x) #Cooresponding Y-values from f(xnj)

    poly = lagrange(x, y) #Generates a symbolic lagrange polynomial for the provided x,y points 
    plt.plot(np.arange(-1,1,0.001), Polynomial(poly.coef[::-1])(np.arange(-1,1,0.001)),lbl_color[n] + '-.',label=lbl_p[n]) #Evaluates the polynomial over [-1,1] with stepsize 0.001


plt.plot(np.linspace(-1,1,15),pjt.function(np.linspace(-1,1,15)),'k.',label='f(x)') #Origa=inal function Plotted from [-1,1] with 15 points

#Stylistic Options
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Project 1 - Equal Spaced Points (iii)")
plt.legend(loc='best')
plt.show()

#Portion 2 creates an alternative visualization with each polynomial on a seperate subplot to show subtle differences 
for n in range(4):
    x = pjt.xnj(pq_arr[n])
    y = pjt.function(x)

    poly = lagrange(x, y)
    plt.subplot(2,2,n+1)
    plt.plot(np.arange(-1,1,0.001), Polynomial(poly.coef[::-1])(np.arange(-1,1,0.001)),lbl_color[n] + '-.',label=lbl_p[n])
    plt.plot(np.linspace(-1,1,15),pjt.function(np.linspace(-1,1,15)),'k.',label='f(x)') #Function Plotted from [-1,1]
    plt.legend(loc='best')
    plt.title(lbl_p[n])      

plt.show()

