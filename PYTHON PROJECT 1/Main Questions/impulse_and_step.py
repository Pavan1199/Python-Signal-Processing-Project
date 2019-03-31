import matplotlib.pyplot as plt
import numpy as np
from impulse import impulse
from step import step
from comb_step_ramp4 import comb_step_ramp4

t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp4(t,x)

t = np.arange(-10, 10,0.01)
i=[]
impulse(t,i)

z=[]
for j in range(len(t)):
    z.append(i[j]*x[j])

plt.step(t,z)

plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('x(t)*d(t)')
plt.show()

t = np.arange(-10, 10,0.01)
i=[]
impulse(-t,i)

t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp4(t,x)


z=[]
for j in range(len(t)):
    z.append(i[j]*x[j])

plt.step(t,z)

plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('x(t)*d(-t)')
plt.show()


t = np.arange(-10, 10,0.01)
t[:]=[x+2 for x in t]
i=[]
impulse(t,i)

t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp4(t,x)

z=[]
for j in range(len(t)):
    z.append(round(i[j]*x[j],3))

plt.step(t,z)

plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('x(t)*d(t+2)')
plt.show()

t = np.arange(-10, 10,0.01)
t[:]=[x-2 for x in t]
i=[]
impulse(t,i)


t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp4(t,x)

z=[]
for j in range(len(t)):
    z.append(round(i[j]*x[j],3))

plt.step(t,z)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('x(t)*d(t-2)')
plt.show()

t = np.arange(-10, 10,0.01)

i=[]
impulse(t,i)


t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp4(t,x)

z=[]
for j in range(len(t)):
    z.append(round(i[j]*x[j],3))
z[:]=[x*4 for x in z]

plt.step(t,z)

plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('x(t)*4*d(t)')
plt.show()











t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp4(t,x)

t = np.arange(-10, 10,0.01)
u=[]
step(t,u)

z=[]
for j in range(len(t)):
    z.append(u[j]*x[j])

plt.step(t,z)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('x(t)*u(t)')
plt.show()

t = np.arange(-10, 10,0.01)
u=[]
step(-t,u)

t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp4(t,x)


z=[]
for j in range(len(t)):
    z.append(u[j]*x[j])

plt.step(t,z)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('x(t)*u(-t)')
plt.show()


t = np.arange(-10, 10,0.01)
t[:]=[x+2 for x in t]
u=[]
step(t,u)

t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp4(t,x)

z=[]
for j in range(len(t)):
    z.append(round(u[j]*x[j],3))

plt.step(t,z)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('x(t)*u(t+2)')
plt.show()

t = np.arange(-10, 10,0.01)
t[:]=[x-2 for x in t]
u=[]
step(t,u)
print(i)

t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp4(t,x)

z=[]
for j in range(len(t)):
    z.append(round(u[j]*x[j],3))

plt.step(t,z)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('x(t)*u(t-2)')
plt.show()

t = np.arange(-10, 10,0.01)

u=[]
step(t,u)


t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp4(t,x)

z=[]
for j in range(len(t)):
    z.append(round(u[j]*x[j],3))
z[:]=[x*4 for x in z]

plt.step(t,z)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('x(t)*4*u(t)')
plt.show()
