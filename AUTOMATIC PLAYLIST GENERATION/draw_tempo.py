import madmom
import matplotlib.pyplot as plt
from madmom.features.beats import RNNBeatProcessor
from madmom.features.tempo import TempoEstimationProcessor
proc2 = TempoEstimationProcessor(fps=100)
act2 = RNNBeatProcessor()("./music/13/茶理理,TetraCalyx,Hanser - Moon Halo.mp3")
print(proc2(act2))
a2 =  proc2(act2)
proc1 = TempoEstimationProcessor(fps=100)
act1 = RNNBeatProcessor()("./music/13/Team Grimoire,Laur - Grievous Lady.mp3")
print(proc1(act1)) 
a1 = proc1(act1)
# def ex(list):
#     sum = 0
#     for i in range(0,len(list)):
#         sum += list[i][0]*list[i][1]
#     return sum
# print(ex(a1))
# print(ex(a2))
def re_list1(a,b):
    for i in range(0,len(a)):
        b[i] = a[i][0]
        # print(b[i])
    return b

def re_list2(a,b):
    for i in range(0,len(a)):
        b[i] = a[i][1]
    return b
# a11 = list(range(len(a1)))
# print(a)
a1_1 = re_list1(a1, list(range(len(a1))))
a1_2 = re_list2(a1, list(range(len(a1))))
print(a1_1)
print(a1_2)
a2_1 = re_list1(a2, list(range(len(a2))))
a2_2 = re_list2(a2, list(range(len(a2))))
print(a2_1)
print(a2_2)
colors1 = '#00CED1' #点的颜色
colors2 = '#DC143C'
# plt.scatter(l1_2,l1_1, c=colors1, alpha=0.4, label='1')
# plt.scatter(l2_2,l2_1, c=colors1, alpha=0.4, label='2')
plt.scatter(a1_2,a1_1, c=colors1, alpha=0.4, label='1')
# plt.scatter(l4_2,l4_1, c=colors1, alpha=0.4, label='4')
# plt.scatter(l5_2,l5_1, c=colors1, alpha=0.4, label='5')
plt.scatter(a2_2,a2_1, c=colors2, alpha=0.4, label='2')
# plt.scatter(l7_2,l7_1, c=colors2, alpha=0.4, label='7')
# plt.scatter(l8_2,l8_1, c=colors2, alpha=0.4, label='8')
# plt.scatter(l9_2,l9_1, c=colors2, alpha=0.4, label='9')
# plt.scatter(l10_2,l10_1, c=colors2, alpha=0.4, label='10')
plt.legend( loc = (0.95, 0.9))
plt.show()#这个智障的编辑器