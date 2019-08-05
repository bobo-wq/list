#! /usr/bin/env python
# encoding: utf8
# author: chenbo
# date:2019/8/5


#列表和元组的使用
# list01=["7","8","9"]
# list_size=list.__sizeof__(list01)
# tuple01=("8","9","10")
# tuple01_size=tuple.__sizeof__(tuple01)
# print("zheshi{}".format(list_size))
# print("zheshisize:{}".format(tuple01_size))
# list01.append(1)
# print(list01)
# list_len=len(list01)
# print(list_len)
# tuple01_len=len(tuple01)
# print(tuple01_len)#注意变量与函数名不能差不多的样子，比如len和tuple_len
# print("数组的个数为：{}".format(list_len))
# print("元组的个数为：{}".format(tuple01_len))
# for i in range(len(list01)):
#     print (list01[i])
# for element in list01:
#     print(element)
# for element in list01:
#     print(element)
# tuple02=(False,4.445,True,False,"String Type")
# number=tuple02.count(True)
# print(number)
# index=tuple02.index(True)
# print(index)
# str01='''
# hello world
# hello kitty
# hello doubleq
# '''
# print(str01)
# print(tuple02[:-1])
# str02="python is a good language"
# str02_split=str02.split(" ")
# print(str02_split,type(str02_split))
# str03=str02.replace("o","0")
# print(str03)
# str03=str03[0:]+"p"
# print(str03)
# str04=str03.strip("p")
# print(str04)
# id,name=998,"bobo"
# print('id:{},name:{}'.format(id,name))
# if 'is' in str04:
#     print("你是帅哥")
# else:
#     print("adh")
# tuple03=list01
# print(tuple03)
#1)代码反转
str01="this is my house"
str02=str01.split(" ")
str02_len=len(str02)
print(str02_len)
x=0
str03=""
for i in range(str02_len):
    x=str02_len-i-1
    #print(str02[x])
    str03=str03+" "+str02[x]
print(str03)
#2)敏感替换
var="you are sb,caonima"
var=var.replace("sb","帅哥")
var=var.replace("caonima","*")
print(var)
# 3)
tuple01=("string","world",1,2,3,4,6,9,10)
list01=list(tuple01)
list02=list01[2:]
print(list02)
# 4)
list01=["string","tuple","list",(1,2,3,4,5),[6,7]]
list01.pop(3)
# tuple02=list01[3]
# list02=list01[4]
# print(type(tuple02),type(list02))
# print(tuple02,list02)
# del list01[3:]
print(list01)
# #list03=list(list02)
# list04=list(tuple02)
# list01.extend(list04)
# list01.extend(list02)
# print(list01)
# list01=[23,12,15,11,29,24,57,21,80,99,45]
# list01_len=len(list01)
# print(type(list01[0]))
# m=list01[0]
# print(type(m),m)
#
# for i in range(0,list01_len):
#
#     for j in range(0,list01_len-1):
#
#         if list01[j]> list01[j+1]:
#             list01[j],list01[j+1]=list01[j+1],list01[j]
#         else:
#             continue
        #temp=int(list01_len[j])
print(list01)








