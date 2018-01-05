import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))
x=np.arange(12)+1

y1 = np.array([3864, 365, 74, 18, 4, 1, 1, 2, 0, 0, 0, 0])
y2 = np.array([2856, 1167, 437, 201, 84, 32, 13, 3, 3, 4, 0, 1])
y3 = np.array([5704, 235, 7, 4, 0, 0, 1, 0, 0, 0, 0, 0])
xticks1=list(['0-4 words','5-9 words','10-14 words','15-19 words','20-24 words','25-29 words','30-34 words','35-39 words','40-44 words','45-49 words','50-54 words','55-59 words'])

ax1 = plt.bar(x-0.3,y1,width = 0.3,align='center',color ='b',alpha=0.8)
ax2 = plt.bar(x,y2,width = 0.3,align='center',color ='g',alpha=0.8)
ax3 = plt.bar(x+0.3,y3,width = 0.3,align='center',color ='r',alpha=0.8)
plt.legend( (ax1[0], ax2[0], ax3[0]), ('AGENT', 'TARGET', 'DSE') )

plt.xticks(x,xticks1,size='small',rotation=30)

plt.ylabel('number')
plt.title('Distribution of entity length in MPQA dataset')

for a,b in zip(x,y1):
    plt.text(a-0.3, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
for a,b in zip(x,y2):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
for a,b in zip(x,y3):
    plt.text(a+0.3, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
#设置y轴的范围
plt.ylim(0,6000)
plt.show()

