import matplotlib.pyplot as plt
import numpy as np
from comb_step_ramp import comb_step_ramp
from scipy.integrate import quad
t = np.arange(-10, 10,0.01)

'TIME SCALING t-2'

x=[]
t[:] = [x-2 for x in t]
comb_step_ramp(t,x)
plt.subplot(2,2,1)
t[:] = [x+2 for x in t]
plt.step(t,x)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('time scaling by t-2 function')
plt.show()

'TIME SCALING t+2'

y=[]
t[:] = [x+2 for x in t]
comb_step_ramp(t,y)
plt.subplot(2,2,2)
t[:] = [x-2 for x in t]
plt.step(t,y)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('time scaling by t+2 function')
plt.show()

'COMBINATION OF TIME SCALING t-2 AND TIME SCALING t+2'

z=[]
plt.subplot(2,2,3)
[z.append(x[i]+y[i]) for i in range(len(x))]
plt.step(t,z)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('combination of t-2 and t+2 function')
plt.show()


'power or energy'

v=0
t = np.arange(-100000001, -100000000,1)
x=[]
comb_step_ramp(t,x)
print("value of function at near negative infinite is ",x[0])
for i in x:
    if i>0:
        v=1
for k in range(1,11,1):
    l=0
    for i in range((len(x)//100)-k):
        if (x[i*100]==x[i*100+k*100]):
            l=l+1
          
        else:
            l=0
            break
           
    if (l== (20-k)):
        m=1
        print("it is power signal")
        break
    else:
        m=0
if (m==0 & (v!=0)):
    print("it is one sided power signal")
elif(m==0 & v==0):
    print("it is energy signal")
else:
    print("it is neither power nor energy")


'for energy'

def integrand(y):
    return -2**2

ans, err = quad(integrand, -1000000000, -3)
x1=ans
def integrand(y):
    return (y+3)**2

ans, err = quad(integrand, -3,-2)
x2=ans
def integrand(y):
    return -1**2

ans, err = quad(integrand, -2,0)
x3=ans
def integrand(y):
    return 2**2

ans, err = quad(integrand, 0,1)
x4=ans
def integrand(y):
    return -1**2

ans, err = quad(integrand, 1,2)
x5=ans
def integrand(y):
    return (y-3)**2

ans, err = quad(integrand, 2,3)
x6=ans
def integrand(y):
    return 3**2

ans, err = quad(integrand, 3,1000000000)
x7=ans

i=0
i=x1+x2+x3+x4+x5+x6+x7

'for average power'

print("energy of the signal when taken from -1000000000 to 1000000000 is ",i)

def integrand(y):
    return -2**2

ans, err = quad(integrand, -1000, -3)
x1=ans
def integrand(y):
    return (y+3)**2

ans, err = quad(integrand, -3,-2)
x2=ans
def integrand(y):
    return -1**2

ans, err = quad(integrand, -2,0)
x3=ans
def integrand(y):
    return 2**2

ans, err = quad(integrand, 0,1)
x4=ans
def integrand(y):
    return -1**2

ans, err = quad(integrand, 1,2)
x5=ans
def integrand(y):
    return (y-3)**2

ans, err = quad(integrand, 2,3)
x6=ans
def integrand(y):
    return 3**2

ans, err = quad(integrand, 3,1000)
x7=ans

i=0
i=x1+x2+x3+x4+x5+x6+x7

u=np.arange(-1000,1000,1)

print("average power  when taken from -1000 to 1000  is ",(i/len(u)))

'for even or odd signal'
        

t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp(t,x)


y=[]
comb_step_ramp(-t,y)
m=0
for i in range(len(x)):
    if (x[i]==y[i]):
        m=1
    else:
        m=0
        print("the given signal is odd signal")
        break
if (m==1):
    print("the given signal is  even signal")

'for periodic or aperiodic'

m=0
for k in range(1,11,1):
    if (m==1):
        break
    l=0
    for i in range((len(x)//100)-k):
        if (x[i*100]==x[i*100+k*100]):
            l=l+1
          
        else:
            l=0
            break
           
    if (l== (20-k)):
        m=1
        print("it is periodic signal")
        break
    else:
        m=0

if (m==0):
    print("the given signal is  aperiodic signal")

'for bounded or unbounded'

m=0
t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp(t,x)
for i in range(len(x)):
            if ( x[i] < 1000000000 ):
                m=1
            else:
                print("it is an unbounded function")
                break
if(m==1):
        print("the given function is bounded function")
            
                
                
            
            
            





            


