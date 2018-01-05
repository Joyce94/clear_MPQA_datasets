import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))

x=np.arange(12)+1

y=np.array([1281, 2579, 2652, 1761, 817, 250, 82, 28, 13, 4, 1, 3])
xticks1=list(['1-9 words','10-19 words','20-29 words','30-39 words','40-49 words','50-59 words','60-69 words','70-79 words','80-89 words','90-99 words','100-109 words','110-119 words'])

plt.bar(x,y,width = 0.5,align='center',color = 'c',alpha=0.8)

plt.xticks(x,xticks1,size='small',rotation=30)

plt.ylabel('number')
plt.title('Distribution of sentence length in MPQA dataset')

for a,b in zip(x,y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)

plt.ylim(0,3000)
plt.show()

