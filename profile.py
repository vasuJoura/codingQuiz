from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkcalendar import DateEntry
from connection import Connect
from tkinter import messagebox
from tkinter import ttk
from emailSend import mailing
import string
import random
from changeDate import changedate


class settings:

    def __init__(self, id):

        # Colors By Default
        self.bgColorDark = '#39005D'
        self.bgColor = '#39005D'
        self.bgColorLite = '#3F0066'
        self.fgColor = '#F3EBFE'

        # Button Colors
        self.btn3 = "#ff8d2c"
        self.btn3A = "#ff7e00"

        self.btn1 = "#6007ED"
        self.btn1A = "#520BD5"

        self.id = id


        self.root = Toplevel()
        self.root.state('zoomed')
        self.root.title('QUIZ & LEARN - DASHBOARD')
        self.root.config(background='#320052')

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
        self.mainFrame1 = Frame(self.root, bg=self.bgColor)
        self.mainFrame2 = Frame(self.root, bg=self.bgColor)

        self.mainFrame1.pack(side='right', fill="both", expand=True)
        self.mainFrame2.place(x=height, y=0)

        # Fonts used
        self.headerFont = Font(family='UI Gothic', size=42, weight='bold', )
        self.bodyFont = Font(family='UI Gothic', size=16)
        self.buttonFont = Font(family='Yu Gothic', size=14)

        # Inside Frame 1, Image is placed___________________________________________________
        img = Image.open('images/bg1.png')

        img = img.resize((width // 2 + 200, height - 20))
        self.bg = ImageTk.PhotoImage(img)
        self.bgImg = Label(self.mainFrame1, image=self.bg, bg='#39005D')
        self.bgImg.place(x=-40, y=0)

        # Inside Frame 2, Content is placed___________________________________________________

        # Page Heading
        Label(self.mainFrame2, font=self.headerFont, bg=self.bgColor, fg="#ffffff", text='USER PROFILE').pack(
            anchor='w', pady=15)
        self.updateProfileForm()

        self.root.mainloop()

    def callChangePasswordForm(self):

        self.formUP.pack_forget()
        self.buttonContainerUP.pack_forget()
        self.buttonFrameUP.pack_forget()
        self.changePasswordForm()

    def callUpdateProfileForm(self):

        self.formCP.pack_forget()
        self.buttonContainerCP.pack_forget()
        self.buttonFrameCP.pack_forget()
        self.updateProfileForm()
        self.resetProfileUpdate()
        self.loadDetails()

    def destroy(self):
        self.root.destroy()

    def resetProfileUpdate(self):
        self.name.delete(0, 'end')
        self.mobile.delete(0, 'end')
        self.city.delete(0, 'end')
        self.address.delete(0, 'end')
        self.email.delete(0, 'end')

    def resetChangePassword(self):
        self.oldPassword.delete(0, 'end')
        self.newPassword.delete(0, 'end')
        self.newPassword2.delete(0, 'end')

    """A FUNCTION TO LOAD THE CONTENTS OF THE SIGNUP FORM"""

    def updateProfileForm(self):

        # Frames

        self.buttonFrameUP = Frame(self.mainFrame2, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                   highlightthickness=3,
                                   pady=5, padx=10)
        self.buttonFrameUP.pack(anchor='w', pady=5)

        # Buttons

        self.settings = Button(self.buttonFrameUP, text='Settings', font=self.buttonFont, padx=31, pady=5,
                               bg=self.btn3,
                               fg=self.fgColor, activebackground=self.btn3A, activeforeground=self.fgColor)
        self.settings.pack(side='left', padx=15, pady=5)

        self.Password = Button(self.buttonFrameUP, text='Password', font=self.buttonFont, padx=30, pady=5,
                               command=self.callChangePasswordForm)
        self.Password.pack(side='left', padx=15, pady=5)

        self.Exit = Button(self.buttonFrameUP, text='Exit', font=self.buttonFont, padx=31, pady=5,
                           bg=self.btn1, fg=self.fgColor, activeforeground=self.fgColor,
                           activebackground=self.btn1A, command=self.destroy)
        self.Exit.pack(side='left', padx=15, pady=5)

        self.formUP = Frame(self.mainFrame2, bg=self.bgColorLite, highlightbackground=self.fgColor,
                            highlightthickness=3)
        self.formUP.pack(anchor='w', pady=5)

        # FIELDS___________________________________
        # Name
        self.nameLabel = Label(self.formUP, text='Name',
                               font=self.bodyFont, pady=7,
                               bg=self.bgColorLite, fg=self.fgColor)

        self.name = Entry(self.formUP, width=28, font=self.bodyFont)
        self.nameLabel.grid(row=0, column=0, sticky='w', pady=7, padx=20)
        self.name.grid(row=0, column=1, sticky='w', pady=7, padx=35)

        # Mobile

        self.mobileLabel = Label(self.formUP, text='Mobile',
                                 font=self.bodyFont, pady=7,
                                 bg=self.bgColorLite, fg=self.fgColor)

        self.mobile = Entry(self.formUP, width=28, font=self.bodyFont)
        self.mobileLabel.grid(row=1, column=0, sticky='w', pady=7, padx=20)
        self.mobile.grid(row=1, column=1, sticky='w', pady=7, padx=35)

        # Email

        self.emailLabel = Label(self.formUP, text='Email',
                                font=self.bodyFont, pady=7,
                                bg=self.bgColorLite, fg=self.fgColor)

        self.email = Entry(self.formUP, width=28, font=self.bodyFont)
        self.emailLabel.grid(row=2, column=0, sticky='w', pady=7, padx=20)
        self.email.grid(row=2, column=1, sticky='w', pady=7, padx=35)

        # Address

        self.addressLabel = Label(self.formUP, text='Address',
                                  font=self.bodyFont, pady=7,
                                  bg=self.bgColorLite, fg=self.fgColor)

        self.address = Entry(self.formUP, width=28, font=self.bodyFont)
        self.addressLabel.grid(row=4, column=0, sticky='w', pady=7, padx=20)
        self.address.grid(row=4, column=1, sticky='w', pady=7, padx=35)

        # City

        self.cityLabel = Label(self.formUP, text='City',
                               font=self.bodyFont, pady=7,
                               bg=self.bgColorLite, fg=self.fgColor)

        self.city = Entry(self.formUP, width=28, font=self.bodyFont)
        self.cityLabel.grid(row=5, column=0, sticky='w', pady=7, padx=20)
        self.city.grid(row=5, column=1, sticky='w', pady=7, padx=35)

        # State

        self.stateLabel = Label(self.formUP, text='State',
                                font=self.bodyFont, pady=7,
                                bg=self.bgColorLite, fg=self.fgColor)
        self.stateList = ['Union Territory', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
                          'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala',
                          'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
                          'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand',
                          'West Bengal']
        self.state = ttk.Combobox(self.formUP, width=26, state="readonly", values=self.stateList, font=self.bodyFont)
        # self.state.set(stateList[0])
        self.state.current(0)
        self.stateLabel.grid(row=6, column=0, sticky='w', pady=7, padx=20)
        self.state.grid(row=6, column=1, sticky='w', pady=7, padx=35)

        # submit
        self.buttonContainerUP = Frame(self.mainFrame2, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                       highlightthickness=3,
                                       pady=5, padx=10, width=540, height=80)
        self.buttonContainerUP.pack(anchor='w', pady=5)
        self.buttonContainerUP.pack_propagate(0)

        self.SubmitBtnUP = Button(self.buttonContainerUP, text='Submit', font=self.buttonFont, padx=31, pady=5,
                                  bg=self.btn1, fg=self.fgColor, activeforeground=self.fgColor,
                                  activebackground=self.btn1A, command=self.verifyMobile)
        self.SubmitBtnUP.pack(side='right', padx=15, pady=5)
        self.loadDetails()

    """A FUNCTION TO LOAD THE CNTENTS OF THE LOGIN FORM"""

    def changePasswordForm(self):

        # Frames

        self.buttonFrameCP = Frame(self.mainFrame2, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                   highlightthickness=3,
                                   pady=5, padx=10)
        self.buttonFrameCP.pack(anchor='w', pady=5)

        # Buttons

        self.settings = Button(self.buttonFrameCP, text='Settings', font=self.buttonFont, padx=31, pady=5,
                               bg=self.btn3,
                               fg=self.fgColor, activebackground=self.btn3A, activeforeground=self.fgColor,
                               command=self.callUpdateProfileForm)
        self.settings.pack(side='left', padx=15, pady=5)

        self.Password = Button(self.buttonFrameCP, text='Password', font=self.buttonFont, padx=30, pady=5)
        self.Password.pack(side='left', padx=15, pady=5)

        self.Exit = Button(self.buttonFrameCP, text='Exit', font=self.buttonFont, padx=31, pady=5,
                           bg=self.btn1, fg=self.fgColor, activeforeground=self.fgColor,
                           activebackground=self.btn1A, command=self.destroy)
        self.Exit.pack(side='left', padx=15, pady=5)

        self.formCP = Frame(self.mainFrame2, bg=self.bgColorLite, highlightbackground=self.fgColor,
                            highlightthickness=3)
        self.formCP.pack(anchor='w', pady=5)

        # FIELDS___________________________________

        # password OLD
        self.passwordLabel = Label(self.formCP, text='Old password',
                                   font=self.bodyFont, pady=7,
                                   bg=self.bgColorLite, fg=self.fgColor)

        self.oldPassword = Entry(self.formCP, width=24, font=self.bodyFont, show="*")
        self.passwordLabel.grid(row=0, column=0, sticky='w', pady=7, padx=12)
        self.oldPassword.grid(row=0, column=1, sticky='w', pady=7, padx=20)

        # password NEW
        self.passwordLabel1 = Label(self.formCP, text='New password',
                                    font=self.bodyFont, pady=7,
                                    bg=self.bgColorLite, fg=self.fgColor)

        self.newPassword = Entry(self.formCP, width=24, font=self.bodyFont, show="*")
        self.passwordLabel1.grid(row=1, column=0, sticky='w', pady=7, padx=12)
        self.newPassword.grid(row=1, column=1, sticky='w', pady=7, padx=20)

        # password NEW 2
        self.passwordLabel2 = Label(self.formCP, text='Re-type password',
                                    font=self.bodyFont, pady=7,
                                    bg=self.bgColorLite, fg=self.fgColor)

        self.newPassword2 = Entry(self.formCP, width=24, font=self.bodyFont, show="*")
        self.passwordLabel2.grid(row=2, column=0, sticky='w', pady=7, padx=12)
        self.newPassword2.grid(row=2, column=1, sticky='w', pady=7, padx=20)

        # Forget Password
        self.forgetPasswordLabel = Label(self.formCP, text='Forget Password ?',
                                         font=self.bodyFont, pady=7,
                                         bg=self.bgColorLite, fg=self.fgColor)
        # self.forgetPasswordLabel.grid(row=3, column=0, columnspan=2, sticky='e', padx=28, pady=7)
        self.forgetPasswordLabel.bind('<Button-1>', self.ForgetPassword)

        # submit
        self.buttonContainerCP = Frame(self.mainFrame2, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                       highlightthickness=3,
                                       pady=5, padx=10, width=540, height=80)
        self.buttonContainerCP.pack(anchor='w', pady=5)
        self.buttonContainerCP.pack_propagate(0)

        self.SubmitBtnCP = Button(self.buttonContainerCP, text='Submit', font=self.buttonFont, padx=31, pady=5,
                                  bg=self.btn1, fg=self.fgColor, activeforeground=self.fgColor,
                                  activebackground=self.btn1A, command=self.changePassword)
        self.SubmitBtnCP.pack(side='right', padx=15, pady=5)

    def loadDetails(self):

        S = f"select * from users where user_id = '{self.id}'"
        self.cr.execute(S)
        self.userDetail = self.cr.fetchone()
        print(self.userDetail)

        self.mobile.insert(0, self.userDetail['mobile'])
        self.name.insert(0, self.userDetail['name'])
        self.address.insert(0, self.userDetail['address'])
        self.city.insert(0, self.userDetail['city'])
        self.email.insert(0, self.userDetail['email'])

        index = self.stateList.index(self.userDetail['state'])
        print(index)
        self.state.set(self.userDetail['state'])

    def changePassword(self):
        op = self.oldPassword.get()
        np = self.newPassword.get()
        np2 = self.newPassword2.get()

        if op == self.userDetail['password']:
            if np == np2:
                if len(np) > 8:
                    s = f"update users set password = '{np}' where user_id = '{self.id}'"
                    self.cr.execute(s)
                    self.conn.commit()
                    self.resetChangePassword()
                    messagebox.showinfo('PASSWORD CHANGED SUCCESSFULLY!!',
                                        'Your password has been changed successfully', parent=self.root)

                else:
                    messagebox.showerror('SIGNUP FAILED!!', 'Please choose a longer passwords ', parent=self.root)
            else:
                messagebox.showerror('failed to change password', 'the two password fields do not match', parent=self.root)
        else:
            messagebox.showerror('failed to change password', 'incorrect password', parent=self.root)

    # SIGNUP & ITS CHECKS ______________________________________________________________________________________________
    def verifyMobile(self):
        # A FUNCTION TO VERIFY UNIQUE AND CORRECT INPUT OF A NUMBER
        self.mobileVal = self.mobile.get()
        # mobile unique constrain

        if len(str(self.mobileVal)) == 10 and str(self.mobileVal).isnumeric():
            self.verifyEmail()

        else:
            messagebox.showerror('SIGNUP FAILED!!', 'Invalid Mobile Number', parent=self.root)

    def verifyEmail(self):
        self.emailVal = self.email.get()
        if str(self.emailVal).isascii() and '@' in str(self.emailVal) and '.' in str(self.emailVal):
            self.update()
        else:
            messagebox.showerror('SIGNUP FAILED!!', "Invalid Email Address is entered", parent=self.root)

    def update(self):
        S = f"update users set email='{self.email.get()}', name = '{self.name.get()}', mobile = '{self.mobile.get()}', address = '{self.address.get()}', city = '{self.city.get()}' , state = '{self.state.get()}' where user_id = '{self.id}'"
        self.cr.execute(S)
        self.conn.commit()
        messagebox.showinfo('success', 'Profile updated successfully',parent=self.root)

    # Exit FORM _______________________________________________________________________________________________________

    # FORGET PASSWORD __________________________________________________________________________________________________
    def ForgetPassword(self, event):
        self.rootfp = Toplevel()
        self.rootfp.geometry('550x350')
        self.rootfp.config(background=self.bgColor)
        # header label
        Label(self.rootfp, text='Forget Password', font=self.headerFont, padx=10, pady=15, bg=self.bgColor,
              fg='#ffffff').pack(pady=25)

        # Frame
        self.fpframe = Frame(self.rootfp, bg=self.bgColorLite, highlightbackground=self.fgColor, highlightthickness=3,
                             padx=20, pady=20)
        self.fpframe.pack()

        self.emailLabelfp = Label(self.fpframe, text='Email :', font=('Arial', 18), padx=10, pady=10,
                                  bg=self.bgColorLite,
                                  fg=self.fgColor)
        self.emailEntryfp = Entry(self.fpframe, font=self.bodyFont, width=26)
        self.emailLabelfp.grid(row=0, column=0)
        self.emailEntryfp.grid(row=0, column=1)

        self.sendEmailfp = Button(self.rootfp, text='Get Password', font=self.buttonFont, width=12,
                                  command=self.sendEmailFunc, pady=8, padx=10, activebackground='#ffffff')
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
                messagebox.showinfo('Success',
                                    'Your password has been successfully sent on your email address. Use it to Log in', parent=self.root)
                self.rootfp.destroy()
            except:
                messagebox.showerror('Unable to send Email', 'This Email Address cannot be reached right now', parent=self.root)
                self.rootfp.destroy()

if __name__ == '__main__':
    settings(1)