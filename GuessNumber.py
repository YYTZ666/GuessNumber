#小游戏
import random
import os
import time
import re
from os import system
机会 = random.randint(4,8)
answer = random.randint(1,20)

system("title 猜数1.3Beta -by dyf189")

fw = open("last.txt","a")

#系统检测部分

系统 = os.name
if 系统 == 'nt':
    系统 = 'win'
elif 系统 == 'win32':#win32
      系统 = 'win'
elif 系统 == 'win64':
      系统 = 'win'
elif 系统 == 'linux':
      系统 = 'GNU'
else:
   print('抱歉，您的系统不支持猜数。')
   time.sleep(3)
   exit()

#登录部分

print('登录猜数')
uesr = input('用户名:')

if os.path.exists('uesr.txt'):#第一层如果，检测是否存在“uesr.txt”
    with open('uesr.txt', 'r', encoding='utf-8') as f:
        usdata = f.readline()

        if uesr == usdata:#第二层如果，检测是否与用户名相同
            password = input('密码:')
            if os.path.exists('password.txt'):#第三层，检测是否存在“password.txt”
                with open('password.txt', 'r', encoding='utf-8') as pw:
                    pwdata = pw.readline()

                    if password == pwdata:#第四层，检测password.txt是否与输入内容一致
                       print('欢迎进入猜数')
                    else:
                       print('密码不正确')
                       os.system('pause')
                       exit()
            else:
                with open('password.txt',mode="a",encoding='utf-8') as pw:#如果不存在，创建password.txt并关闭程序（重启）
                    pw.write('12345678')
                    print('未检测到文件，正在创建中......请重启猜数')
                    time.sleep(2)
                    exit()
        else:
            print('此用户名不存在')
            os.system('pause')
            exit()
else:
    with open("uesr.txt", mode='a', encoding='utf-8') as f:
        f.write('admin')
        print('未检测到文件，正在创建中......请重启猜数')
        time.sleep(2)
        exit()


#选择部分

temp = input('_____________________________________\n 请选择模式：\n 1：游玩 2：查看记录 3：用户数据 \n如果不想登录或不想看到此消息？请输入4\n空格默认为1\n')
if temp == '1':
    pass
elif temp == '2':
      print('抱歉，功能未实现')
elif temp == '3':
      print('抱歉，功能未实现')
elif temp == '4':
      print('抱歉，功能未实现')
else:
    pass


#猜数部分

while 机会 > 0:
    temp = input('我们玩个游戏，猜一猜，这个数字是在1到20之间的:')#初始化，输入数值以猜测
    if re.match(r"^-?\d+$", temp):#判断是否为整数值，如果是，进行判断
        guess = int(temp)

        if guess == answer:
            print('厉害啊，你是不是偷看代码了 good!')
            print('我先溜了，不玩了，别想要奖品')
            break
        else:
            if guess < answer:
                print('太小了，大胆一点')
                机会 = 机会-1
            else:
                print('大了，小点')
                机会 = 机会 - 1
    else:#否则进行提示，并结束本次循环
        print('请输入一个整数')
        continue


#结尾清算部分

fw.write('\n结果是:' + str(answer))
fw.close()

print('游戏结束^_^Game Over^_^')
time.sleep(2)
print('----------------------------------')
print('剩余机会:', 机会)
print('答案:' , answer)
print('最后的回答:' , guess)
print('版本:1.4Beta')
print('----------------------------------')

#结尾等待部分

if 系统 == 'win':
    os.system('pause')
elif 系统 == 'GNU':
    os.system('sleep 5')
else:
    exit()



