#! usr/env/bin
#author: chenbo
#encoding study
#usage: 课堂练习
# 1)求100以内的素数
# for i in range (1,101):
#      if i < 9 and i % 2==1:
#          print(i)
#      elif i % 2 == 0 or i % 3 == 0 or i % 5 ==0 or i % 7==0 :
#          continue
#      else:
#          print(i)
# 2)求输入两个数的和
# a=input("please input:")
# b=input("please input:")
# c=int(a)+int(b)
# print(c)
# 3)判断两个数的大小
# a=input("please input :")
# b=input("please input :")
# if int(a)>int(b) :
#     print(a+">"+b)
# elif int(a)==int(b) :
#     print(a+"="+b)
# else:
#     print(a+"<"+b)
# 4）求两个数的最大公约数
# a=input("please int:")
# m=int(a)
# b=input("please input:")
# n=int(b)
# k=1
# for i in range(1,m+1):
#     if (i%2 ==0 or i%3 ==0 or i%5 ==0 or i%7 ==0) and m%i ==0:
#             if n%i ==0:
#                 k=i
# print(k)
# 5）求两个数的最小公倍数
# a=input("please input:")
# m=int(a)
# b=input("please input:")
# n=int(b)
# z=0
# z1=0
# x=0
# x1=0
# y=0
# y1=0
# j=0
# j1=0
# while True:
#     if m%2 ==0 :
#         z=z+1
#         m=m/2
#     if m%3 ==0 :
#         x=x+1;
#         m=m/3
#     if m%5 ==0 :
#         y=y+1
#         m=m/5
#     if m%7 ==0 :
#         j=j+1
#     if m==1 :
#         break
# while True:
#        if n%2 == 0:
#            z1=z1+1
#            n=n/2
#        if n%3 == 0:
#            x1=x1+1
#            n=n/3
#        if n%5 == 0:
#            y1=y1+1
#            m1=m1/5
#        if n%7 ==0 :
#            j1=j+1
#        if n==1 :
#            break
# mm=(2**max(z1,z))*(3**max(x1,x))*(5**max(y1,y))*(7**max(j1,j))
# print(mm)
# 6)求1到100的和
# m=0
# for i in range(1,100):
#     m=m+i
#     i=i+1
# print(m)
#7)求1到10的乘积
# m=1
# for i in range(1,10):
#     m=m*i
#     i=i+1
# print(m)






#     else
#         print(i)


# user_input_02 = int(input("please input your number: "))
# if 20 < user_input_02 and user_input_02 < 30:
#     print("The number location 20 of 30 between.")
# elif 30 > user_input_02 or user_input_02 > 40:
#     print("The number location all.")
# else:
#     print("The number is: ", user_input_02)




