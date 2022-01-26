A = [0]
B = [1]
C = 0
fa = 0
fb = 0
fc = 0
er = 1
i = 0 

while er > 10**-5:
    fa = ((5*A[i])**3) + 405*(A[i]**2) -20
    fb = ((5*B[i])**3) + 405*(B[i]**2) -20
    C = A[i] - ( (( B[i]- A[i])/(fb - fa)) * fa )
    fc = ((5*C)**3) + 405*(C**2) -20
    print('%d : A = %.5f  B = %0.5f '%(i+1,A[i],B[i]), end = '')
    print('C = %0.5f f(C) = %0.5f'%(C,fc))
    print("A:",fa,"B:",fb)
    er = abs(fc - 0)
    if fc < 0 :
        A.append(C)
        B.append(B[i])
    else :
        B.append(C)
        A.append(A[i])
    i += 1 
