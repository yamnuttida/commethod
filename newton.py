''' #system of linear equations
import math
x = [0]  ;xi = 0 
fx = 0   ;dfx = 0
er = 1   ;i = 0 
print("%d : x%d = %.5f " %(i,i,x[i]))

while er > 10**-5:
    fx = math.sin(405-x[i])
    dfx = -math.cos(405-x[i])
    xi = x[i] - (fx/dfx)
    x.append(xi)
    i += 1
    print("%d : x%d = %.5f " %(i,i,x[i]), end='  ')
    fx = math.sin(405-x[i])
    print("f(x%d) = %0.5f" %(i,fx))
    er = abs(fx - 0)
'''
#system of non-linear equations
import numpy as np
xi = [0]  ;yi = [0] 
er = 10    ;l = 0 
fx = 0    ;dfx = 0

while er > 1:
    fx = np.array([[(yi[l]**2)-xi[l] -405],[(xi[l]**2)-yi[l] +405]])
    dfx = np.array([[-1,2*yi[l]],[2*xi[l],-1]])
    #Gaussian elimination
    A = dfx
    b = -fx
    n = len(A)
    B = A
    A = np.hstack((A,b))
    for i in range(0,n-1):
        for j in range(i+1,n):
            lamb = -A[j,i]/A[i,i]
            A[j,:] = A[j,:] + lamb*A[i,:]
    b = A[:,n]
    A = A[:,0:n]
    
    n = n-1
    x = np.zeros([n+1,1]) 
    x[n] = b[n] / A[n,n]
    
    for k in range(n-1,-1,-1):
        x[k] = (b[k]-sum(A[k,k+1:]@x[k+1:])) / A[k,k]
    
    xi.append(xi[l]+float(x[0]))
    yi.append(yi[l]+float(x[1]))
    l += 1
    print("x%d = " %l)
    print(np.array([[xi[l]],[yi[l]]]))
    
    if abs(fx[0] - 0) < 10**-5 and abs(fx[1] - 0) < 10**-5: 
        break
    
print("fx = ",fx)
