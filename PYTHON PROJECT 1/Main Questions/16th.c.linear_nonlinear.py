import matplotlib.pyplot as plt
import numpy as np
from comb_step_ramp3 import comb_step_ramp3
from linear_nonlinear import lin_nonlin
't'
t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp3(t,x)
lin_nonlin(x)

'-t'
y=[]
comb_step_ramp3(-t,y)
lin_nonlin(y)
'-x(t)'
z=[]
comb_step_ramp3(t,z)
z[:] = [x*-1 for x in z]
lin_nonlin(z)
'x(2t)'
u=[]
comb_step_ramp3(2*t,u)
lin_nonlin(u)
'x(t/2)'
x=[]
comb_step_ramp3(t/2,x)
lin_nonlin(x)
'4x(t)'
y=[]
comb_step_ramp3(t,y)
y[:] = [x*4 for x in y]
lin_nonlin(y)
'-4x(t)'
z=[]
comb_step_ramp3(t,z)
z[:] = [x*-4 for x in z]
lin_nonlin(z)
't-2'
x=[]
t[:] = [x-2 for x in t]
comb_step_ramp3(t,x)
lin_nonlin(x)
't+2'
t = np.arange(-10, 10,0.01)
y=[]
t[:] = [x+2 for x in t]
comb_step_ramp3(t,y)
lin_nonlin(y)
z=[]
for i in range(len(x)):
    z.append(x[i]+y[i])
lin_nonlin(z)

