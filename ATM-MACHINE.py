from tkinter import *
from PIL import ImageTk, Image
import time

current_balance = 1000
class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.shared_data = {'Balance':IntVar()}
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, DepositPage, BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        global bg
        global n1
        global n2
        global n3
        global n4
        global n5
        global n6
        global n7
        global n8
        global n9
        global n0
        global nc
        global ne
        self.controller.title('ATM-Machine')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,PhotoImage(file='images/atm-machine.png'))
        bg=ImageTk.PhotoImage(Image.open("images/ATM software layout.png"))
        my_canvas = Canvas(self, width=960, height=700, bd=0, highlightthickness=0)
        my_canvas.pack()
        my_canvas.create_image(0,0, image=bg, anchor="nw")
        my_canvas.create_text(380, 230, text="Please enter your PIN", font=("Helvetica", 24, "bold"))
        my_canvas.create_text(390, 390, text="Please use the KEY PAD to enter PIN", font=("Helvetica", 18))
        pin_entry= Entry(self, font=("Helvetica", 24, "bold"), width=6, bd=5)
        my_canvas.create_window(320,270, anchor="nw", window=pin_entry)
        
        def button_click(number):
            current=pin_entry.get()
            pin_entry.delete(0, END)
            pin_entry.insert(0, str(current)+str(number))
        def button_clear():
            pin_entry.delete(0, END)
        n1=ImageTk.PhotoImage(Image.open("images/1.png"))
        img_label1= Label(image=n1)
        b1= Button(self, image=n1, borderwidth=0, command=lambda: button_click(1))
        l1= Label(self, text='')
        window_1=my_canvas.create_window(275,550, anchor="nw", window=b1)

        n2=ImageTk.PhotoImage(Image.open("images/2.png"))
        img_label2= Label(image=n2)
        b2= Button(self, image=n2, borderwidth=0, command=lambda: button_click(2))
        l2= Label(self, text='')
        window_2=my_canvas.create_window(355,550, anchor="nw", window=b2)

        n3=ImageTk.PhotoImage(Image.open("images/3.png"))
        img_label3= Label(image=n3)
        b3= Button(self, image=n3, borderwidth=0, command=lambda: button_click(3))
        l3= Label(self, text='')
        window_3=my_canvas.create_window(435,550, anchor="nw", window=b3)

        n4=ImageTk.PhotoImage(Image.open("images/4.png"))
        img_label4= Label(image=n4)
        b4= Button(self, image=n4, borderwidth=0, command=lambda: button_click(4))
        l4= Label(self, text='')
        window_4=my_canvas.create_window(275,585, anchor="nw", window=b4)

        n5=ImageTk.PhotoImage(Image.open("images/5.png"))
        img_label5= Label(image=n5)
        b5= Button(self, image=n5, borderwidth=0, command=lambda: button_click(5))
        l5= Label(self, text='')
        window_5=my_canvas.create_window(355,585, anchor="nw", window=b5)

        n6=ImageTk.PhotoImage(Image.open("images/6.png"))
        img_label6= Label(image=n6)
        b6= Button(self, image=n6, borderwidth=0, command=lambda: button_click(6))
        l6= Label(self, text='')
        window_6=my_canvas.create_window(435,585, anchor="nw", window=b6)

        n7=ImageTk.PhotoImage(Image.open("images/7.png"))
        img_label7= Label(image=n7)
        b7= Button(self, image=n7, borderwidth=0, command=lambda: button_click(7))
        l7= Label(self, text='')
        window_7=my_canvas.create_window(275,620, anchor="nw", window=b7)

        n8=ImageTk.PhotoImage(Image.open("images/8.png"))
        img_label8= Label(image=n8)
        b8= Button(self, image=n8, borderwidth=0, command=lambda: button_click(8))
        l8= Label(self, text='')
        window_8=my_canvas.create_window(355,620, anchor="nw", window=b8)

        n9=ImageTk.PhotoImage(Image.open("images/9.png"))
        img_label9= Label(image=n9)
        b9= Button(self, image=n9, borderwidth=0, command=lambda: button_click(9))
        l9= Label(self, text='')
        window_9=my_canvas.create_window(435,620, anchor="nw", window=b9)

        n0=ImageTk.PhotoImage(Image.open("images/0.png"))
        img_label0= Label(image=n0)
        b0= Button(self, image=n0, borderwidth=0, command=lambda: button_click(0))
        l0= Label(self, text='')
        window_0=my_canvas.create_window(355,655, anchor="nw", window=b0)

        nc=ImageTk.PhotoImage(Image.open("images/clear.png"))
        img_labelc= Label(image=nc)
        bc= Button(self, image=nc, borderwidth=0, command=button_clear)
        lc= Label(self, text='')
        window_c=my_canvas.create_window(275,655, anchor="nw", window=bc)


        def button_enter():
            number=pin_entry.get()
            global pin
            pin=int(number)
            if pin==281832:
                ip=Label(self, text="", font=("Helvetica", 24, "bold"), foreground="red", background="#FFFFFF")
                my_canvas.create_window(390,340, width=400, height=40, window=ip)
                controller.show_frame('MenuPage')
                pin_entry.delete(0, END)            
            else:
                ip=Label(self, text="Incorrect PIN! Try Again", font=("Helvetica", 24, "bold"), foreground="red", background="#FFFFFF")
                pin_entry.delete(0, END)
                my_canvas.create_window(390,340, window=ip)
            
        
        ne=ImageTk.PhotoImage(Image.open("images/enter.png"))
        img_labele= Label(image=ne)
        be= Button(self, image=ne, borderwidth=0, command=button_enter)
        le= Label(self, text='')
        window_e=my_canvas.create_window(435,655, anchor="nw", window=be)    

class MenuPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        global c2 
        c2=ImageTk.PhotoImage(Image.open("images/canvas2.png"))
        canvas = Canvas(self, width=960, height=700, bd=0, highlightthickness=0)
        canvas.create_image(0,0, image=c2, anchor="nw")
        canvas.pack()

        frame1 = Frame(self,width=696, height=430, bg='#FF7F50' )
        frame1.pack()
        canvas.create_window(486,300, window=frame1)

        heading_label = Label(frame1,
                                                    text='NEUTRINOVAULT ATM',
                                                    font=('orbitron',40,'bold'),
                                                    foreground='#ffffff',
                                                    background='#FF7F50')
        heading_label.pack(pady=18)

        main_menu_label = Label(frame1,
                                                        text='Main Menu',
                                                        font=('orbitron',13),
                                                        fg='white',
                                                        bg='#FF7F50')
        main_menu_label.pack()

        selection_label = Label(frame1,
                                                        text='Please make a selection',
                                                        font=('orbitron',13),
                                                        fg='white',
                                                        bg='#FF7F50',
                                                        anchor='w')
        selection_label.pack(fill='x')

        button_frame = Frame(frame1,bg='#FF4040')
        button_frame.pack(fill='both',expand=True)

        def withdraw():
            controller.show_frame('WithdrawPage')
                    
        withdraw_button = Button(button_frame,
                                                            text='Withdraw',
                                                            command=withdraw,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=30,
                                                            height=3)
        withdraw_button.grid(row=0,column=0,pady=5)

        def deposit():
            controller.show_frame('DepositPage')
                    
        deposit_button = Button(button_frame,
                                                            text='Deposit',
                                                            command=deposit,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=30,
                                                            height=3)
        deposit_button.grid(row=1,column=0,pady=5)

        def balance():
            controller.show_frame('BalancePage')
                    
        balance_button = Button(button_frame,
                                                            text='Balance',
                                                            command=balance,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=30,
                                                            height=3)
        balance_button.grid(row=2,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')
                    
        exit_button = Button(button_frame,
                                                            text='Exit',
                                                            command=exit,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=30,
                                                            height=3)
        exit_button.grid(row=3,column=0,pady=5)


        bottom_frame = Frame(frame1,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = PhotoImage(file='images/visa.png')
        visa_label = Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = PhotoImage(file='images/mastercard.png')
        mastercard_label = Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = PhotoImage(file='images/american-express.png')
        american_express_label = Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick() 


class WithdrawPage(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        global c3 
        c3=ImageTk.PhotoImage(Image.open("images/canvas2.png"))
        canvas = Canvas(self, width=960, height=700, bd=0, highlightthickness=0)
        canvas.create_image(0,0, image=c2, anchor="nw")
        canvas.pack()

        frame1 = Frame(self,width=696, height=430, bg='#FF7F50' )
        frame1.pack()
        canvas.create_window(486,300, window=frame1)

        heading_label = Label(frame1,
                                                     text='NEUTRINOVAULT ATM',
                                                     font=('orbitron',40,'bold'),
                                                     foreground='#ffffff',
                                                     background='#FF7F50')
        heading_label.pack(pady=21)

        choose_amount_label = Label(frame1,
                                                           text='Choose the amount you want to withdraw',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#FF7F50')
        choose_amount_label.pack()

        button_frame = Frame(frame1,bg='#FF4040')
        button_frame.pack(fill='both',expand=True)

        def withdraw(amount):
            global current_balance
            current_balance -= amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            
        twenty_button = Button(button_frame,
                                                       text='20',
                                                       command=lambda:withdraw(20),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=15,
                                                       height=3)
        twenty_button.grid(row=0,column=0,pady=5)

        forty_button = Button(button_frame,
                                                       text='40',
                                                       command=lambda:withdraw(40),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=15,
                                                       height=3)
        forty_button.grid(row=1,column=0,pady=5)

        sixty_button = Button(button_frame,
                                                       text='60',
                                                       command=lambda:withdraw(60),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=15,
                                                       height=3)
        sixty_button.grid(row=2,column=0,pady=5)

        eighty_button = Button(button_frame,
                                                       text='80',
                                                       command=lambda:withdraw(80),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=15,
                                                       height=3)
        eighty_button.grid(row=3,column=0,pady=5)

        one_hundred_button = Button(button_frame,
                                                       text='100',
                                                       command=lambda:withdraw(100),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=15,
                                                       height=3)
        one_hundred_button.grid(row=0,column=1,pady=5,padx=200)

        two_hundred_button = Button(button_frame,
                                                       text='200',
                                                       command=lambda:withdraw(200),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=15,
                                                       height=3)
        two_hundred_button.grid(row=1,column=1,pady=5)

        three_hundred_button = Button(button_frame,
                                                       text='300',
                                                       command=lambda:withdraw(300),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=15,
                                                       height=3)
        three_hundred_button.grid(row=2,column=1,pady=5)

        cash = StringVar()
        other_amount_entry = Entry(button_frame,
                                                              textvariable=cash,
                                                              width=20,
                                                              justify='right')
        other_amount_entry.grid(row=3,column=1,pady=5,ipady=30)

        def other_amount(_):
            global current_balance
            current_balance -= int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('MenuPage')
            
        other_amount_entry.bind('<Return>',other_amount)

        bottom_frame = Frame(frame1,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = PhotoImage(file='images/visa.png')
        visa_label = Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = PhotoImage(file='images/mastercard.png')
        mastercard_label = Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = PhotoImage(file='images/american-express.png')
        american_express_label = Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()
   

class DepositPage(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        global c3
        c3=ImageTk.PhotoImage(Image.open("images/canvas2.png"))
        canvas = Canvas(self, width=960, height=700, bd=0, highlightthickness=0)
        canvas.create_image(0,0, image=c2, anchor="nw")
        canvas.pack()

        frame1 = Frame(self,width=696, height=430, bg='#FF7F50' )
        frame1.pack()
        canvas.create_window(486,300, window=frame1)

        heading_label = Label(frame1,
                                                     text='NEUTRINOVAULT ATM',
                                                     font=('orbitron',40,'bold'),
                                                     foreground='#ffffff',
                                                     background='#FF7F50')
        heading_label.pack(pady=29)

        space_label = Label(frame1,height=4,bg='#FF7F50')
        space_label.pack()

        enter_amount_label = Label(frame1,
                                                      text='Enter amount',
                                                      font=('orbitron',13),
                                                      bg='#FF7F50',
                                                      fg='white')
        enter_amount_label.pack(pady=20)

        cash = StringVar()
        deposit_entry = Entry(frame1,
                                                  textvariable=cash,
                                                  font=('orbitron',12),
                                                  width=22)
        deposit_entry.pack(ipady=14)

        def deposit_cash():
            global current_balance
            current_balance += int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')
            
        enter_button = Button(frame1,
                                                     text='Enter',
                                                     command=deposit_cash,
                                                     relief='raised',
                                                     borderwidth=3,
                                                     width=40,
                                                     height=3)
        enter_button.pack(pady=20)

        two_tone_label = Label(frame1,bg='#FF7F50')
        two_tone_label.pack(fill='both',expand=True)

        bottom_frame = Frame(frame1,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = PhotoImage(file='images/visa.png')
        visa_label = Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = PhotoImage(file='images/mastercard.png')
        mastercard_label = Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = PhotoImage(file='images/american-express.png')
        american_express_label = Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()


class BalancePage(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        global c4
        c4=ImageTk.PhotoImage(Image.open("images/canvas2.png"))
        canvas = Canvas(self, width=960, height=700, bd=0, highlightthickness=0)
        canvas.create_image(0,0, image=c2, anchor="nw")
        canvas.pack()

        frame1 = Frame(self,width=696, height=430, bg='#FF7F50' )
        frame1.pack()
        canvas.create_window(486,300, window=frame1)

        
        heading_label = Label(frame1,
                                                     text='NEUTRINOVAULT ATM',
                                                     font=('orbitron',40,'bold'),
                                                     foreground='#ffffff',
                                                     background='#FF7F50')
        heading_label.pack(pady=35)

        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label = Label(frame1,
                                                  textvariable=controller.shared_data['Balance'],
                                                  font=('orbitron',13),
                                                  fg='white',
                                                  bg='#FF7F50',
                                                  anchor='w')
        balance_label.pack(fill='x')

        button_frame = Frame(frame1,bg='#FF4040')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = Button(button_frame,
                                                    command=menu,
                                                    text='Menu',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=40,
                                                    height=4)
        menu_button.grid(row=0,column=0,pady=30)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = Button(button_frame,
                                                 text='Exit',
                                                 command=exit,
                                                 relief='raised',
                                                 borderwidth=3,
                                                 width=40,
                                                 height=4)
        exit_button.grid(row=1,column=0,pady=30)

        bottom_frame = Frame(frame1,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = PhotoImage(file='images/visa.png')
        visa_label = Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = PhotoImage(file='images/mastercard.png')
        mastercard_label = Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = PhotoImage(file='images/american-express.png')
        american_express_label = Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("960x700")
    app.mainloop()
