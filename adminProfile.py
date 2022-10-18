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
import questions
import topicManager
from changeDate import changedate


class settings:

    def __init__(self, id):
        self.id = id

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



        self.root = Toplevel()
        self.root.state('zoomed')
        self.root.title('QUIZ & LEARN - ADMIN PROFILE')
        self.root.config(background='#320052')

        # navbar
        self.NavBar = Menu(self.root)

        self.TopicMenu = Menu(self.NavBar, tearoff=0)  # Sub Menu 1
        self.QuestionMenu = Menu(self.NavBar, tearoff=0)
        self.SettingsMenu = Menu(self.NavBar, tearoff=0)
        self.root.config(menu=self.NavBar)

        self.NavBar.add_cascade(label='          TOPIC          ', menu=self.TopicMenu)
        self.NavBar.add_cascade(label='        QUESTIONS        ', menu=self.QuestionMenu)
        self.NavBar.add_cascade(label='         SETTINGS        ', menu=self.SettingsMenu)

        self.TopicMenu.add_command(label='MANAGE TOPICS', command=self.redirectTopic)
        self.QuestionMenu.add_command(label='MANAGE QUESTIONS', command=self.redirectQuestions)
        self.SettingsMenu.add_command(label='PROFILE')

        # Favicon image for root window
        self.fav = PhotoImage(file='images/quiz.png', master=self.root)
        self.root.iconphoto(False, self.fav)

        # Get screen height & width for effective use of pack and place
        height = int(self.root.winfo_screenheight())
        width = int(self.root.winfo_screenwidth())

        # DATABASE CONNECTION
        self.conn = Connect()
        self.cr = self.conn.cursor()

        # Mainframes for Signup Page
        self.mainFrame1 = Frame(self.root, bg="#39005D")
        self.mainFrame2 = Frame(self.root, bg="#39005D")

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
        Label(self.mainFrame2, font=self.headerFont, bg=self.bgColor, fg="#ffffff", text='ADMIN PROFILE').pack(
            anchor='w', pady=15)
        self.callChangePasswordForm()

        self.root.mainloop()

    def callChangePasswordForm(self):
        self.changePasswordForm()

    def redirectQuestions(self):
        self.root.destroy()
        questions.Questions(self.id)

    def redirectTopic(self):
        self.root.destroy()
        topicManager.topic(self.id)


    def destroy(self):
        self.root.destroy()



    def resetChangePassword(self):
        self.oldPassword.delete(0, 'end')
        self.newPassword.delete(0, 'end')
        self.newPassword2.delete(0, 'end')

    """A FUNCTION TO LOAD THE CONTENTS OF THE SIGNUP FORM"""



    """A FUNCTION TO LOAD THE CNTENTS OF THE LOGIN FORM"""

    def changePasswordForm(self):

        # Frames

        self.buttonFrameCP = Frame(self.mainFrame2, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                   highlightthickness=3,
                                   pady=5, padx=10)
        self.buttonFrameCP.pack(anchor='w', pady=5)

        # Buttons

        # self.settings = Button(self.buttonFrameCP, text='Settings', font=self.buttonFont, padx=31, pady=5,
        #                        bg=self.btn3,
        #                        fg=self.fgColor, activebackground=self.btn3A, activeforeground=self.fgColor,
        #                        command=self.callUpdateProfileForm)
        # self.settings.pack(side='left', padx=15, pady=5)

        self.Password = Button(self.buttonFrameCP, text='Password',width=12, font=self.buttonFont,fg=self.fgColor,activeforeground=self.fgColor,bg=self.btn3, activebackground=self.btn3A, padx=30, pady=5)
        self.Password.pack(side='left', padx=28, pady=5)

        self.Exit = Button(self.buttonFrameCP, text='Logout',width=12, font=self.buttonFont, padx=31, pady=5,
                           bg=self.btn1, fg=self.fgColor, activeforeground=self.fgColor,
                           activebackground=self.btn1A, command=self.destroy)
        self.Exit.pack(side='left', padx=28, pady=5)

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



    def changePassword(self):
        op = self.oldPassword.get()
        np = self.newPassword.get()
        np2 = self.newPassword2.get()

        n = f"select * from admin where id = '{self.id}'"
        self.cr.execute(n)
        self.userDetail = self.cr.fetchall()

        if op == self.userDetail[0]['password']:
            if np == np2:
                if len(np) > 8:
                    s = f"update admin set password = '{np}' where id = '{self.id}'"
                    self.cr.execute(s)
                    self.conn.commit()
                    self.resetChangePassword()
                    messagebox.showinfo('PASSWORD CHANGED SUCCESSFULLY!!',
                                        'Your password has been changed successfully', parent=self.root)

                else:
                    messagebox.showerror('failed to change password', 'Please choose a longer passwords ', parent=self.root)
            else:
                messagebox.showerror('failed to change password', 'the two password fields do not match', parent=self.root)
        else:
            messagebox.showerror('failed to change password', 'incorrect password', parent=self.root)

    # SIGNUP & ITS CHECKS ______________________________________________________________________________________________


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