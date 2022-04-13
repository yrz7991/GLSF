import madmom
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
# a1_2 = list(range(1, len(a1_1)+1)






# # import openpyxl
# # wb = openpyxl.load_workbook('feature.xlsx')
# # tempo = wb.worksheets[0]
# # rms = wb.worksheets[1]
# # zero = wb.worksheets[2]
# # for n in range(1, 3):
# #     sum = 0
# #     ind = 2
# #     while True:
# #         if not tempo.cell(n, ind).value or not tempo.cell(1, ind).value:
# #             break
# #         else:
# #             sum += (tempo.cell(n, ind).value - tempo.cell(1, ind).value) ** 2
# #         ind = ind + 1
# #         pass
# # print(sum)
# # print(type(tempo.cell(1, 100).value))
# #
# # # 创建工作簿
# # ws = openpyxl.Workbook()
# # sheet = ws.active
# # ws.create_sheet(index=1, title='rms1')
# # # 保存工作表
# # ws.save("recommend.xlsx")
# # l = [0, [0]]
# # # print(l[0])
# # # l[0] = [1, 2]
# # # print(l[0])
# # # l.append(1)
# # # print(l)
# # # print(l[0][0])
# # del l[0]
# # # print(l[1])
# # # print(l[1] == [0])
# # print(l)
# import librosa
# import os
# import openpyxl
# path_filename = "./music/09/010377.mp3"
# y, sr = librosa.load(path_filename)
# tempo, beats = librosa.beat.beat_track(y=y, sr=sr)  # 节奏和与节拍对应的帧
# time = librosa.frames_to_time(beats, sr=sr)  # 将与节拍对应的帧转换为秒
# print(tempo)
# print(beats)
# print(time)
# tempo_be = []
# i = 0
# while i < len(time) - 1:
#     # num_m = num_m + 1
#     con_time = time[i + 1] - time[i]
#     if i == 0:
#         set_time = 0
#         pass
#     else:
#         set_time = time[i - 1]
#     y_be, sr_be = librosa.load(path_filename, offset=set_time, duration=con_time)
#     tempo_be_c, beats_be_c = librosa.beat.beat_track(y=y_be, sr=sr_be)
#     # sheet_tempo.cell(num_m, num - 1).value = 'tempo'
#     tempo_be.append(tempo_be_c)
#     i = i + 1
#     pass
# print(tempo_be)
# li =[1, 3, 2, 4, 5, 6]
# a = list(reversed(li))
# print (a)
# print(li)
