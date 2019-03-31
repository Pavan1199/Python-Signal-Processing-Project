import matplotlib.pyplot as plt
import numpy as np
from comb_step_ramp3 import comb_step_ramp3
from sta_unsta_func import sta_unsta_func
t = np.arange(-10, 10,0.01)
't'
a=[]
comb_step_ramp3(t,a)
sta_unsta_func(a)

'-t'
b=[]
comb_step_ramp3(-t,b)
sta_unsta_func(b)

'-x(t)'
c=[]
comb_step_ramp3(t,c)
c[:] = [x*-1 for x in c]
sta_unsta_func(c)

'x(2t)'
d=[]
comb_step_ramp3(2*t,d)
sta_unsta_func(d)

'x(t/2)'
e=[]
comb_step_ramp3(t/2,e)
sta_unsta_func(e)

'4x(t)'
f=[]
comb_step_ramp3(t,f)
f[:] = [x*4 for x in f]
sta_unsta_func(f)

'-4x(t)'
g=[]
comb_step_ramp3(t,g)
g[:] = [x*-4 for x in g]
sta_unsta_func(g)

't-2'
h=[]
t[:] = [x-2 for x in t]
comb_step_ramp3(t,h)
sta_unsta_func(h)

't+2'
t = np.arange(-10, 10,0.01)
i=[]
t[:] = [x+2 for x in t]
comb_step_ramp3(t,i)
sta_unsta_func(i)

't-2 + t+2'
j=[]
for k in range(len(h)):
    j.append(h[k]+i[k])
sta_unsta_func(j)




















