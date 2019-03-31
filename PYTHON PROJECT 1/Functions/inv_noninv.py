def inv_noninv(x):
    
    k=0
    l=0
    m=1
    for i in range(len(x)):
        k=0
        if(m!=0):
            for j in range(len(x)):
                if(i!=j):
                    
                    if (round(x[i],3)==round(x[j],3)):
                        print("not one to one")
                        print("so non-invertible\n")
                        m=0
                        break
                    
                    else:
                        k=k+1
                    
            
            if(k==len(x)-1):
                l=l+1
    if (l==len(x)):
        print("invertible")

