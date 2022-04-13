# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 15:57:43 2021

@author: yrz
"""

import pandas as pd
import numpy as np
import time
#计算两个元素之间方差的函数
def getstd2(data,name1,name2):
    data1 = np.array(data[name1].dropna())
    data2 = np.array(data[name2].dropna())
    length = min(len(data1),len(data2))
    #两个元素对应数据相减然后平方求和
    return sum(pow(data1[:length]-data2[:length],2))/length

def prd(io = 'feature.xlsx',weight_sheet = [1,1,1],weight = [1,1,1,1,1,1,1,1] ,first_data_name = '001039.mp3'):
    datas = []
    for i in range(len(weight_sheet)):
        #读取一张工作表，并将行列倒置，将第一行（元素名）作为表头
        dt = pd.read_excel(io,header = None,sheet_name = i).T
        dt.columns = dt.loc[0]
        dt = dt.drop(labels = 0,axis = 0)
        data_name = dt.columns
        datas.append(dt)       
    #设定一个list负责记录结果顺序，一个list负责记录剩余元素
    result = []
    result.append(np.argwhere(data_name == first_data_name)[0,0])
    remain = list(range(len(data_name)))
    remain.remove(np.argwhere(data_name == first_data_name)[0,0])
    while(len(remain)!=0):
    #计算剩余元素和其他元素之间的距离
        std = []
        for i in range(len(data_name)):
            if i in remain:
                sr = []
                for data in datas:
                    stds = []    
                    for j in range(len(result)):    
                        stds.append(getstd2(data,data_name[i],data_name[j]))
                    length = min(len(stds),len(weight))
                    #方差*权重并求和
                    stds = sum(np.array(stds)[(len(stds)-length):]*weight[:length])
                    # stds = sum(np.array(stds)[(len(stds) - length):] * list(reversed(weight[:length])))
                    sr.append(stds)
                #每张表的结果*权重并求和
                sr = sum(np.array(sr)*np.array(weight_sheet))
                std.append(sr)
        #找距离最小的元素加入结果，并将其从剩余元素中移除
        std = np.argmin(np.array(std))
        result.append(remain[std])
        remain.remove(remain[std])
    #把元素的index转化为元素名
    result_final = []
    for i in result:
        result_final.append(data_name[i])
        #result_final.append(i)
    return result_final

if __name__ == '__main__':
    # print(prd(weight = [1, 233, 1, 1, 0, 1, 0, 0]))
    # print(prd(weight = [1, 1, 1, 1, 1, 1, 1, 1]))
    # print(prd(weight = [1, 0.6, 0.5, 0.3, 0.1, 0.08, 0.01, 0.007]))
    # print(prd(weight_sheet = [0.001, 1000, 1]))
    # print(prd(first_data_name = '001039.mp3'))
    # sort = prd(weight_sheet = [0.009, 1, 1],weight = [1, 0.8, 0.5, 0.3, 0.1, 0.08, 0.01, 0.007])
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5, 0.45, 0.41, 0.37, 0.35], first_data_name = '000002.mp3')  # 1/x**0.5
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5,
    #                                                0.45, 0.41, 0.37, 0.35,0.33,0.32,0.3,0.29,
    #                                                0.28,0.27,0.26,0.25,
    #                                                0.24,0.24,0.23,0.22], first_data_name = '000002.mp3')  # 1/x**0.5
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5,
    #                                                 0.45, 0.41, 0.37, 0.35,0.33,0.32,0.3,0.29,
    #                                                 0.28,0.27,0.26,0.25,
    #                                                 0.24,0.24,0.23,0.22],
    #             first_data_name='001039.mp3')  # 1/x**0.5
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5,
    #                                                 0.45, 0.41, 0.37, 0.35,0.33,0.32,0.3,0.29,
    #                                                 0.28,0.27,0.26,0.25,
    #                                                 0.24,0.24,0.23,0.22],
                # first_data_name='003263.mp3')  # 1/x**0.5
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5,
    #                                                 0.45, 0.41, 0.37, 0.35,0.33,0.32,0.3,0.29,
    #                                                 0.28,0.27,0.26,0.25,
    #                                                 0.24,0.24,0.23,0.22],
    #             first_data_name='004013.mp3')  # 1/x**0.5
    # t1 = time.time()
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5,
    #                                                 0.45, 0.41, 0.37, 0.35,0.33,0.32,0.3,0.29,
    #                                                 0.28,0.27,0.26,0.25],
    #             first_data_name='000853.mp3')  # 1/x**0.5
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5,
    #                                                 0.45, 0.41, 0.37, 0.35,0.33,0.32,0.3,0.29,
    #                                                 0.28,0.27,0.26,0.25,
    #                                                 0.24,0.24,0.23,0.22],
    #             first_data_name='006329.mp3')  # 1/x**0.5
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5,
    #                                                 0.45, 0.41, 0.37, 0.35,0.33,0.32,0.3,0.29,
    #                                                 0.28,0.27,0.26,0.25,
    #                                                 0.24,0.24,0.23,0.22],
    #             first_data_name='007374.mp3')  # 1/x**0.5
    # t1 = time.time()
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5,
    #                                                 0.45, 0.41, 0.37, 0.35,0.33,0.32,0.3,0.29,
    #                                                 0.28,0.27,0.26,0.25,
    #                                                 0.24,0.24,0.23,0.22],
    #             first_data_name='009555.mp3')  # 1/x**0.5
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0, 0, 0, 0, 0, 0, 0],
    #             first_data_name='009557.mp3')  # 1/x**0.5
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5,
    #                                                 0.45, 0.41, 0.37, 0.35,0.33,0.32,0.3,0.29,
    #                                                 0.28,0.27,0.26,0.25,
    #                                                 0.24,0.24,0.23,0.22],
    #             first_data_name='011019.mp3')  # 1/x**0.5
    # sort = prd(weight_sheet=[, 1, 1], weight = [1, 1, 1, 1, 1, 1, 1, 1])
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0, 0, 0, 0, 0, 0, 0])
    # sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5, 0.45, 0.41, 0.37, 0.35],
                # first_data_name='Memme - Gold Town.mp3')  # 1/x**0.5
    sort = prd(weight_sheet=[0.009, 1, 1], weight=[1, 0.71, 0.58, 0.5, 0.45, 0.41, 0.37, 0.35],
                first_data_name = '1005376.mp3')  # 1/x**0.5
    for i in range(len(sort)):
        print(sort[i],i+1)
    # t2 = time.time()
    import openpyxl
    wb = openpyxl.load_workbook('feature.xlsx')
    tempo = wb.worksheets[0]
    li = [0 for x in range(0, len(sort))]
    for i in range(len(sort)):
        for j in range(len(sort)):
            if tempo.cell(i+1, 1).value == sort[j]:
                li[i] = j+1
    print(li)
    for i in range(len(sort)):
        sort[i] = int(sort[i][:-4])
    print(sort)
    # print(t1)
    # print(t2)
    # print(t2-t1)