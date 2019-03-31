import matplotlib.pyplot as plt
import numpy as np
from cau_noncau import cau_noncau
t = np.arange(-10, 10,0.01)

'general form is a(b*t-c+d) c is shift which is t0'
cau_noncau(1,1,0,0,1)
cau_noncau(1,-1,0,0,2)
cau_noncau(-1,1,0,0,3)
cau_noncau(1,2,0,0,4)
cau_noncau(1,0.5,0,0,5)
cau_noncau(4,1,0,0,6)
cau_noncau(-4,1,0,0,7)
cau_noncau(1,1,-2,0,8)
cau_noncau(1,1,2,0,9)
cau_noncau(1,1,-2,2,10)
