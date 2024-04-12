from tkinter import *
import Cal_sin_cos_rad
import Cal_sin_cos_degree
import tkinter.messagebox
import math
import main

'''将用户设置下发至交互模块'''
def BeginSimulation(set1, set2_1, set2_2, set2_3):
    global Function, choice1, Angle, Rad
    Function = set1
    choice1 = set2_1
    Angle = set2_2
    Rad = set2_3

def confirm():
    answer = tkinter.messagebox.askokcancel('确认/取消',
                                            '请选择是否重新输入计算')
    if answer:
        root.destroy()
        # import functionchoose1
        main.init_functionchoose()


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

    if choice1 == 1:
        if Function ==1:
            sin_result_deg = Cal_sin_cos_degree.Calculate_sin(int(Angle))
            sin = math.radians(int(Angle))
            sinReal = math.sin(sin)
            sin_difference = abs(sinReal - sin_result_deg)
            lb1 = Label(root, text='角度制：' + setting1 + '(' + Angle + ')' + ' = ' + str(sin_result_deg),
                        font=('微软雅黑', 10), bg='LightGrey')
            lb2 = Label(root, text='结果误差：'+ str(sin_difference) , font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)
            lb2.place(relx=0, y=120, relheight=0.3, width=400)
        if Function ==2:
            cos_result_deg = Cal_sin_cos_degree.Calculate_cos(int(Angle))
            cos = math.radians(int(Angle))
            cosReal = math.cos(cos)
            cos_difference = abs(cosReal - cos_result_deg)
            lb1 = Label(root, text='角度制：' + setting1 + '(' + Angle + ')' + ' = ' + str(cos_result_deg),
                        font=('微软雅黑', 10), bg='LightGrey')
            lb2 = Label(root, text='结果误差：'+ str(cos_difference), font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)
            lb2.place(relx=0, y=120, relheight=0.3, width=400)
        if Function ==3:
            tan_result_deg = Cal_sin_cos_degree.Calculate_tan(int(Angle))
            tan = math.radians(int(Angle))
            tanReal = math.tan(tan)
            tan_difference = abs(tanReal - tan_result_deg)
            lb1 = Label(root, text='角度制：' + setting1 + '(' + Angle + ')' + ' = ' + str(tan_result_deg),
                        font=('微软雅黑', 10), bg='LightGrey')
            lb2 = Label(root, text='结果误差：'+ str(tan_difference), font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)
            lb2.place(relx=0, y=120, relheight=0.3, width=400)

    if choice1 == 2:
        if Function ==1:
            sin_result_rad = Cal_sin_cos_rad.Calculate_sin(int(Rad))
            sinRadreal = math.sin(int(Rad))
            sinRaddifference = abs(sin_result_rad - sinRadreal)
            lb1 = Label(root, text='弧度制：' + setting1 + '(' + Rad + ')' + ' = ' + str(sin_result_rad),
                        font=('微软雅黑', 10), bg='LightGrey')
            lb2 = Label(root, text='结果误差：'+ str(sinRaddifference), font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)
            lb2.place(relx=0, y=120, relheight=0.3, width=400)
        if Function ==2:
            cos_result_Rad = Cal_sin_cos_rad.Calculate_cos(int(Rad))
            cosRadreal = math.cos(int(Rad))
            cosRaddifference = abs(cos_result_Rad - cosRadreal)
            lb1 = Label(root, text='弧度制：' + setting1 + '(' + Rad + ')' + ' = ' + str(cos_result_Rad),
                        font=('微软雅黑', 10), bg='LightGrey')
            lb2 = Label(root, text='结果误差：'+ str(cosRaddifference), font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)
            lb2.place(relx=0, y=120, relheight=0.3, width=400)
        if Function ==3:
            tan_result_Rad = Cal_sin_cos_rad.Calculate_tan(int(Rad))
            tanRadreal = math.tan(int(Rad))
            tanRaddifference = abs(tan_result_Rad - tanRadreal)
            lb1 = Label(root, text='弧度制：' + setting1 + '(' + Rad + ')' + ' = ' + str(tan_result_Rad),
                        font=('微软雅黑', 10), bg='LightGrey')
            lb2 = Label(root, text='结果误差：'+ str(tanRaddifference), font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)
            lb2.place(relx=0, y=120, relheight=0.3, width=400)

    '''设置回退任务按钮'''
    performbtn = Button(root, text='确认', activebackground='gray',command = confirm)
    performbtn.place(relx=0.2, y=260, relheight=0.1, width=200)
    root.mainloop()
