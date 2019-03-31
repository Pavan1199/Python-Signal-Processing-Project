def comb_step_ramp2(t,x):
    
    for i in t:
        if i <=-6:
            k=-2
            step(-6,i,k,x)
        elif (i>-6) & (i<=-2) :
            ramp(-2,i,4,1,x)
        elif (i>-2) & (i<-1) :
            step(-1,i,-1,x)
        elif (i>=-1) & (i<=1) :
            step(+1,i,2,x)
        elif (i>1) & (i<=2) :
            step(2,i,-1,x)
        elif (i>2) & (i<=6) :
            ramp(6,i,-3,1,x)
        
        else:
            x.append(3)

def step(j,i,k,x):
    if j >=i:
        x.append(k)
    else:
        x.append(0)
    
def ramp(j,i,k,l,x):
    if j >=i:
        x.append(l*i+k)

    else:
        x.append(0)
