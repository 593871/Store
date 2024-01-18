import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as mb
def uyuyu():
    a = picture_1_var.get()
    b = picture_2_var.get()
    c = picture_3_var.get()
    d = picture_4_var.get()
    v = ''
    if a == 1:
       v += 'Яблоко'
    if b == 1:
        v += 'Кот'
    if c == 1:
        v += 'Пляж'
    if d == 1:
        v += 'Кошка'
    if not v:
        mb.showerror(message='Вы не выбрали товар')
    else:
        def check():
            check_entry = entry_1.get()
            check_entry_1 = entry_2.get()
            check_combobox = combobox_1.get()

            if not check_entry or not check_entry_1 or not check_combobox:
                mb.showerror(message='Вы не заполнели поля инфориации')
            else:
                mb.showinfo(message=f'Ваш заказ {v}')

        win_1 = tk.Toplevel(win)
        win_1.geometry('600x1000')

        label_new = tk.Label(win_1,text='Заполните поля информации')
        label_new.pack(side='top')

        label_new_1 = tk.Label(win,text='Выберете ваш город')
        label_new_1.place(x=120, y=80)

        combobox_1 = ttk.Combobox(win_1,values=['Москва','Стамбул','Санкт-Петербург','Липецк'])
        combobox_1.place(x=120, y=110)

        label_new_2 = tk.Label(win_1, text='Укажите номер телефона')
        label_new_2.place(x=120, y=140)

        entry_1 = tk.Entry(win_1)
        entry_1.place(x=120, y=170)

        label_new_3 = tk.Label(win_1, text='Укажите адрес')
        label_new_3.place(x=120, y=200)

        entry_2 = tk.Entry(win_1)
        entry_2.place(x=120, y=230)

        button_2 = tk.Button(win_1, text='Подтвердить заказ', command=check)
        button_2.pack()
def minus (item_var):
    if item_var.get() > 1:
        item_var.set(item_var.get()-1)




def plus(item_var):
    item_var.set(item_var.get()+1)






def  mouse():
    win_2 = tk.Toplevel(win)
    win_2.geometry('600x1000')
    label_11  = tk.Label(win_2,text='Выберите колличество товара')
    label_11.pack()
    a = picture_1_var.get()
    b = picture_2_var.get()
    c = picture_3_var.get()
    d = picture_4_var.get()
    if a == 1:
        label_12 = tk.Label(win_2, text='Яблоко')
        label_12.pack()

        button_1 = tk.Button(win_2, text='+',command=lambda:plus(picture_1_var))
        button_1.pack()

        label_13 = tk.Label(win_2, textvariable=picture_1_var)
        label_13.pack()

        button_2 = tk.Button(win_2, text='-',command=lambda:minus(picture_1_var))
        button_2.pack()

    if b == 1:
        label_14 = tk.Label(win_2, text='Кот')
        label_14.pack()

        button_3 = tk.Button(win_2, text='+',command=lambda:plus(picture_2_var))
        button_3.pack()

        label_15 = tk.Label(win_2, textvariable=picture_2_var)
        label_15.pack()

        button_4 = tk.Button(win_2, text='-',command=lambda:minus(picture_2_var))
        button_4.pack()

    if c == 1:
       label_16 = tk.Label(win_2, text='Пляж')
       label_16.pack()

       button_5 = tk.Button(win_2, text='+',command=lambda:plus(picture_3_var))
       button_5.pack()

       label_17 = tk.Label(win_2, textvariable=picture_3_var)
       label_17.pack()

       button_6 = tk.Button(win_2, text='-',command=lambda:minus(picture_3_var))
       button_6.pack()
    if d == 1:
        label_18 = tk.Label(win_2, text='Кошка')
        label_18.pack()

        button_7 = tk.Button(win_2, text='+',command=lambda:plus(picture_4_var))
        button_7.pack()

        label_19 = tk.Label(win_2, textvariable=picture_4_var)
        label_19.pack()

        button_8 = tk.Button(win_2, text='-',command=lambda:minus(picture_4_var))
        button_8.pack()

win = tk.Tk()
win.geometry('600x1000')

picture_1_var = tk.IntVar()
picture_1 = Image.open('h.jpg')
picture_1 = picture_1.resize((200, 200))
pic_1 = ImageTk.PhotoImage(picture_1)

label_1 = tk.Label(win,image=pic_1)
label_1.place(x=5, y=25)

label_2 = tk.Label(win, text='Яблоко', font=('Arial', 20))
label_2.place(x=20, y=230)

chekbutton_1 = tk.Checkbutton(win,variable=picture_1_var)
chekbutton_1.place(x=140, y=240)




picture_2_var = tk.IntVar()
picture_2 = Image.open('cat.jpg')
picture_2 = picture_2.resize((200, 200))
pic_2 = ImageTk.PhotoImage(picture_2)

label_3 = tk.Label(win, image=pic_2)
label_3.place(x=320, y=25)

label_4 = tk.Label(win, text='Кот', font=('Arial', 20))
label_4.place(x=360, y=230)

chekbutton_2 = tk.Checkbutton(win,variable=picture_2_var)
chekbutton_2.place(x=430, y=240)




picture_3_var = tk.IntVar()
picture_3 = Image.open('vid.jpg')
picture_3 = picture_3.resize((200, 200))
pic_3 = ImageTk.PhotoImage(picture_3)

label_5 = tk.Label(win, image=pic_3)
label_5.place(x=20, y=300)

label_6 = tk.Label(win, text='Пляж', font=('Arial', 20))
label_6.place(x=20, y=510)

chekbutton_3 = tk.Checkbutton(win,variable=picture_3_var)
chekbutton_3.place(x=120, y=520)



picture_4_var = tk.IntVar()
picture_4 = Image.open('images.jpg')
picture_4 = picture_4.resize((200, 200))
pic_4 = ImageTk.PhotoImage(picture_4)

label_7 = tk.Label(win,image=pic_4)
label_7.place(x=320, y=300)

label_8 = tk.Label(win, text='Кошка', font=('Arial', 20))
label_8.place(x=360, y=510)

chekbutton_4 = tk.Checkbutton(win, variable=picture_4_var)
chekbutton_4.place(x=430, y=520)

label_9 = tk.Label(win, text='По умолчанию одна позиция,чтобы изиенить количество',font=('Arial', 15))
label_9.place(x=65,y=600)

label_10 = tk.Label(win,text='Нажмите сюда',font=('Arial', 15))
label_10.bind('<Button-1>', lambda e:mouse())
label_10.place(x=200,y=650)

button_1  = tk.Button(win,text='Оформить заказ', width=25, height=10, command=uyuyu)
button_1.pack(side = 'bottom')




win.mainloop()

