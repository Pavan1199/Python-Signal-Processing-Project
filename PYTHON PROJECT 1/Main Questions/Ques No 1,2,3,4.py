import matplotlib.pyplot as plt
import numpy as np
from comb_step_ramp import comb_step_ramp

'original function'

t = np.arange(-10, 10,0.01)
a=[]
comb_step_ramp(t,a)
print(a)
plt.subplot(2,2,1)
plt.step(t,a)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('original function')

'TIME INVERSION x(-t)'

b=[]
comb_step_ramp(-t,b)
plt.subplot(2,2,2)
plt.step(t,b)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('time inversion x(-t) function')
plt.show()

'AMPLITUDE INVERSION -x(t)'

c=[]
comb_step_ramp(t,c)
plt.subplot(2,2,3)
c[:] = [a*-1 for a in c]
plt.step(t,c)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('amplitude inversion -x(t) function')
plt.show()

'TIME SCALING BY 2t'

d=[]
comb_step_ramp(2*t,d)
plt.subplot(2,2,4)
plt.step(t,d)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('time scalling by 2 function')
plt.show()


