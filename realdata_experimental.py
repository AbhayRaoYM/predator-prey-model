import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.interpolate import interp1d
import csv

with open("new_predator_prey.csv","r") as i:
    rawdata=list(csv.reader(i,delimiter=","))

exampledata=np.array(rawdata[1:],dtype=np.cfloat)
t_exp=np.array(exampledata[:,0],dtype=np.cfloat)
f_exp=np.array(exampledata[:,1],dtype=np.cfloat)
b_exp=np.array(exampledata[:,2],dtype=np.cfloat)

# Interpolate experimental data for fish and bears
f_interp=interp1d(t_exp,f_exp,kind='linear',fill_value="extrapolate")
b_interp=interp1d(t_exp,b_exp,kind='linear',fill_value="extrapolate")


#intial conditions:
y0=[f_exp[0],b_exp[0]] #[fish,bear] initial row

t=np.linspace(0,1000) #time period with n evenly spaced time points
alpha=0.03
beta=0.0009
delta=0.0005
gamma=0.05
para=[alpha,beta,delta,gamma]

#considering steady state
#y0=[gamma/delta,alpha/beta]


def sim(variables,t,para,f_interp,b_interp):
    #declaring the data locally inside the simulation funciton
    #f_model=variables[0] 
    #b_model=variables[1]

    #Interpolated experimental data at time t
    f_data=f_interp(t)
    b_data=b_interp(t)

    alpha=para[0]
    beta=para[1]
    delta=para[2]
    gamma=para[3]

    #writing the ode equations of growth and death term.
    #dxdt=alpha*f_model-beta*f_model*b_model
    #dydt=delta*f_model*b_model-gamma*b_model

    dxdt=alpha*f_data-beta*f_data*b_data
    dydt=delta*f_data*b_data-gamma*b_data

    #return the value of rate of change of fish and bear units
    return([dxdt,dydt])
   
y=odeint(sim,y0,t,args=(para,f_interp,b_interp)) #solves system of ode  

f,(ax1)=plt.subplots(1) #one subplots is generated
plt.title("Lotka-Volterra Predator-Prey Interaction")
line1,=ax1.plot(t_exp, f_exp, 'bo', label="Prey", markersize=4, alpha=0.6)
line2,=ax1.plot(t_exp, b_exp, 'ro', label="Predator", markersize=4, alpha=0.6)
legend=plt.legend()
ax1.set_ylabel("Number of animals")
ax1.set_xlabel("Genration years(Time Period)")

plt.show()

