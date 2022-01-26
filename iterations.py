''' #system of linear equations
x = [-21]
er = 1
i = 0
y = 0

while er > 10**-5:
    y = ((x[i]**3 - 405*x[i] +5) / (-3))**(1/2)
    x.append(y)
    er = abs(x[i]-x[i-1])
    print("x",end="")
    print(i,'=',x[i])
    i += 1    
else :
    print("x",end="")
    print(i,'=',x[i])


A = np.array([[math.sqrt(y[i]+405)],[math.sqrt(405-((x[i]**2)/4))]])
'''
#system of non-linear equations
import numpy as np
import math
x = [0]
y = [0]
i = 0
er = 1

while er > 10**-5:
    A = np.array([[(y[i]**2)-405],[(x[i]**2)+405]])
    x.append(float(A[0]))
    y.append(float(A[1]))
    if abs(x[i]-x[i-1]) < 10**-5 and abs(y[i]-y[i-1]) < 10**-5: 
        break
    i += 1 
    print("x%d = " %i)
    print(np.array([[x[i]],[y[i]]]))
    print()



