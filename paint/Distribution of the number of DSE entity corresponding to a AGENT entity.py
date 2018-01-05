import matplotlib.pyplot as plt
import numpy as np

# plt.figure(figsize=(10,6))
# x=np.arange(3)+1
#
# y1 = np.array([4655, 145, 1])
# xticks1=list(['1','2','3'])
#
# ax1 = plt.bar(x,y1,width = 0.3,align='center',color ='c',alpha=0.8)
# # plt.legend( (ax1[0], ax2[0]), ('AGENT', 'TARGET') )
#
# plt.xticks(x,xticks1,rotation=360)
#
# plt.xlabel('entity number')
# plt.title('Distribution of the number of DSE entity corresponding to a TARGET entity')
#
# for a,b in zip(x,y1):
#     plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
#
# plt.ylim(0,5000)
# plt.show()

t1 = np.arange(3)+1
t2 = np.arange(4)+1

plt.figure(12)
plt.subplot(221)
y1 = np.array([4655, 145, 1])
xticks1=list(['1','2','3'])
plt.bar(t1,y1,width = 0.3,align='center',color ='c',alpha=0.8)
plt.xticks(t1,xticks1,rotation=360)
# plt.xlabel('entity number')
plt.title('Distribution of the number of DSE entity corresponding to a TARGET entity')
for a,b in zip(t1,y1):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
plt.ylim(0,5000)

plt.subplot(222)
y2 = np.array([3926, 373, 28, 2])
xticks1=list(['1','2','3','4'])
plt.bar(t2,y2,width = 0.3,align='center',color ='c',alpha=0.8)
plt.xticks(t2,xticks1,rotation=360)
# plt.xlabel('entity number')
plt.title('Distribution of the number of DSE entity corresponding to a AGENT entity')
for a,b in zip(t2,y2):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
plt.ylim(0,4200)

plt.subplot(212)
x=np.arange(5)+1

y1 = np.array([1169, 4752, 6, 0, 0])
y2 = np.array([1252, 4424, 231, 18, 2])
xticks1=list(['0','1','2','3','4'])

ax1 = plt.bar(x-0.15,y1,width = 0.3,align='center',color ='c',alpha=0.8)
ax2 = plt.bar(x+0.15,y2,width = 0.3,align='center',color ='#AB82FF',alpha=0.8)
plt.legend( (ax1[0], ax2[0]), ('AGENT', 'TARGET') )
#设置x轴的刻度，将构建的xticks代入，同时由于课程类目文字较多，在一块会比较拥挤和重叠，因此设置字体和对齐方式
plt.xticks(x,xticks1,rotation=360)

plt.xlabel('entity number')
plt.title('Distribution of the number of AGENT or TARGET entity corresponding to a DSE entity')

for a,b in zip(x,y1):
    plt.text(a-0.15, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
for a,b in zip(x,y2):
    plt.text(a+0.15, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
plt.ylim(0,5000)
plt.show()