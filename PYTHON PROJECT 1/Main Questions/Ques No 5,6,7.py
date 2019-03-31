import matplotlib.pyplot as plt
import numpy as np
from comb_step_ramp import comb_step_ramp
t = np.arange(-10, 10,0.01)

'TIME SCALING BY t/2'

a=[]
comb_step_ramp(t/2,a)
plt.subplot(2,2,1)
plt.step(t,a)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('time scaling by 1/2 function')
plt.show()

'AMPLITUDE SCALING BY 4'

b=[]
comb_step_ramp(t,b)
b[:] = [a*4 for a in b]
plt.subplot(2,2,2)
plt.step(t,a)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('amplitude scaling by 4 function')
plt.show()

'AMPLITUDE SCALING BY -4'

c=[]
comb_step_ramp(t,c)
c[:] = [a*-4 for a in c]
plt.subplot(2,2,3)
plt.step(t,c)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('amplitude scaling by -4 function')
plt.show()




