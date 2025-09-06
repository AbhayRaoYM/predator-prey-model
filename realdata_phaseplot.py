import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import csv

with open("Predator prey model.csv","r") as i:
    rawdata=list(csv.reader(i,delimiter=",")) 

exampledata=np.array(rawdata[1:],dtype=np.cfloat)
xdata=exampledata[:,0]
ydata=exampledata[:,1]

plt.figure(1,dpi=100)
plt.plot(xdata,ydata,label="Real Data")
plt.title("Predator V/S Prey Count")
plt.xlabel("Number of Prey")
plt.ylabel("Number of Predator")
plt.xscale("linear")
plt.yscale("linear")
plt.show()
