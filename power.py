import numpy as np

n = int(input('Enter order of matrix: '))
a = np.zeros((n,n))
print('Enter Matrix Coefficients:')
for i in range(n):
    for j in range(n):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

x = np.zeros((n))
print('\n Enter initial guess vector: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))

# Power Method Implementation
lambda_old = 1.0
xi = 1
error = 1
#xy = 10
#while xy > 1:
while error > 0.1:
    # Multiplying a and x
    x = np.matmul(a,x)
    lambda_new = max(abs(x))
    x = x/lambda_new
    print('\n x%d' %(xi))
    print('Dominant EigenValue = %0.5f' %(lambda_new))
    print('Eigen Vector = ')
    for i in range(n):
        print('\t%0.5f' % (x[i]))
    
    error = abs(lambda_new - lambda_old)
    print("error : %0.5f" %(error))
    lambda_old = lambda_new
    xi += 1
    #xy -= 1
   
    
    
    
    
    
    
    
    
    