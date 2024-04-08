from tkinter import *
import tkinter.messagebox
from tkinter.simpledialog import *
import Interaction

'''第二个界面的数据信息'''
def valueget():
    Interaction.BeginSimulation(setting1, var1_1.get(), angle.get(), radian.get())
def confirmcalculate():
    answer = tkinter.messagebox.askokcancel('Confirm/Cancel',
                                            'Data has saved successfully, please select Confirm or Cancel.')
    if answer:
        valueget()
        root.destroy()
        Interaction.Show3()
def choicejudge():
    global angle
    global number
    global radian
    choice = var1_1.get()
    if choice == 1:
        angle = Entry(width=50)
        angle.place(relx=0.22, y=100, relheight=0.05, width=200)
        radian = Entry(state='disable')
        radian.place(relx=0.22, y=180, relheight=0.05, width=200)
    if choice == 2:
        angle = Entry(state='disable')
        angle.place(relx=0.22, y=100, relheight=0.05, width=200)
        radian = Entry(width=50)
        radian.place(relx=0.22, y=180, relheight=0.05, width=200)

def Show2(window,set1):
    global root
    global setting1
    global var1_1
    setting1 = set1
    root = window
    root.title('输入')#标题
    root.geometry('350x350')  # 设置窗口大小
    var1_1 = IntVar()
    '''标题'''
    lb1 = Label(root, text='参数输入', font=('Times', 15), bg='#ADD8E6',relief=SUNKEN,anchor='center')
    lb1.place(relx=0, y=0, relwidth=1, relheight=0.1)

    btn1 = Radiobutton(root, text='角度', bg="#ADD8E6", activebackground='gray', variable=var1_1,
                       value=1, command = choicejudge)
    btn1.place(relx=0.22, y=80, relheight=0.05, width=200)

    btn2 = Radiobutton(root, text='弧度', bg="#ADD8E6", activebackground='gray', variable=var1_1,
                       value=2, command = choicejudge)
    btn2.place(relx=0.22, y=160, relheight=0.05, width=200)

    '''设置计算任务按钮'''
    perform = Label(root, text='Calculate', font=('微软雅黑', 10), bg='#ADD8E6')
    perform.place(relx=0.22, y=240, relheight=0.05, width=200)
    performbtn = Button(root, text='计算', activebackground='gray', command=confirmcalculate)
    performbtn.place(relx=0.22, y=260, relheight=0.05, width=200)
    root.mainloop()




