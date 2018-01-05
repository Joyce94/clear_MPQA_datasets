import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))
x=np.arange(3)+1

y1 = np.array([4655, 145, 1])
xticks1=list(['1','2','3'])

ax1 = plt.bar(x,y1,width = 0.3,align='center',color ='c',alpha=0.8)
# plt.legend( (ax1[0], ax2[0]), ('AGENT', 'TARGET') )

plt.xticks(x,xticks1,rotation=360)

plt.xlabel('entity number')
plt.title('Distribution of the number of DSE entity corresponding to a TARGET entity')

for a,b in zip(x,y1):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)

plt.ylim(0,5000)
plt.show()

