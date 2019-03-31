def sta_unsta_func(x):
    m=0
    for i in range(len(x)):
        if ((x[i]<100000000) & (x[i]>-1000000)):
            m=1
        else:
            m=0
            print("the given funnction is not stable")
            break
    if(m==1):
        print("the given function is stable")
