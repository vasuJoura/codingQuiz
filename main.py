# common login for admin and student

from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkcalendar import DateEntry

import adminProfile
from connection import Connect
from tkinter import messagebox
from tkinter import ttk
from emailSend import mailing
import string
import random
from changeDate import changedate
import dashboardDemo

class Launch:

    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('QUIZ & LEARN - LOGIN WINDOW')
        self.root.config(background="#320052")

        # Favicon image for root window
        self.fav = PhotoImage(file='images/quiz.png')
        self.root.iconphoto(False, self.fav)

        # Get screen height & width for effective use of pack and place
        height = int(self.root.winfo_screenheight())
        width = int(self.root.winfo_screenwidth())

        # DATABASE CONNECTION
        self.conn = Connect()
        self.cr = self.conn.cursor()

        # Mainframes for Signup Page
        self.mainFrame1 = Frame(self.root, bg='#39005D')
        self.mainFrame2 = Frame(self.root, bg='#39005D')

        self.mainFrame1.pack(side='right', fill="both", expand=True)
        self.mainFrame2.place(x=height, y=0)

        # Fonts used
        self.headerFont = Font(family='UI Gothic', size=42, weight='bold', )
        self.bodyFont = Font(family='UI Gothic', size=16)
        self.buttonFont = Font(family='Yu Gothic', size=14)

        # Inside Frame 1, Image is placed___________________________________________________
        img = Image.open('images/bg1.png')

        img = img.resize((width//2+200, height-20))
        self.bg = ImageTk.PhotoImage(img)
        self.bgImg = Label(self.mainFrame1, image=self.bg, bg='#39005D')
        self.bgImg.place(x=-40, y=0)

        # Inside Frame 2, Content is placed___________________________________________________

        # Page Heading
        Label(self.mainFrame2, font=self.headerFont, bg='#39005D', fg="#F3EBFE", text='QUIZ & LEARN').pack(anchor='w', pady=15)

        self.showLoginForm()
        self.root.mainloop()


    def hideLoginForm(self):
        self.buttonFrameL.pack_forget()
        self.formFrameL.pack_forget()
        self.formLabel.pack_forget()
        self.SpaceFrameL.pack_forget()
        self.showSignupForm()


    def hideSignupForm(self):
        self.buttonFrameS.pack_forget()
        self.formFrameS.pack_forget()
        self.formLabel.pack_forget()
        self.showLoginForm()


    """A FUNCTION TO LOAD THE CNTENTS OF THE LOGIN FORM"""
    def showLoginForm(self):
        self.formLabel = Label(self.mainFrame2, font=self.bodyFont, bg='#39005D', fg="#F3EBFE", text='Login Form')
        self.formLabel.pack(anchor='w', padx=10)

        # Frames
        self.formFrameL = Frame(self.mainFrame2, bg="#4B007A", highlightbackground='#e8ebed', highlightthickness=3)
        self.formFrameL.pack(anchor='w', pady=5)
        self.buttonFrameL = Frame(self.mainFrame2, bg="#4B007A", highlightbackground='#e8ebed', highlightthickness=3,
                                 pady=5, padx=10)
        self.buttonFrameL.pack(anchor='w', pady=5)

        self.SpaceFrameL = Frame(self.mainFrame2, bg="#320052", height=400, width=450,
                                  pady=5, padx=10)
        self.SpaceFrameL.pack(anchor='w', pady=5, fill='both')
        self.SpaceFrameL.pack_propagate(0)

        #FIELDS___________________________________
        #email
        self.emailLabel = Label(self.formFrameL, text='Email :',
                                font=self.bodyFont, pady=7,
                                bg='#4B007A', fg='#e8ebed')

        self.loginEmail = Entry(self.formFrameL, width=27, font=self.bodyFont)
        self.emailLabel.grid(row=0, column=0, sticky='w', pady=17, padx=12)
        self.loginEmail.grid(row=0, column=1, sticky='w', pady=7, padx=35)

        #password
        self.passwordLabel = Label(self.formFrameL, text='Password :',
                                   font=self.bodyFont, pady=7,
                                   bg='#4B007A', fg='#e8ebed')

        self.loginPassword = Entry(self.formFrameL, width=27, font=self.bodyFont, show="*")
        self.passwordLabel.grid(row=1, column=0, sticky='w', pady=7, padx=12)
        self.loginPassword.grid(row=1, column=1, sticky='w', pady=7, padx=35)

        # Forget Password
        self.forgetPasswordLabel = Label(self.formFrameL, text='Forget Password ?',
                                   font=self.bodyFont, pady=7,
                                   bg='#4B007A', fg='#e8ebed')
        # self.forgetPasswordLabel.grid(row=2, column=0, columnspan=2, sticky='e', padx=28, pady=7)
        self.forgetPasswordLabel.bind('<Button-1>', self.ForgetPassword)

        # Buttons

        self.submitBtnL = Button(self.buttonFrameL, text='Submit', font=self.buttonFont, padx=33, pady=5, bg="#6308F7",
                                fg="#F3EBFE", activebackground="#580CE7", activeforeground="#F3EBFE", command=self.login)
        self.submitBtnL.pack(side='left', padx=15, pady=5)

        self.SignupBtnL = Button(self.buttonFrameL, text='Sign up', font=self.buttonFont, padx=33, pady=5, command=self.hideLoginForm)
        self.SignupBtnL.pack(side='left', padx=15, pady=5)

        self.refreshBtnL = Button(self.buttonFrameL, text='Reset', font=self.buttonFont, padx=33, pady=5, bg="#F18D41",
                                 activebackground="#EE771B", command=self.resetLogin)
        self.refreshBtnL.pack(side='left', padx=15, pady=5)




    """A FUNCTION TO LOAD THE CONTENTS OF THE SIGNUP FORM"""
    def showSignupForm(self):

        self.formLabel = Label(self.mainFrame2, font=self.bodyFont, bg='#39005D', fg="#F3EBFE", text='Signup Form')
        self.formLabel.pack(anchor='w', padx=10)

        # Frames
        self.formFrameS = Frame(self.mainFrame2, bg="#4B007A", highlightbackground='#e8ebed', highlightthickness=3)
        self.formFrameS.pack(anchor='w', pady=5)
        self.buttonFrameS = Frame(self.mainFrame2, bg="#4B007A", highlightbackground='#e8ebed', highlightthickness=3,
                                 pady=5, padx=10)
        self.buttonFrameS.pack(anchor='w', pady=5)

        # FIELDS___________________________________
        # Name
        self.nameLabel = Label(self.formFrameS, text='Name :',
                               font=self.bodyFont, pady=7,
                               bg='#4B007A', fg='#e8ebed')

        self.name = Entry(self.formFrameS, width=27, font=self.bodyFont)
        self.nameLabel.grid(row=0, column=0, sticky='w', pady=7, padx=12)
        self.name.grid(row=0, column=1, sticky='w', pady=7, padx=35)

        # Mobile

        self.mobileLabel = Label(self.formFrameS, text='Mobile :',
                                 font=self.bodyFont, pady=7,
                                 bg='#4B007A', fg='#e8ebed')

        self.mobile = Entry(self.formFrameS, width=27, font=self.bodyFont)
        self.mobileLabel.grid(row=1, column=0, sticky='w', pady=7, padx=12)
        self.mobile.grid(row=1, column=1, sticky='w', pady=7, padx=35)

        # Email

        self.emailLabel = Label(self.formFrameS, text='Email :',
                                font=self.bodyFont, pady=7,
                                bg='#4B007A', fg='#e8ebed')

        self.email = Entry(self.formFrameS, width=27, font=self.bodyFont)
        self.emailLabel.grid(row=2, column=0, sticky='w', pady=7, padx=12)
        self.email.grid(row=2, column=1, sticky='w', pady=7, padx=35)

        # Date Of Birth

        self.DOBLabel = Label(self.formFrameS, text='Birth Date :',
                              font=self.bodyFont, pady=7,
                              bg='#4B007A', fg='#e8ebed')

        self.DOB = DateEntry(self.formFrameS, width=26, font=self.bodyFont)
        self.DOBLabel.grid(row=3, column=0, sticky='w', pady=7, padx=12)
        self.DOB.grid(row=3, column=1, sticky='w', pady=7, padx=35)

        # Address

        self.addressLabel = Label(self.formFrameS, text='Address :',
                                  font=self.bodyFont, pady=7,
                                  bg='#4B007A', fg='#e8ebed')

        self.address = Entry(self.formFrameS, width=27, font=self.bodyFont)
        self.addressLabel.grid(row=4, column=0, sticky='w', pady=7, padx=12)
        self.address.grid(row=4, column=1, sticky='w', pady=7, padx=35)

        # City

        self.cityLabel = Label(self.formFrameS, text='City :',
                               font=self.bodyFont, pady=7,
                               bg='#4B007A', fg='#e8ebed')

        self.city = Entry(self.formFrameS, width=27, font=self.bodyFont)
        self.cityLabel.grid(row=5, column=0, sticky='w', pady=7, padx=12)
        self.city.grid(row=5, column=1, sticky='w', pady=7, padx=35)

        # State

        self.stateLabel = Label(self.formFrameS, text='State :',
                                font=self.bodyFont, pady=7,
                                bg='#4B007A', fg='#e8ebed')
        self.stateList = ['Union Territory', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
        self.state = ttk.Combobox(self.formFrameS, width=26, state="readonly", values=self.stateList, font=self.bodyFont)
        # self.state.set(stateList[0])
        self.state.current(0)
        self.stateLabel.grid(row=6, column=0, sticky='w', pady=7, padx=12)
        self.state.grid(row=6, column=1, sticky='w', pady=7, padx=35)

        # Password

        self.passwordLabel = Label(self.formFrameS, text='Password :',
                                   font=self.bodyFont, pady=7,
                                   bg='#4B007A', fg='#e8ebed')

        self.password = Entry(self.formFrameS, width=27, font=self.bodyFont, show="*")
        self.passwordLabel.grid(row=7, column=0, sticky='w', pady=7, padx=12)
        self.password.grid(row=7, column=1, sticky='w', pady=7, padx=35)

        # INSIDE BUTTONFRAME_____________________________________________________

        self.submitBtnS = Button(self.buttonFrameS, text='Submit', font=self.buttonFont, padx=37, pady=5,  bg="#6308F7",
                                fg="#F3EBFE",activebackground="#580CE7", activeforeground="#F3EBFE", command=self.verifyMobile)
        self.submitBtnS.pack(side='left', padx=15, pady=5)

        self.LoginBtnS = Button(self.buttonFrameS, text='Login', font=self.buttonFont, padx=38, pady=5, command=self.hideSignupForm)
        self.LoginBtnS.pack(side='left', padx=15, pady=5)

        self.refreshBtnS = Button(self.buttonFrameS, text='Reset', font=self.buttonFont, padx=37, pady=5, bg="#ff8d2c",
                                 activebackground="#ff7e00", command=self.resetSignup)
        self.refreshBtnS.pack(side='left', padx=15, pady=5)


    # LOGIN ____________________________________________________________________________________________________________
    def login(self):

        # Check if admin exists
        S1 = f"SELECT * from admin where email='{self.loginEmail.get()}' and password='{self.loginPassword.get()}'"
        self.cr.execute(S1)
        adminResults = self.cr.fetchall()

        if len(adminResults) != 0:
            # IF ADMIN EXISTS, ADMIN PENAL WILL OPEN, OTHERWISE, will check for student
            self.resetLogin()
            adminProfile.settings(adminResults[0]['id'])

        else:
            # Check if student exists
            S2 = f"SELECT * from users where email='{self.loginEmail.get()}' and password='{self.loginPassword.get()}'"
            self.cr.execute(S2)
            results = self.cr.fetchall()
            print(results)

            if len(results) == 0:
                messagebox.showerror('LOGIN FAILED!!', 'Incorrect Email or Password', parent=self.root)
            else:
                # print(results)
                self.root.destroy()
                dashboardDemo.Dashboard(results[0]['user_id'])


    # SIGNUP & ITS CHECKS ______________________________________________________________________________________________
    def verifyMobile(self):
        # A FUNCTION TO VERIFY UNIQUE AND CORRECT INPUT OF A NUMBER
        self.mobileVal = self.mobile.get()
        # mobile unique constrain
        m = f"select * from users where mobile='{self.mobileVal}'"
        self.cr.execute(m)
        result1 = self.cr.fetchall()

        if len(str(self.mobileVal)) == 10 and str(self.mobileVal).isnumeric():
            if len(result1) == 0:
                self.verifyEmail()
            else:
                messagebox.showerror('SIGNUP FAILED!!', 'A User with this Mobile number already exists ', parent=self.root)
        else:
            messagebox.showerror('SIGNUP FAILED!!', 'Invalid Mobile Number', parent=self.root)

    def verifyEmail(self):
        self.emailVal = self.email.get()
        e = f"select * from users where email='{self.emailVal}'"
        self.cr.execute(e)
        result2 = self.cr.fetchall()

        if str(self.emailVal).isascii() and '@' in str(self.emailVal) and '.' in str(self.emailVal):
            if len(result2) == 0:
                # Other Verifications
                if len(self.name.get()) > 0 and len(self.city.get()) > 0 and len(self.address.get()) > 0:
                    if len(self.password.get()) > 8:
                        self.signup()
                    else:
                        messagebox.showerror('SIGNUP FAILED!!', 'Please choose a longer passwords ', parent=self.root)
                else:
                    messagebox.showerror('SIGNUP FAILED!!', 'Please fill all the fields', parent=self.root)
            else:
                messagebox.showerror('SIGNUP FAILED!!', 'A user with the same email address already exists', parent=self.root)
        else:
            messagebox.showerror('SIGNUP FAILED!!', "Invalid Email Address is entered", parent=self.root)

    def signup(self):
        Date = changedate(self.DOB.get())
        Q = f"insert into users values(null, '{self.name.get()}', '{self.mobile.get()}', '{self.address.get()}', '{self.city.get()}', '{ self.state.get()}','{Date}','{self.email.get()}', '{self.password.get()}')"
        self.cr.execute(Q)
        self.conn.commit()
        messagebox.showinfo('Success', 'Signup Successful. PLease Login now', parent=self.root)
        self.resetSignup()

    # RESET FORM _______________________________________________________________________________________________________
    def resetSignup(self):
        self.name.delete(0, 'end')
        self.mobile.delete(0, 'end')
        self.city.delete(0, 'end')
        self.address.delete(0, 'end')
        self.email.delete(0, 'end')
        self.state.set(self.stateList[0])
        self.password.delete(0, 'end')
        self.DOB.delete(0, "end")

    def resetLogin(self):
        self.loginPassword.delete(0, 'end')
        self.loginEmail.delete(0, 'end')

    # FORGET PASSWORD __________________________________________________________________________________________________
    def ForgetPassword(self, event):
        self.rootfp = Toplevel()
        self.rootfp.geometry('550x350')
        self.rootfp.config(background='#39005D')
        # header label
        Label(self.rootfp, text='Forget Password', font=self.headerFont, padx=10, pady=15, bg='#39005D',
              fg='#F3EBFE').pack(pady=25)

        # Frame
        self.fpframe = Frame(self.rootfp, bg='#4B007A',  highlightbackground='#e8ebed', highlightthickness=3,  padx=20, pady=20)
        self.fpframe.pack()

        self.emailLabelfp = Label(self.fpframe, text='Email :', font=('Arial', 18), padx=10, pady=10, bg='#4B007A',
                                 fg='#e8ebed')
        self.emailEntryfp = Entry(self.fpframe, font=self.bodyFont, width=26)
        self.emailLabelfp.grid(row=0, column=0)
        self.emailEntryfp.grid(row=0, column=1)

        self.sendEmailfp = Button(self.rootfp, text='Get Password', font=self.buttonFont, width=12, command=self.sendEmailFunc, pady=8, padx=10, activebackground='#F3EBFE')
        self.sendEmailfp.pack(pady=25)

        self.rootfp.mainloop()

    def sendEmailFunc(self):
        self.emailFp = self.emailEntryfp.get()

        Q = f"SELECT user_id FROM users where email='{self.emailFp}'"
        self.cr.execute(Q)
        result = self.cr.fetchall()
        if len(result) == 0:
            messagebox.showerror('Error !', 'No User with this email exists in the Database', parent=self.root)
            self.rootfp.destroy()
        else:
            print(result)
            print(result[0]['user_id'])
            user_id = result[0]['user_id']
            lenS = 10
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=lenS))
            password = str(ran)
            s = f"UPDATE users SET password='{password}' where user_id='{user_id}'"
            self.cr.execute(s)
            self.conn.commit()
            try:
                mailing(reciever=self.emailFp, subject='New Password', text=f'Here is your Password {password}')
                messagebox.showinfo('Success', 'Your password has been successfully sent on your email address. Use it to Log in', parent=self.root)
                self.rootfp.destroy()
            except:
                messagebox.showerror('Unable to send Email', 'This Email Address cannot be reached right now', parent=self.root)
                self.rootfp.destroy()

if __name__ == "__main__":
    Launch()