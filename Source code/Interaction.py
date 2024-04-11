from tkinter import *
import Calculate_arctan
#import Cal_sin_cos_rad
#import Cal_sin_cos_degree
import tkinter.messagebox
import numpy as np

'''将用户设置下发至交互模块'''
def BeginSimulation(set1, set2_1, set2_2, set2_3):
    global Function, choice1, Angle, Radian
    Function = set1
    choice1 = set2_1
    Angle = set2_2
    Radian = set2_3

def Show3():
    global root
    root = Tk()
    root.title('计算信息')  # 标题
    lb = Label(root, text=' 计算结果', \
                        bg='#ADD8E6', \
                       fg='black', \
                        font=('Times', 15), \
                        width=60, \
                        height=1, \
                        relief=SUNKEN)
    lb.pack()
    root.geometry('400x300')
    '''显示选择函数'''
    dic = {1: 'sin',
           2: 'cos',
           3: 'tan',
           4: 'arcsin',
           5: 'arctan',
           }
    setting1 = dic.get(Function)

    arctan_result = Calculate_arctan.Calculate_arctan(int(Angle))
    arctan_result_rad = arctan_result[0]
    arctan_result_deg = arctan_result[1]


    if choice1 == 1:
        lb1 = Label(root, text='角度制：' + setting1 + '(' + Angle + ')' + ' = ' + str(result_deg), font=('微软雅黑', 10), bg='LightGrey')
        lb2 = Label(root, text='结果误差：', font=('微软雅黑', 10), bg='LightGrey')
        lb1.place(relx=0, y=50, relheight=0.3, width=400)
        lb2.place(relx=0, y=120, relheight=0.3, width=400)
    if choice1 == 2:
        lb1 = Label(root, text='弧度制：' + setting1 + '(' + Radian+ ')' + ' = ' + str(arctan_rad), font=('微软雅黑', 10), bg='LightGrey')
        lb2 = Label(root, text='结果误差：', font=('微软雅黑', 10), bg='LightGrey')
        lb1.place(relx=0, y=50, relheight=0.3, width=400)
        lb2.place(relx=0, y=120, relheight=0.3, width=400)
    root.mainloop()

#def resultshow1():
#def resultshow2():
