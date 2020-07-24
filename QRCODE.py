from tkinter import *
from tkinter import messagebox,Toplevel
import pyqrcode
import  os
root = Tk()
root.geometry('570x400')
root.title('QR Generator')
root.configure(bg='yellow')
root.wm_iconbitmap('QR.ico')
##Function
def Generate_QR():
    QR_Name=QR_Name_ENTRY_BOX.get()
    QR_ID=QR_ID_ENTRY_BOX.get()
    QR_MESSAGE=QR_MESSAGE_ENTRY_BOX.get()
    Message_QR= 'Name : '+QR_Name+'\n'+'Id : '+QR_ID+'\n'+'Message : '+QR_MESSAGE
    url=pyqrcode.create(Message_QR)
    path = r'C:\Users\Shivam\Desktop\QR'
    cc = '{}\{}{}.png'.format(path,QR_ID,QR_Name)
    ll= os.listdir(path)
    if('{}{}.png'.format(QR_ID,QR_Name) in ll):
        messagebox.showinfo('Notification','Please choose another id or name')
    else:
        url.png(cc,scale=8)
        mes= 'QR code saves as :'+QR_ID+QR_Name+'.png'
        QR_NOTIFICATION_Mlabel.configure(text=mes)
        rs = messagebox.askyesno('Notification','QR code is generated and want to see it then yes :')
        if(rs == True):
            top = Toplevel()
            top.geometry('400x400')
            top.configure(bg='white')
            img = PhotoImage(file=cc)
            label1=Label(top,image=img,bg='white')
            label1.place(x=10,y=10)
            top.mainloop()


def Clear_id():
    QR_ID_ENTRY_BOX.delete(0,'end')
    QR_MESSAGE_ENTRY_BOX.delete(0,'end')
    QR_Name_ENTRY_BOX.delete(0,'end')
    QR_NOTIFICATION_Mlabel.configure(text='')

def Quit_root():
    res = messagebox.askokcancel('Notification','Are you sure you want to quit?')
    if(res == True):
        root.destroy()
    else:
        pass








##Labels
QR_ID_label = Label(master=root,text='Enter Your Id: ',bg='red',width=20,height=2,
                    font=('times',12,'italic bold'))
QR_ID_label.place(x=10,y=20)

QR_Name_label = Label(master=root,text='Enter Your Name: ',bg='red',width=20,height=2,
                    font=('times',12,'italic bold'))
QR_Name_label.place(x=10,y=80)

QR_Message_label = Label(master=root,text='Enter Your Message: ',bg='red',width=20,height=2,
                    font=('times',12,'italic bold'))
QR_Message_label.place(x=10,y=140)

QR_NOTIFICATION_label = Label(master=root,text='Notification',bg='red',width=10,height=2,
                    font=('times',15,'bold underline'))
QR_NOTIFICATION_label.place(x=10,y=350)

QR_NOTIFICATION_Mlabel = Label(master=root,text='',bg='red',width=30,height=2,
                    font=('times',15,'bold'))
QR_NOTIFICATION_Mlabel.place(x=200,y=350)




###Entry Box
QR_ID_ENTRY_BOX = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'italic bold'))
QR_ID_ENTRY_BOX.place(x=250,y=20)

QR_Name_ENTRY_BOX = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'italic bold'))
QR_Name_ENTRY_BOX.place(x=250,y=80)

QR_MESSAGE_ENTRY_BOX = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'italic bold'))
QR_MESSAGE_ENTRY_BOX.place(x=250,y=140)

##Button
Generate_QRimage = Button(master=root,text='Generate',width=15,font=('times',10,' bold'),bd=10,activebackground='yellow'
                          ,bg='red',command=Generate_QR)
Generate_QRimage.place(x=10,y=250)

CLEAR_ID_NAME = Button(master=root,text='Clear',width=15, font=('times', 10, ' bold'), bd=10,activebackground='yellow'
                          ,bg='red',command=Clear_id)
CLEAR_ID_NAME.place(x=210,y=250)

QUIT_root_Button = Button(master=root,text='Quit',width=15,font=('times',10,' bold'),bd=10,activebackground='yellow'
                          ,bg='red',command=Quit_root)
QUIT_root_Button.place(x=410,y=250)

###Hover Effect
def Generate_QRimageEnter(e):
    Generate_QRimage['bg'] = 'purple2'
def Generate_QRimageLeave(e):
    Generate_QRimage['bg'] = 'red'

def CLEAR_ID_NAMEEnter(e):
    CLEAR_ID_NAME['bg'] = 'purple2'
def CLEAR_ID_NAMELeave(e):
    CLEAR_ID_NAME['bg'] = 'red'

def QUIT_root_ButtonEnter(e):
    QUIT_root_Button['bg'] = 'purple2'
def QUIT_root_ButtonLeave(e):
    QUIT_root_Button['bg'] = 'red'




Generate_QRimage.bind('<Enter>',Generate_QRimageEnter)
Generate_QRimage.bind('<Leave>',Generate_QRimageLeave)

CLEAR_ID_NAME.bind('<Enter>',CLEAR_ID_NAMEEnter)
CLEAR_ID_NAME.bind('<Leave>',CLEAR_ID_NAMELeave)

QUIT_root_Button.bind('<Enter>',QUIT_root_ButtonEnter)
QUIT_root_Button.bind('<Leave>',QUIT_root_ButtonLeave)









root.mainloop()

