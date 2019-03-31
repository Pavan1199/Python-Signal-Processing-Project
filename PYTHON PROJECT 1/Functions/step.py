def step(t,u):
    
    for j in t:
        
        if (round(j,3)>=0):
            u.append(1)
        else:
            u.append(0)
