import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))

x=np.arange(12)+1
y=np.array([2856, 1167, 437, 201, 84, 32, 13, 3, 3, 4, 0, 1])
xticks1=list(['1-4 words','5-9 words','10-14 words','15-19 words','20-24 words','25-29 words','30-34 words','35-39 words','40-44 words','45-49 words','50-54 words','55-59 words'])
plt.bar(x,y,width = 0.5,align='center',color ='#AB82FF',alpha=0.8)

plt.xticks(x,xticks1,size='small',rotation=30)

plt.ylabel('number')
plt.title('Distribution of TARGET entity length in MPQA dataset')

for a,b in zip(x,y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
#设置y轴的范围
plt.ylim(0,3000)
plt.show()

