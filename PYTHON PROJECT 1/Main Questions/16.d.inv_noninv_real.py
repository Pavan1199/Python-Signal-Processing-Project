import matplotlib.pyplot as plt
import numpy as np
from comb_step_ramp3 import comb_step_ramp3
from inv_noninv import inv_noninv
't'
t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp3(t,x)
inv_noninv(x)

'-t'
y=[]
comb_step_ramp3(-t,y)
inv_noninv(y)
'-x(t)'
z=[]
comb_step_ramp3(t,z)
z[:] = [x*-1 for x in z]
inv_noninv(z)
'x(2t)'
u=[]
comb_step_ramp3(2*t,u)
inv_noninv(u)
'x(t/2)'
x=[]
comb_step_ramp3(t/2,x)
inv_noninv(x)
'4x(t)'
y=[]
comb_step_ramp3(t,y)
y[:] = [x*4 for x in y]
inv_noninv(y)
'-4x(t)'
z=[]
comb_step_ramp3(t,z)
z[:] = [x*-4 for x in z]
inv_noninv(z)
't-2'
x=[]
t[:] = [x-2 for x in t]
comb_step_ramp3(t,x)
inv_noninv(x)
't+2'
t = np.arange(-10, 10,0.01)
y=[]
t[:] = [x+2 for x in t]
comb_step_ramp3(t,y)
inv_noninv(y)
z=[]
for i in range(len(x)):
    z.append(x[i]+y[i])
inv_noninv(z)
