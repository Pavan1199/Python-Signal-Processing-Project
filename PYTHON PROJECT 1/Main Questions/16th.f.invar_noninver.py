import matplotlib.pyplot as plt
import numpy as np
from timevariant_invariant import time_var_invar
from comb_step_ramp1 import comb_step_ramp1
t = np.arange(-10, 10,0.01)

'general form is a(b*t-c+d) c is shift which is t0'
time_var_invar(1,1,2,0,t)
time_var_invar(-1,1,2,0,t)
time_var_invar(1,-1,2,0,t)
time_var_invar(1,2,2,0,t)
time_var_invar(1,0.5,2,0,t)
time_var_invar(4,1,2,0,t)
time_var_invar(-4,1,2,0,t)
a=time_var_invar(1,1,2,-2,t)
b=time_var_invar(1,1,2,2,t)
if((a==b) & (a==1)):
    print("x(t-2)+x(t+2) is also time invariant")
    
