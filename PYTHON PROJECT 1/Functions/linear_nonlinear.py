def lin_nonlin(x):
    
    k=0
    l=0
    m=1
    for i in range(len(x)):
        k=0
        if(m!=0):
            for j in range(len(x)):
                if (round((x[i]+x[j]),3)==round(x[i+j],3)):
                    k=k+1
                else:
                    print("not linear")
                    m=0
                    break
            
            if(k==len(x)):
                l=l+1
    if (l==len(x)):
        print("linear function")
