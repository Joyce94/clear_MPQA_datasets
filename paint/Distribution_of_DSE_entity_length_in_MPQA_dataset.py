import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))

x=np.arange(15)+1
y=np.array([3452, 1260, 705, 287, 128, 52, 34, 15, 6, 1, 4, 2, 3, 1, 1])
xticks1=list(['1 word','2 words','3 words','4 words','5 words','6 words','7 words','8 words','9 words','10 words','11 words','14 words', '15 words','18 words','34 words'])
# {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8, 10:9, 11:10, 14:11, 15:12, 18:13, 34:14}
#画出柱状图
plt.bar(x,y,width = 0.5,align='center',color ='#AB82FF',alpha=0.8)

plt.xticks(x,xticks1,size='small',rotation=30)

plt.ylabel('number')
plt.title('Distribution of DSE entity length in MPQA dataset')

for a,b in zip(x,y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
#设置y轴的范围
plt.ylim(0,3600)
plt.show()

