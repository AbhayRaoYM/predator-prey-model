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

y1=odeint(sim,y0,t,args=(para,)) #alpha=1.1; first simulation

para=[0.8,beta,delta,gamma]
y2=odeint(sim,y0,t,args=(para,)) #second simulation

para=[1.3,beta,delta,gamma]
y3=odeint(sim,y0,t,args=(para,)) #third simulation

f,(ax1)=plt.subplots(1)

line1,=ax1.plot(y1[:,0],y1[:,1],color="g",label="alpha=1.1")
line2,=ax1.plot(y2[:,0],y2[:,1],color="b",label="alpha=0.8")
line3,=ax1.plot(y3[:,0],y3[:,1],color="r",label="alpha=1.3")
legend=plt.legend()
ax1.set_xlabel("Prey (thousands)")
ax1.set_ylabel("Predator (thousands)")
plt.show()