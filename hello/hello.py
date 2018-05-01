# msg = "hello world!"
# print(msg)

# mylist = ['yue','hao','mariah']

# for member in mylist:
#     print("hello, "+member.title())
#     print("we like you,"+member.title())

# mylist.append("keith")
# print(mylist)

# myDict = {'age':5,'height':20,'name':"keith"}
# myDict['age'] = 50
# myDict['height'] = "liu"

# for k,v in myDict.items():
#     print(str(k) +":"+str(v))

# print(myDict)

# #message = input("please input your name:")
# #print("my name is: "+message)

# def GreetWorld(*mygreets):
#     print(mygreets)

# GreetWorld("hello greet"," from ",32)

# from collections import OrderedDict

# myorderdic = OrderedDict()
# myorderdic['k1'] = 45
# myorderdic['k2'] = "hao"
# print(myorderdic)

# with open('hello world file.txt','wr') as file_obj:
#     file_obj.write("hao, hello in Python!")
#     print(file_obj.read())

try:
    print(5/0)
except ZeroDivisionError:
    print("you can't devide by zero")