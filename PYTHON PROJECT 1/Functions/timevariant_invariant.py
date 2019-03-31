from comb_step_ramp1 import comb_step_ramp1
import numpy as np
import matplotlib.pyplot as plt
def time_var_invar(a,b,c,d,t):
    t = np.arange(-10, 10,0.01)
    x=[]
    comb_step_ramp1(b*t,x)

    
    

    t[:] = [x+c+d for x in t]
  
    
    x[:] = [x*a for x in x]
    
    

    t= np.arange(-10, 10,0.01)
    y=[]

    t[:] = [x-c+d for x in t]

    comb_step_ramp1(b*t,y)
    t[:] = [x+c+d for x in t]


    y[:] = [x*a for x in y]
    
    
    m=0


    for i in range(len(x)):
        if(i<(2000-((c-d)*200))):
            a=round(x[i],3)
            b=round(y[i+(c-d)*100],3)
            
    
        if(a==b):
            m=1
        else:
            m=0
            break
    if(m==1):
        print("time invariant\n")
    else:
        print("time variant")
    return m
    
    

