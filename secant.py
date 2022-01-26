import math
A = [0]  ;B = [1]  ;C = 0
fa = 0   ;fb = 0   ;fc = 0
er = 1   ;i = 0 

while er > 10**-5:
    fa = math.sin(405-A[i])
    fb = math.sin(405-B[i])
    C = A[i] - ( (( B[i]- A[i])/(fb - fa)) * fa )
    fc = math.sin(405-C)
    print('%d : A = %.5f   B = %0.5f '%(i+1,A[i],B[i]), end ='   ')
    print('C = %0.5f   f(C) = %0.5f'%(C,fc))
    print("fa",fa,"fb",fb)
    er = abs(fc - 0)
    A.append(B[i])
    B.append(C)
    i += 1 
