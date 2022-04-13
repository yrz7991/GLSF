import math

rel1 = 1
def dcg(list1,list2):
    rel = [0 for x in range(0,20)]
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            rel[i] = 1
        else:
            rel[i] = 0
    sum = 0
    for n in range(len(rel)):
        sum += rel[n] / math.log(n + 2, 2)
        # if n == 0:
        #     continue
        # else:
        #     sum += rel[n] / math.log(n+1,2)
    # print(sum)
    # return rel1 + sum
    return sum

def idcg(list1):
    sum = 0
    for i in range(len(list1)):
        sum += 1 / math.log(i + 2, 2)
        # if i == 0:
        #     continue
        # else:
        #     sum += 1 / math.log(i+1,2)
    # print(sum)
    # return 1 + sum
    return sum

l1 =[1, 15, 8, 6, 10, 12, 19, 4, 14, 9, 11, 5, 2, 17, 16, 13, 7, 3, 20, 18]
# l2 = [1,3, 4,6,10,13,15,7,16,5,14,11,9,17,12,19,2,8,18,20]
l2 =[1,10,16,18,20,7,14,13,12,15,17,6,3,9,2,8,11,4,5,19]
# l2 = [1, 3, 20,4,6,11,12,10,9,7,16,15,14,19,5,13,2,8,18,17]

ndcg = dcg(l1,l2)/idcg(l1)
print(ndcg)