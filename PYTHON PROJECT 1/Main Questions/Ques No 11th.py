import matplotlib.pyplot as plt
import numpy as np
from comb_step_ramp import comb_step_ramp

'EVEN SIGNAL'

t = np.arange(-10, 10,0.01)
a=[]
comb_step_ramp(t,a)

b=[]
comb_step_ramp(-t,b)

z=[]
plt.subplot(2,1,1)
[z.append((a[i]+b[i])/2) for i in range(len(a))]
plt.step(t,z)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('the even signal')
plt.show()
'ODD SIGNAL'
d=[]
plt.subplot(2,1,2)
[d.append((a[i]-b[i])/2) for i in range(len(a))]
plt.step(t,d)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('odd signal')
plt.show()

