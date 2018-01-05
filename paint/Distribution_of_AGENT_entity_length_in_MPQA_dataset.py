import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))

x=np.arange(13)+1
y=np.array([3153, 858, 175, 89, 28, 14, 4, 3, 1, 1, 0, 1, 2])
xticks1=list(['1-2 words','3-5 words','6-8 words','9-11 words','12-14 words','15-17 words','18-20 words','21-23 words','24-26 words','27-29 words','30-32 words','33-35 words', '36-38 words'])

plt.bar(x,y,width = 0.5,align='center',color ='#AB82FF',alpha=0.8)

plt.xticks(x,xticks1,size='small',rotation=30)

plt.ylabel('number')
plt.title('Distribution of AGENT entity length in MPQA dataset')

for a,b in zip(x,y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)

plt.ylim(0,3300)
plt.show()

