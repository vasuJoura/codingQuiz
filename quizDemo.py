from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkcalendar import DateEntry
from connection import Connect
from tkinter import messagebox
from tkinter import ttk
import datetime


class quiz:
    def __init__(self, id, topic):
        self.user_id = id
        self.topic = topic

        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('QUIZ & LEARN - QUIZ')
        self.root.config(background="#330051")

        # Favicon image for root window
        self.fav = PhotoImage(file='images/quiz.png', master=self.root)
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



        """TO CONTAIN THE PAGE HEADING"""
        self.titleFrame = Frame(self.root, pady=10, bg=self.bgColorDark)
        self.titleFrame.pack(fill='x')

        # Title
        self.Title = Label(self.titleFrame, text='QUIZ & LEARN', font=self.headerFont, pady=2, bg=self.bgColorDark,
                           fg=self.fgColor)
        self.Title.pack(padx=20, side='left')




        # initilize stringVar
        self.variable = StringVar()

        # By default, count = 0
        self.count = 0

        # Answers in dictionary
        self.ansList = []

        self.fetchQuestions()
        self.root.mainloop()

        # executes onli one time when the programm is called upon

    # executes onli one time when the programm is called upon
    def fetchQuestions(self):
        Q = f"select * from question where topic='{self.topic}' ORDER BY RAND() LIMIT 10"
        self.cr.execute(Q)
        self.questList = self.cr.fetchall()
        for r in self.questList:
            print(r)

        self.defineStructure()
        self.showQuestion()

    def defineStructure(self):

        self.supremeFrame = Frame(self.root, bg=self.bgColor)
        self.supremeFrame.pack(fill='both')
        # MajorFrames

        """TO CONTAIN THE THE THREE GRID FRAMES"""
        self.majorFrame1 = Frame(self.supremeFrame, bg=self.bgColor, pady=10, padx=10)
        self.majorFrame1.grid(row=0, column=0)

        """TO CONTAIN THE FIVE DAY WEATHER"""
        self.majorFrame2 = Frame(self.supremeFrame, pady=10, padx=10, bg=self.bgColor)
        self.majorFrame2.grid(row=0, column=1)

        # MainFrames in grid
        self.mainFrame1 = Frame(self.majorFrame1, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                highlightthickness=2, padx=15, pady=15, height=self.height-150, width=self.width // 3 + 100)
        self.mainFrame1.pack()
        self.mainFrame1.pack_propagate(0)

        self.mainFrame2 = Frame(self.majorFrame2, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                highlightthickness=2, padx=15, pady=15, height=self.height // 2 + 30, width=self.width //2 + 70)
        self.mainFrame2.grid(row=0, column=0, pady=15)
        self.mainFrame2.pack_propagate(0)

        self.mainFrame4 = Frame(self.majorFrame2, pady=15, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                highlightthickness=2, height=self.height // 2 - 210, width=self.width //2 + 70)
        self.mainFrame4.grid(row=1, column=0, pady=15)
        self.mainFrame4.pack_propagate(0)

    def showQuestion(self):
        # mainFrame1 for question
        self.questLabel = Label(self.mainFrame1, text=f'QUESTION {self.count+1}', font=self.subheaderFont, bg=self.bgColorLite, fg=self.fgColor)
        self.questLabel.pack()

        self.questEntry = Text(self.mainFrame1, bg=self.bgColorLite, relief='flat', fg=self.fgColor, wrap=WORD, font=self.bodyFont, height=18)
        self.questEntry.insert(0.0, f"{self.questList[self.count]['quest']}")
        self.questEntry.config(state='disabled')
        self.questEntry.pack(pady=10)

        # mainframe2 for options

        self.variable.set('a')

        # option 1

        self.option1 = Radiobutton(self.mainFrame2, text=f'A:{self.questList[self.count]["op_a"]}', variable=self.variable, value='a', bg=self.btn3,
                                   activebackground=self.btn3A, fg=self.fgColor, activeforeground=self.fgColor,
                                   font=self.bodyFont, pady=14, padx=5, justify='left', width=54, anchor='w',
                                   borderwidth=2, selectcolor=self.btn3A, relief='raised')
        self.option1.pack( pady=12)

        # option 2
        self.option2 = Radiobutton(self.mainFrame2, text=f'B:{self.questList[self.count]["op_b"]} ', variable=self.variable, value='b', bg=self.btn3,
                                   activebackground=self.btn3A, fg=self.fgColor, activeforeground=self.fgColor,
                                   font=self.bodyFont, pady=14, padx=5, justify='left', width=54, anchor='w',
                                   borderwidth=2, selectcolor=self.btn3A, relief='raised')
        self.option2.pack( pady=12)

        # option 3
        self.option3 = Radiobutton(self.mainFrame2, text=f'C:{self.questList[self.count]["op_c"]}', variable=self.variable, value='c', bg=self.btn3,
                                   activebackground=self.btn3A, fg=self.fgColor, activeforeground=self.fgColor,
                                   font=self.bodyFont, pady=14, padx=5, justify='left', width=54, anchor='w',
                                   borderwidth=2, selectcolor=self.btn3A, relief='raised')
        self.option3.pack( pady=12)

        # option 4
        self.option4 = Radiobutton(self.mainFrame2, text=f'D:{self.questList[self.count]["op_d"]}', variable=self.variable, value='d', bg=self.btn3,
                                   activebackground=self.btn3A, fg=self.fgColor, activeforeground=self.fgColor,
                                   font=self.bodyFont, pady=14, padx=5, justify='left', width=54, anchor='w',
                                   borderwidth=2, selectcolor=self.btn3A, relief='raised')
        self.option4.pack(pady=12)

        # mainframe3 for SUBMIT & RESET BUTTON
        self.submitButton = Button(self.mainFrame4, text='SUBMIT ANSWER', bg=self.btn1, fg=self.fgColor,
                                   activeforeground=self.fgColor, activebackground=self.btn1A, width=35, padx=25,
                                   font=self.subheaderFont,
                                   command=self.nextQuestion)

        self.submitButton.pack(pady=25)

    def nextQuestion(self):
        # save current answer
        ansDict = {}
        ansDict['id'] = self.questList[self.count]['id']
        ansDict['ans'] = self.variable.get()
        self.ansList.append(ansDict)
        print(self.ansList)

        if self.count < 9:
            # show next question
            self.count += 1

            # to remove the previous question
            self.supremeFrame.pack_forget()

            self.defineStructure()
            self.showQuestion()
        else:
            self.supremeFrame.pack_forget()
            self.saveResult()

    def saveResult(self):

        self.score = 0
        for i in range(0, 10):
            if self.questList[i]['ans'] == self.ansList[i]['ans']:
                print(
                    f"{self.questList[i]['ans']} == {self.ansList[i]['ans']} for Question ID {self.questList[i]['id']}")
                self.score += 1

        Q = f"insert into score values(null, '{self.user_id}','{self.topic}', '{self.score}', '{datetime.date.today()}')"
        print(Q)
        self.cr.execute(Q)
        self.conn.commit()
        self.showResult()

    def showResult(self):
        self.resultFrame = Frame(self.root, bg=self.bgColorLite, highlightbackground=self.fgColor,
                                highlightthickness=2, padx=15, pady=15, height=self.height - 150,
                                width=self.width - 100)
        self.resultFrame.pack()
        self.resultFrame.pack_propagate(0)

        self.message = Label(self.resultFrame, text="You have completed the test successfully", bg=self.bgColorLite,
                           fg=self.fgColor, font=self.subheaderFont)
        self.message.pack(pady=20)

        self.message2 = Label(self.resultFrame, text="Here is Your Score", bg=self.bgColorLite,
                             fg=self.fgColor, font=self.headerFont)
        self.message2.pack(pady=10)

        self.scoreLabel = Label(self.resultFrame, text=f'{self.score}', font=('Arial Black', 90, 'bold'), bg=self.bgColorLite,
                           fg=self.fgColor)
        self.scoreLabel.pack()

        self.logoutButton = Button(self.titleFrame, text='LOGOUT', bg=self.btn1, fg=self.fgColor,
                                   activeforeground=self.fgColor, activebackground=self.btn1A, width=10, padx=15,
                                   font=self.subheaderFont,
                                   command=lambda: self.root.destroy())
        self.logoutButton.pack(side='right', padx=60)


# quiz(1, 3)