import matplotlib
matplotlib.use("Agg")
import numpy as np 
import matplotlib.pyplot as plt 

data = np.loadtxt('./results.dat',delimiter=' ')

plt.scatter(data[:,0],data[:,1])
plt.xlabel('# of partitions')
plt.ylabel('time (ms)')
plt.savefig('results.pdf')
