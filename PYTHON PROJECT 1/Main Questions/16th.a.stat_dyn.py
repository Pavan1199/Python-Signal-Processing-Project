import matplotlib.pyplot as plt
import numpy as np
from comb_step_ramp3 import comb_step_ramp3
from stat_dyn_func import stat_dyn_fun
t = np.arange(-10, 10,0.01)
't'
a=[]
comb_step_ramp3(t,a)
stat_dyn_fun(a,a)

'-t'
b=[]
comb_step_ramp3(-t,b)
stat_dyn_fun(a,b)

'-x(t)'
c=[]
comb_step_ramp3(t,c)
c[:] = [x*-1 for x in c]
stat_dyn_fun(a,c)

'x(2t)'
d=[]
comb_step_ramp3(2*t,d)
stat_dyn_fun(a,d)

'x(t/2)'
e=[]
comb_step_ramp3(t/2,e)
stat_dyn_fun(a,e)

'4x(t)'
f=[]
comb_step_ramp3(t,f)
f[:] = [x*4 for x in f]
stat_dyn_fun(a,f)

'-4x(t)'
g=[]
comb_step_ramp3(t,g)
g[:] = [x*-4 for x in g]
stat_dyn_fun(a,g)

't-2'
h=[]
t[:] = [x-2 for x in t]
comb_step_ramp3(t,h)
stat_dyn_fun(a,h)

't+2'
t = np.arange(-10, 10,0.01)
i=[]
t[:] = [x+2 for x in t]
comb_step_ramp3(t,i)
stat_dyn_fun(a,i)

't-2 + t+2'
j=[]
for k in range(len(h)):
    j.append(h[k]+i[k])
stat_dyn_fun(a,j)
