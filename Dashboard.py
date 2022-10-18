from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkcalendar import DateEntry
from connection import Connect
from tkinter import messagebox
from tkinter import ttk
import datetime
from profile import settings

class Dashboard:
    def __init__(self, id):
        self.user_id = id

        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('QUIZ & LEARN - DASHBOARD')
        self.root.config(background="#330051")

        # Favicon image for root window
        self.fav = PhotoImage(file='images/quiz.png')
        self.root.iconphoto(False, self.fav)

        # Get screen height & width for effective use of pack and place
        self.height = int(self.root.winfo_screenheight())
        self.width = int(self.root.winfo_screenwidth())

        # DATABASE CONNECTION
        self.conn = Connect()
        self.cr = self.conn.cursor()

        # Fonts used
        self.headerFont = Font(family='UI Gothic', size=36, weight='bold')
        self.subheaderFont = Font(family='UI Gothic', size=20)
        self.bodyFont = Font(family='UI Gothic', size=16)
        self.buttonFont = Font(family='Yu Gothic', size=12)

        # Colors By Default
        self.bgColorDark = '#330051'
        self.bgColor = '#360059'
        self.bgColorLite = '#3F0066'
        self.fgColor = '#F3EBFE'

        # Button Colors
        self.btn3 = "#ff8d2c"
        self.btn3A = "#ff7e00"

        self.btn1 = "#6007ED"
        self.btn1A = "#520BD5"


        # ____TREE VIEW STYLING ____
        self.treeStyle = ttk.Style()
        self.treeStyle.configure('Treeview', background=self.fgColor, foreground='black', rowheight=48,
                                 fieldground='black')
        self.treeStyle.map('Treeview', background=[('selected', '#3F0066')])

        self.openApplication()
        self.root.mainloop()

    def openApplication(self):

        self.supremeFrame = Frame(self.root, bg=self.bgColorDark)
        self.supremeFrame.pack(fill='both')
        # MajorFrames
        """TO CONTAIN THE PAGE HEADING"""
        self.titleFrame = Frame(self.supremeFrame, pady=10, bg=self.bgColorDark)
        self.titleFrame.pack(fill='x')


        """TO CONTAIN THE FIVE DAY WEATHER"""
        self.majorFrame2 = Frame(self.supremeFrame, pady=5, bg=self.bgColorLite)
        self.majorFrame2.pack(fill='x')

        """TO CONTAIN THE THE THREE GRID FRAMES"""
        self.majorFrame1 = Frame(self.supremeFrame, bg=self.bgColor, pady=10, padx=10)
        self.majorFrame1.pack(fill='x')

        self.logoutButton = Button(self.titleFrame, text='LOGOUT', bg=self.btn1, fg=self.fgColor,
                                    activeforeground=self.fgColor, activebackground=self.btn1A, width=10, padx=15,
                                    font=self.subheaderFont,
                                    command=lambda: self.root.destroy() )
        self.logoutButton.pack(side='right', padx=60)


        # Title
        self.Title = Label(self.titleFrame, text='QUIZ & LEARN', font=self.headerFont, pady=2, bg=self.bgColorDark,
                           fg=self.fgColor)
        self.Title.pack(padx=150, side='right')

        self.settingsButton = Button(self.titleFrame, text='SETTINGS', bg=self.btn3, fg=self.fgColor,
                                    activeforeground=self.fgColor, activebackground=self.btn3A, width=10, padx=15,
                                    font=self.subheaderFont,
                                    command=lambda k=self.user_id : settings(k))
        self.settingsButton.pack(side='right', padx=60)
        # MainFrames in grid
        self.mainFrame1 = Frame(self.majorFrame1, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                highlightthickness=2, padx=15, pady=10, height=330, width=self.width // 3 - 35)
        self.mainFrame1.grid(row=0, column=2, padx=15)
        self.mainFrame1.pack_propagate(0)

        self.mainFrame2 = Frame(self.majorFrame1, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                highlightthickness=2, padx=15, pady=10, height=330, width=self.width // 3 * 2 - 40)
        self.mainFrame2.grid(row=0, column=1, padx=15)
        self.mainFrame2.pack_propagate(0)



        # MainFrame To Accomodate the 5 day weather
        self.mainFrame4 = Frame(self.majorFrame2, pady=15, bg=self.bgColor, highlightbackground=self.fgColor,
                                highlightthickness=2, width=self.width - 50, height=210)
        self.mainFrame4.pack(pady=15)
        self.mainFrame4.pack_propagate(0)

        self.subjects()
        self.scoreCard()
        self.profileInfo()

    def removeApplication(self):
        self.supremeFrame.pack_forget()


    """_________________________________________________________________________________________________________________
                                                       WEATHER AREA AND RELATED FUNCTIONS
           ____________________________________________________________________________________________________________________"""

    """ SHOW THE CONTENTS OF WEATHER FRAME """
    def subjects(self):
        # Content in mainFrame1

        self.titleF1 = Label(self.mainFrame1, text='TAKE TEST', font=self.subheaderFont, bg=self.bgColorLite, fg=self.fgColor)
        self.titleF1.pack()

        # ListBox Containing all the Cities Present in the City Table
        self.subjectBox = Listbox(self.mainFrame1, bg=self.bgColor, fg=self.fgColor, selectbackground=self.bgColorDark,
                                  relief=FLAT, font=self.bodyFont, selectmode='SINGLE ', height=15, width=50,
                                  cursor='plus')

        self.subjectBox.pack()
        self.getSubject()

    def getSubject(self):

        q = f'select * from topic'
        self.cr.execute(q)
        result = self.cr.fetchall()
        print(result)
        self.subjectBox.delete(0, END)
        c = 1
        for r in result:
            self.subjectBox.insert(c, r['name'])
            c += 1


    """_________________________________________________________________________________________________________________
                                                   CITIES AREA AND RELATED FUNCTIONS
       ____________________________________________________________________________________________________________________"""

    def scoreCard(self):
        # Frame to contain the title as well as the add button
        self.titleFrameF2 = Label(self.mainFrame2,  bg=self.bgColorLite, fg=self.fgColor)
        self.titleFrameF2.pack()

        # Frame Title
        self.titleF2 = Label(self.titleFrameF2, text='SCORE CARD', font=self.subheaderFont,
                             bg=self.bgColorLite, fg=self.fgColor)
        self.titleF2.grid(row=0, column=0, sticky="w", padx=0)

        # Treeview
        self.scoreTable = ttk.Treeview(self.mainFrame2)
        self.scoreTable['column'] = ('subject', 'date', 'marks', 'totalMarks')

        self.scoreTable.column('#0', width=0)
        self.scoreTable.column('subject', width=200, anchor=CENTER)
        self.scoreTable.column('date', width=200, anchor=CENTER)
        self.scoreTable.column('marks', width=150, anchor=CENTER)
        self.scoreTable.column('totalMarks', width=150, anchor=CENTER)

        self.scoreTable.heading('subject', text='SUBJECT', anchor=CENTER)
        self.scoreTable.heading('date', text='DATE', anchor=CENTER)
        self.scoreTable.heading('marks', text='MARKS', anchor=CENTER)
        self.scoreTable.heading('totalMarks', text='OUT OF', anchor=CENTER)


        self.scoreTable['show'] = 'headings'
        self.scoreTable.pack(pady=20)
        # self.getScore()

        self.scoreTable.pack()


    # def getScore(self):
    #
    #     q = f"select * from topic where user_id='{self.user_id}'"
    #     self.cr.execute(q)
    #     result = self.cr.fetchall()
    #     print(result)
    #     for i in self.scoreTable.get_children():
    #         self.scoreTable.delete(i)
    #     count = 0
    #     for i in result:
    #         self.scoreTable.insert('', index=count, values=i)
    #         count += 1


    """_________________________________________________________________________________________________________________
                                                   FIVE DAY WEATHER AREA AND RELATED FUNCTIONS
       ____________________________________________________________________________________________________________________"""
    def profileInfo(self):
        self.titleF3 = Label(self.mainFrame4, text='PROFILE', font=self.subheaderFont,
                             bg=self.bgColor, fg=self.fgColor)
        self.titleF3.pack()

        # container Frame
        self.containerFrame = Frame(self.mainFrame4, bg=self.bgColorLite, pady=15, padx=15,  highlightbackground=self.fgColor,
                                highlightthickness=2, height=200, width=self.width-10)
        self.containerFrame.pack(padx=10)
        self.containerFrame.pack_propagate(0)

        # Name Frame
        self.infoFrame1 = Frame(self.containerFrame, bg=self.bgColorLite, height=200, width=self.width//4-25)
        self.infoFrame1.pack(side='left', anchor='w')
        self.infoFrame1.pack_propagate(0)

        # Ruler frame
        self.rulerFrame1 = Frame(self.containerFrame, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                 highlightthickness=2, height=100, padx=5)
        self.rulerFrame1.pack(side='left', anchor='w')
        self.rulerFrame1.pack_propagate(0)

        # Total Test Frame
        self.infoFrame2 = Frame(self.containerFrame, bg=self.bgColorLite, height=200, width=self.width//4-25)
        self.infoFrame2.pack(side='left', anchor='w')
        self.infoFrame2.pack_propagate(0)

        # Ruler frame
        self.rulerFrame2 = Frame(self.containerFrame, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                 highlightthickness=2, height=100, padx=5)
        self.rulerFrame2.pack(side='left', anchor='w')
        self.rulerFrame2.pack_propagate(0)

        # Highest marks Frame
        self.infoFrame3 = Frame(self.containerFrame, bg=self.bgColorLite, height=200, width=self.width//4-25)
        self.infoFrame3.pack(side='left', anchor='w')
        self.infoFrame3.pack_propagate(0)

        # Ruler frame
        self.rulerFrame3 = Frame(self.containerFrame, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                 highlightthickness=2, height=100, padx=5)
        self.rulerFrame3.pack(side='left', anchor='w')
        self.rulerFrame3.pack_propagate(0)

        # Average marks Frame
        self.infoFrame4 = Frame(self.containerFrame, bg=self.bgColorLite, height=200, width=self.width//4-25)
        self.infoFrame4.pack(side='left', anchor='w')
        self.infoFrame4.pack_propagate(0)

        # inside self.infoFrame1 (name)
        self.userNameLabel = Label(self.infoFrame1, text='NAME', font=self.bodyFont, bg=self.bgColorLite, fg=self.fgColor)
        self.userNameLabel.pack()

        self.userNameValue = Label(self.infoFrame1, text='DUMMY', font=self.subheaderFont, bg=self.bgColorLite,
                                   fg=self.fgColor, pady=20)
        self.userNameValue.pack()

        # inside self.infoFrame2 (total test)
        self.userTestLabel = Label(self.infoFrame2, text='TESTS TAKEN', font=self.bodyFont, bg=self.bgColorLite,
                                   fg=self.fgColor)
        self.userTestLabel.pack()

        # inside self.infoFrame3 (HIGHEST)
        self.userHMarksLabel = Label(self.infoFrame3, text='HIGHEST MARKS', font=self.bodyFont, bg=self.bgColorLite,
                                   fg=self.fgColor)
        self.userHMarksLabel.pack()

        # inside self.infoFrame3 (HIGHEST)
        self.userAMarksLabel = Label(self.infoFrame4, text='AVERAGE MARKS', font=self.bodyFont,
                                     bg=self.bgColorLite,
                                     fg=self.fgColor)
        self.userAMarksLabel.pack()

    def showprofileInfo(self):
       pass

    def showError5D(self):
        pass

    def getWeather(self, event):
        pass


# Dashboard(1)