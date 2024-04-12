from tkinter import *
import Calculate_arctan
import Arcsin_calc
import tkinter.messagebox


'''将用户设置下发至交互模块'''

def BeginSimulation_arc(set1, set2):
    global Function,Num
    Function = set1
    Num = set2

def confirm():
    answer = tkinter.messagebox.askokcancel('确认/取消',
                                            '请选择是否重新输入计算')
    if answer:
        root.destroy()
        import functionchoose1
        functionchoose1.init_functionchoose()


def Show4():
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
    root.geometry('400x400')
    '''显示选择函数'''
    dic = {1: 'sin',
           2: 'cos',
           3: 'tan',
           4: 'arcsin',
           5: 'arctan',
           }
    setting1 = dic.get(Function)

    if Function == 4:
        arcsin_result = Arcsin_calc.Arcsin_calc(int(Num))
        arcsin_result_Rad = arcsin_result[0]
        arcsin_result_deg = arcsin_result[1]
        lb1 = Label(root, text='弧度制：' + setting1 + '(' + Num + ')' + ' = ' + str(arcsin_result_Rad),
                        font=('微软雅黑', 10), bg='LightGrey')
        lb2 = Label(root, text='角度制：' + setting1 + '(' + Num + ')' + ' = ' + str(arcsin_result_deg),
                    font=('微软雅黑', 10), bg='LightGrey')
        lb3 = Label(root, text='结果误差：', font=('微软雅黑', 10), bg='LightGrey')
        lb1.place(relx=0, y=50, relheight=0.3, width=400)
        lb2.place(relx=0, y=120, relheight=0.3, width=400)
        lb3.place(relx=0, y=190, relheight=0.3, width=400)
    if Function ==5:
        arctan_result = Calculate_arctan.Calculate_arctan(int(Num))
        arctan_result_Rad = arctan_result[0]
        arctan_result_deg = arctan_result[1]
        lb1 = Label(root, text='弧度制：' + setting1 + '(' + Num + ')' + ' = ' + str(arctan_result_deg),
                    font=('微软雅黑', 10), bg='LightGrey')
        lb2 = Label(root, text='角度制：' + setting1 + '(' + Num + ')' + ' = ' + str(arctan_result_Rad),
                        font=('微软雅黑', 10), bg='LightGrey')
        lb3 = Label(root, text='结果误差：', font=('微软雅黑', 10), bg='LightGrey')
        lb1.place(relx=0, y=50, relheight=0.3, width=400)
        lb2.place(relx=0, y=120, relheight=0.3, width=400)
        lb3.place(relx=0, y=190, relheight=0.3, width=400)

    '''设置回退任务按钮'''
    performbtn = Button(root, text='确认', activebackground='gray',command = confirm)
    performbtn.place(relx=0.25, y=350, relheight=0.1, width=200)
    root.mainloop()
