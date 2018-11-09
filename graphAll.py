import matplotlib.pyplot as plt 
import numpy as np 

procs = [[],[],[],[]]
procsErr = [[],[],[],[]]
for i,proc in enumerate([1,2,4,8]):
  for part in ([1,10,20,50,100]):
    # print("tiempoPart"+str(part)+"proc"+str(proc)+".txt")
    data = np.loadtxt("tiempoPart"+str(part)+"proc"+str(proc)+".txt")
    procs[i].append(np.mean(data))
    procsErr[i].append(np.std(data))
    # plt.scatter(part,np.mean(data),label='proc')


# print(procs)
for i,procsito in enumerate(procs):
  # print(procsito)
  (_, caps, _) = plt.errorbar([1,10,20,50,100],procsito,yerr=procsErr[i],label=str([1,2,4,8][i])+" procesadores", markersize=8, capsize=5)
  # plt.plot
# for cap in caps:
#     cap.set_markeredgewidth(1)
plt.xlabel('Particiones')
plt.ylabel('Tiempo (ns)')
plt.legend()
plt.savefig("./graficas/allResults.pdf")