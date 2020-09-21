# a = [3,'和'] # 列表list 可修改 有序
# print(a)
# a[1]='好'
# print(a)
# b = (1,13)   # 元组tuple 不可修改 有序
# print(b)
# c = {2,23}   # 集合set 可修改 不可重复 无序
# print(c)
# d = {"姓名":"小明"} # 字典dict key不可重复 无序
# print(d)
#
# a = 1
# b = '15'
# print (str(a)+b)
# a = 15
# b ='20'
# print (a+int(b))
#
# a = '123'
# print (list(a))
# print (tuple(a))
# print (set(a))
#
# 算数运算
# 比较运算
# 逻辑运算 and  or  not
# a = 1
# b = 4
# c = 7
# print(c>b and c>a)
# 成员运算 in  not in
# a = [1,2,3]
# b = (4,5,6)
# c = {7,8,9}
# print(7 in c)
# 如果我有500万，买两碗豆浆，喝一碗扔一碗；如果没钱，还是洗洗睡吧
# money = 600
# if (money >= 500):
#     print("买两碗豆浆，喝一碗扔一碗")
# else:
#     print("洗洗睡吧")

# money = 1000000000000
# if (money < 300 ):
#     print("坐火车")
# elif (money < 600 ):
#     print("坐高铁")
# elif (money < 1000 ):
#     print("坐飞机")
# else:
#     print("开大炮")

# for i in [1,2,3,4]:
#     print("李越是只猪")
#     print("李越是蜘蛛")
# for i in range(100):
#     print("李越是只猪")
#     print("李越是蜘蛛")
# for i in range(0,101,5):
#     print(i)
# while True:
#     print("李越是蜘蛛")
# for i in range(1,10,1):
#     if (i == 4):
#         continue
#     print(i)
# 计算1-100的和 1+2+3+4....+100 =
# s = 0
# for i in range(1,101):
#     s+=i
# print(s)

# def div():
# 	a = 10
# 	b = 2
# 	if b == 0:
# 		print("被除数不能为0")
# 		return
# 	print(a / b)
#
# div()
#
# def div(a,b):
# 	if b == 0:
# 		print("被除数不能为0")
# 		return
# 	print(a / b)
#
# div(10,3)
#
# def div():
# 	a = 10
# 	b = 2
# 	if b == 0:
# 		print("被除数不能为0")
# 		return
# 	return a / b
# print(div())
#
# def div(a,b):
# 	if b == 0:
# 		print("被除数不能为0")
# 		return
# 	return a / b
# print(div(10,0))

# def div(a=10,b=2):
# 	if b == 0:
# 		print("被除数不能为0")
# 		return
# 	return a / b
#
# print(div())
# print(div(20))
# print(div(20,9))
# for i in range(1,10):
#      for j in range (1,i+1):
#         print(j,'x',i,'=',i*j,end='\t')
#      print()

# c = 2
# def we():
#     global c
#     c = 20
# we()
# print(c)
#
# a='1234567890'
# print(a[2:5])
# print(a[-4:])
# print(a[8:])
# print(a[2])
# print(a[::-1])
# print(a[::3])
# b=" khkkkllss  "
# print(b.strip())
# print(b.lstrip())
# print(b.rstrip())


# 面向对象编程
# def s(a,b):
#     return a+b
#
# print(s(10,20))


# 对变量和方法的打包

# 类和对象
# 创建一个类
# class str_demo():
#
#     s = "类变量" # 类变量  类加载到内存中就会被创建   类被销毁时，同步被销毁
#
#     def replace(self):
#         self.a = "实例变量" # 实例变量 调用该变量创建的实例方法时 对象被销毁时同步被销毁掉
#         b = "局部变量"  # 局部变量  方法运行结束就被销毁
#         print("字符串替换")
#
#     def split(self):
#         print(str_demo.s) # 访问类变量
#         print(__class__.s) # 访问类变量(推荐)
#         print(self.s) # 不推荐
#         print(self.a) # 访问实例变量



# 实例化
# sd = str_demo() # 实例化 sd就是一个对象
# sd.s = "hello"
# sd.replace()
# sd.split()

# 类外部访问
# 类变量
# print(str_demo.s) # 通过类名直接访问（推荐）
#
# # 实例变量
# sd = str_demo() # 实例化成一个对象
# sd.replace() # 调用实例方法创建 实例变量
# print(sd.a) # 通过对象访问实例变量
# # 通过对象和类调用类变量
# print(sd.s) # 可以通过对象访问类变量（不推荐） 通过对象调用属性的搜索顺序 实例变量-》类变量
# sd.s="s是一个实例变量" # 创建了一个实例变量
# print(sd.s) # 访问实例变量s
# print(str_demo.s) # 访问类变量s
# 类内部访问实例变量和类变量
# sd = str_demo()
# sd.replace()
# sd.split()

# sd = str_demo()
# st = str_demo()
# str_demo.s="str_demo"
# sd.a = "sd"
# st.a = "st"
# print(sd.a)
# print(st.a)
#
# print(sd.s)
# print(st.s)


# 类方法&实例方法&静态方法&魔法方法
# class str_demo():
#     b = "类变量"
#     # 不需要显式调用，程序自动调用的
#     def __init__(self):
#         self.a="实例变量"
#         print("魔法方法")
#         self.replace() # 在实例方法中调用实例方法
#         __class__.split() # 在实例方法中调用类方法
#         __class__.static()  # 在实例方法中调用静态方法
#         self.static()  # 在实例方法中调用静态方法
#
#
#     # 实例方法
#     def replace(self): # self代表当前对象本身
#         print("实例方法")
#
#
#     @classmethod
#     def class_method(cls):# cls 代表当前类本身
#         # 不能调用实例方法
#         cls.split() # 调用类方法
#         cls.static()# 调用静态方法
#
#
#     @classmethod # 装饰器
#     def split(cls):
#         print("类方法")
#
#     @staticmethod
#     def static_method():
#         # 不能调用实例方法
#         __class__.split()  # 调用类方法
#         __class__.static()  # 调用静态方法
#     @staticmethod
#     def static():
#         print("静态方法")



# 类外部调用方法
# str_demo.split() # 调用类方法
# str_demo().replace() # 通过对象调用实例方法
# str_demo.static() # 通过类名调用静态方法
# str_demo().static() # 通过对象调用静态方法
# str_demo() # 调用__init__魔法方法

# 在类内部调用方法
# str_demo()# 实例方法
# str_demo.class_method()# 类方法
# str_demo.static_method() # 静态方法

# 1、编写一个返回随机手机号的方法
# import random
# a = random.choices(("130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","166","171","172","173","175","176","177","178","181","182","183""184","185","186","187","188","189","198","199"),k=1)
# b = random.choices("0123456789",k=8)
# c = (a+b)
# print(c)
# print("".join(c))
# 2、编写一个返回指定长度和内容的随机字符串方法
# import random
# a = random.choices("dhhd184f187f9djlj",k=6)
# print(a)
# print("".join(a))
# 3、编写一个返回随机姓名的方法
# import random
# a = random.choices("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张",k=1)
# b = random.choices(("哈喽","回来","十个","色粉","广告","尬","按个","感叹"),k=1)
# c = (a+b)
# print(c)
# print("".join(c))

# def case1(a,b=2):
#     print(a)
#     print(b)
#     print("这是一个测试用例1")
#
#
# print("执行用例之前",10,20)
# r=case1(10,20)
# print("用例执行之后",r)

# print("执行用例之前",2,4)
# r=case2(2,4)
# print("用例执行之后",r)
#
#
# def log(func,*args,**kwargs):
#     print("执行用例之前",args,kwargs)
#     r = func(*args,**kwargs)
#     print("用例执行之后", r)
#
#
# log(case1,10,20)
# log(case2,1,2)
#
#
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,'=',i*j,end='\t')
#     print()
# c = 10 # 全局变量

# d={"name":"王小锤"}
# def ddd():
#     d["name"]="王大锤"
#
# ddd()
# print(d)

# class str_demo():
#
#     s = "类变量" # 类变量  类加载到内存中就会被创建   类被销毁时，同步被销毁
#
#     def replace(self):
#         self.a = "实例变量" # 实例变量 调用该变量创建的实例方法时 对象被销毁时同步被销毁掉
#         b = "局部变量"  # 局部变量  方法运行结束就被销毁
#         print("字符串替换")
#
#     def split(self):
#         print(str_demo.s) # 访问类变量
#         print(__class__.s) # 访问类变量(推荐)
#         print(self.s) # 不推荐
#         print(self.a) # 访问实例变量


# 实例化
# sd = str_demo() # 实例化 sd就是一个对象
# sd.s = "hello"
# sd.replace()
# sd.split()
try:
     a = open ("module_1.py","r")
     print(1/2)
except (FileNotFoundError,ZeroDivisionError) as c:
    print(c)
    print("程序执行遇到了问题")
    print("重新打开文件")
else:
    print("程序无报错时运行")
finally:
    print("程序有无报错都运行")
print("文件已打开")
