import matplotlib.pyplot as plt
import numpy as np

class linear:
	def __init__(self):
		
		x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
		y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
		n = 10
		    
		dl1 = 0
		dl0 = 0
		t0 = 0
		t1 = 0
		w = [0]*2
		a = 0.1
		
		
		while(1 == 1):
		    for i in range(0,n):
		        #dl1 += (((w[1]*x[i]) + w[0] - y[i])*2*x[i])
		        dl0 += ((w[1]*x[i]) + w[0] - y[i])*2
		        
		    dl0 = dl0/float(n)
		    dl1 = dl1/float(n)
		    
		    t0 = w[0] - (a*dl0)
		    t1 = w[1] - (a*dl1)
		    
		    if((w[0] == t0) and (w[1] == t1)):
		        break
		    else:
		        w[0] = t0
		        w[1] = t1
		   
		plt.plot(x,y,'ro')
		p = np.linspace(-1,1,100)
		plt.plot(p,t1*p + t0)
		plt.show()

if __name__ == '__main__':
	linear()
