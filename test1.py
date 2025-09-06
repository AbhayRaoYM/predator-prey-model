import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#intial conditions:
y0=[10,1] #[fish,bear] in thousands

t=np.linspace(0,50,num=1000) #time period with n evenly spaced time points
alpha=1.1
beta=0.4
delta=0.1
gamma=0.4

#considering steady state
#y0=[gamma/delta,alpha/beta]

para=[alpha,beta,delta,gamma]
def sim(variables,t,para):
    #declaring the data locally inside the simulation funciton
    x=variables[0]
    y=variables[1]
    alpha=para[0]
    beta=para[1]
    delta=para[2]
    gamma=para[3]

    #writing the ode equations of growth and death term.
    dxdt=alpha*x-beta*x*y
    dydt=delta*x*y-gamma*y

    #return the value of rate of change of fish and bear units
    return([dxdt,dydt])

y=odeint(sim,y0,t,args=(para,)) #solves system of ode

f,(ax1,ax2)=plt.subplots(2) #two subplots is generated
line1,=ax1.plot(t,y[:,0],color="b") #fish in the fist column
line2,=ax2.plot(t,y[:,1],color="r") #bear in the second column

ax1.set_ylabel("Fish(thousands)")
ax2.set_ylabel("Bears(thousands)")
ax2.set_xlabel("Time Period")
plt.show()