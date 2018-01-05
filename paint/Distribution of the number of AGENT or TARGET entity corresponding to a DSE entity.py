import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))
#设置x轴柱子的个数
x=np.arange(5)+1 #课程品类数量已知为14，也可以用len(ppv3.index)
#设置y轴的数值，需将numbers列的数据先转化为数列，再转化为矩阵格式
# y1=np.array([[3864, 365, 74, 18, 4, 1, 1, 2, 0, 0, 0, 0],[3153, 858, 175, 89, 28, 14, 4, 3, 1, 1, 0, 1, 2],[5704, 235, 7, 4, 0, 0, 1, 0, 0, 0, 0, 0]])
y1 = np.array([1169, 4752, 6, 0, 0])
y2 = np.array([1252, 4424, 231, 18, 2])
xticks1=list(['0','1','2','3','4']) #构造不同课程类目的数列
#画出柱状图 #EEDC82
ax1 = plt.bar(x-0.15,y1,width = 0.3,align='center',color ='c',alpha=0.8)
ax2 = plt.bar(x+0.15,y2,width = 0.3,align='center',color ='#AB82FF',alpha=0.8)
plt.legend( (ax1[0], ax2[0]), ('AGENT', 'TARGET') )
#设置x轴的刻度，将构建的xticks代入，同时由于课程类目文字较多，在一块会比较拥挤和重叠，因此设置字体和对齐方式
plt.xticks(x,xticks1,rotation=360)
#x、y轴标签与图形标题
# plt.xlabel('课程主题类别')
# plt.ylabel('number')
plt.xlabel('entity number')
plt.title('Distribution of the number of AGENT or TARGET entity corresponding to a DSE entity')

for a,b in zip(x,y1):
    plt.text(a-0.15, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
for a,b in zip(x,y2):
    plt.text(a+0.15, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)

#设置y轴的范围
plt.ylim(0,5000)
plt.show()

