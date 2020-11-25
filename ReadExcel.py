# coding=utf-8

import xlrd
import pandas as pd
import numpy as np

df=pd.read_excel('a_2.xls')
height,width = df.shape
print(height,width,type(df))

x = np.zeros((height,width))
nameList = []
personIdList = []
phoneList = []
apptime = []
arrtime = []
enttime = []
sitId = []
for i in range(0,height):
    tpName = df.values[i][0]
    a1 = tpName.replace(tpName[0],'*')
    tpId = df.values[i][1]
    a2 = tpId.replace(tpId[14:18],'****')
    tpphone = str(df.values[i][2])
    a3 = tpphone.replace(tpphone[7:11],'****')
    tpapp = df.values[i][3]
    tparr = df.values[i][4]
    tpend = df.values[i][5]
    # tpsit = df.values[i][6]
    nameList.append(str(a1))
    personIdList.append(str(a2))
    phoneList.append(str(a3))
    apptime.append(str(tpapp))
    arrtime.append(str(tparr))
    enttime.append(str(tpend))
    # sitId.append(str(tpsit))  
    print(i)



# name_to_list = {'姓名': nameList,'身份证':personIdList,'手机号':phoneList,
#                 '预约日期': apptime, '预约到馆时间':arrtime,'入馆时间':enttime,'座位号':sitId}
name_to_list = {'姓名': nameList,'身份证':personIdList,'手机号':phoneList,
                '预约日期': apptime, '预约到馆时间':arrtime,'入馆时间':enttime}
df = pd.DataFrame(data=name_to_list)
df.to_csv('sheet_2.csv', encoding='utf_8_sig')
