def cau_noncau(a,b,c,d,e):
    if(b==0.5):
        b=3
        c=9
    
    if  ((b==1) & (c==0) & (d==0)):
        print(e," is causal")
    elif((b==-1) & (c==0) & (d==0)):
        print(e," is non-causal")
    elif((b>1) & (c==0) & (d==0)):
        print(e," is non-causal")
    elif((b<0) & (c==0) & (d==0)):
        print(e," is non-causal")
    elif((b==3) & (c==9) & (d==0)):
              print(e," is anti-causal")
    elif((b==1) & (c>0) & (d==0)):
              print(e," is anti-causal")
    elif((b==1) & (c<0) & (d==0)):
              print(e," is causal")
    elif((c*d)<0):
              print(e," is non-causal")
    
        
    
