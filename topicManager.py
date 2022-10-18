from tkinter import *

import adminProfile
from connection import Connect
from tkinter import ttk
from tkinter.font import Font
import tkinter.messagebox as msg
import questions

class topic:
    def __init__(self,id):
        self.id = id
        # DATABASE CONNECTION
        self.conn = Connect()
        self.cr = self.conn.cursor()

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

        self.root = Toplevel()
        self.root.geometry('600x600')
        self.root.state('zoomed')
        self.root.title('ONLINE QUIZ - TOPIC MANAGER')
        self.root.config(background=self.bgColor)

        # navbar
        self.NavBar = Menu(self.root)

        self.TopicMenu = Menu(self.NavBar, tearoff=0)  # Sub Menu 1
        self.QuestionMenu = Menu(self.NavBar, tearoff=0)
        self.SettingsMenu = Menu(self.NavBar, tearoff=0)
        self.root.config(menu=self.NavBar)

        self.NavBar.add_cascade(label='          TOPIC          ', menu=self.TopicMenu)
        self.NavBar.add_cascade(label='        QUESTIONS        ', menu=self.QuestionMenu)
        self.NavBar.add_cascade(label='         SETTINGS        ', menu=self.SettingsMenu)

        self.TopicMenu.add_command(label='MANAGE TOPICS')
        self.QuestionMenu.add_command(label='MANAGE QUESTIONS', command=self.redirectQuestions)
        self.SettingsMenu.add_command(label='PROFILE', command=self.redirectProfile)

        # ____TREE VIEW STYLING ____
        self.treeStyle = ttk.Style()
        self.treeStyle.configure('Treeview', background=self.fgColor, foreground='black', rowheight=40,
                                 fieldground='black')
        self.treeStyle.map('Treeview', background=[('selected', '#3F0066')])

        # Fonts used
        self.headerFont = Font(family='UI Gothic', size=36, weight='bold')
        self.subheaderFont = Font(family='UI Gothic', size=20)
        self.bodyFont = Font(family='UI Gothic', size=16)
        self.buttonFont = Font(family='Yu Gothic', size=12)

        # STRUCTURE___________________________________
        self.title = Label(self.root, font=self.headerFont, bg=self.bgColor, fg=self.fgColor, text="Manage Topics")
        self.title.pack(pady=20)

        self.table = ttk.Treeview(self.root)
        self.table['columns'] = ('Question_id', 'Question',)

        self.table.column('Question_id', width=200, anchor=CENTER)
        self.table.column('Question', width=440, anchor=CENTER)


        self.table.heading('Question_id', text="Topic ID")
        self.table.heading('Question', text="Name")


        self.table.config(show='headings')
        self.table.pack()
        self.table.bind('<Double-1>', self.deleteQuestion)
        self.getValues()

        self.buttonFrame = Frame(self.root, bg=self.bgColorLite, pady=20, padx=20, highlightcolor=self.fgColor, highlightthickness=2)
        self.buttonFrame.pack(pady=20)

        # Buttons
        self.addQuestion = Button(self.buttonFrame, bg=self.btn1, fg=self.fgColor,activebackground=self.btn1A,activeforeground=self.fgColor, text='ADD NEW', width=15, font=self.buttonFont , command=self.openAddQuestionForm)
        self.addQuestion.grid(row=0, column=0, padx=20)

        self.refreshQuestion = Button(self.buttonFrame, bg=self.btn1, fg=self.fgColor, activebackground=self.btn1A,
                                  activeforeground=self.fgColor, text='REFRESH', width=15, font=self.buttonFont,command=self.getValues)
        self.refreshQuestion.grid(row=0, column=1, padx=20)

        self.exit = Button(self.buttonFrame, bg=self.btn3, fg=self.fgColor, activebackground=self.btn3A,
                                  activeforeground=self.fgColor, text='EXIT', width=15, font=self.buttonFont, command = lambda: self.root.destroy())
        self.exit.grid(row=0, column=2, padx=20)

        self.root.mainloop()

    def redirectProfile(self):
        self.root.destroy()
        adminProfile.settings(self.id)


    def redirectQuestions(self):
        self.root.destroy()
        questions.Questions(self.id)


    def getValues(self):
        Q = f"select * from topic"
        self.cr.execute(Q)
        result = self.cr.fetchall()

        for i in self.table.get_children():
            self.table.delete(i)
        count = 0

        for j in result:
            que = [j['id'], j['name']]
            self.table.insert('', count, values=que)


    def deleteQuestion(self, event):
        self.values = self.table.item(self.table.selection())['values']
        print(self.values)
        option = msg.askokcancel("DELETE TOPIC",f"Are u sure You want to delete This Topic", parent=self.root)
        if option:
            q = f"delete from topic where id='{self.values[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getValues()
        else:
            msg.showinfo('ACTION CANCELLED', 'The selected Topic is not deleted', parent=self.root)


#     __________________________________________________________________________________________
    def openAddQuestionForm(self):
        self.addFrom = Toplevel()
        self.addFrom.geometry('800x800')
        self.addFrom.title('ONLINE QUIZ - ADD TOPIC')
        self.addFrom.config(background=self.bgColor)

        self.titleAF = Label(self.addFrom, font=self.headerFont, bg=self.bgColor, fg=self.fgColor, text="Add Topic")
        self.titleAF.pack(pady=20)

        self.formFrame = Frame(self.addFrom, bg=self.bgColorLite, pady=20, padx=20, highlightcolor=self.fgColor,
                                 highlightthickness=2)
        self.formFrame.pack(pady=20)


        # QUESTION
        self.questionLabelAF = Label(self.formFrame, font=self.bodyFont, bg=self.bgColorLite, fg=self.fgColor, text="Add Topic")
        self.questionLabelAF.grid(row=0, column=0, padx=20, pady=5, sticky='nw')

        self.questionEntryAF = Text(self.formFrame, font=self.bodyFont, height=4, width=35)
        self.questionEntryAF.grid(row=0, column=1, padx=20, pady=5)


        self.buttonFrameAF = Frame(self.addFrom, bg=self.bgColorLite, pady=20, padx=20, highlightcolor=self.fgColor,
                                 highlightthickness=2)
        self.buttonFrameAF.pack(pady=20)

        # Buttons
        self.addQuestionAF = Button(self.buttonFrameAF, bg=self.btn1, fg=self.fgColor, activebackground=self.btn1A,
                                  activeforeground=self.fgColor, text='SUBMIT', width=15, font=self.buttonFont,
                                  command=self.submitQuestion)
        self.addQuestionAF.grid(row=0, column=0, padx=20)

        self.refreshQuestionAF = Button(self.buttonFrameAF, bg=self.btn1, fg=self.fgColor, activebackground=self.btn1A,
                                      activeforeground=self.fgColor, text='RESET', width=15, font=self.buttonFont, command=self.resetForm)
        self.refreshQuestionAF.grid(row=0, column=1, padx=20)

        self.exitAF = Button(self.buttonFrameAF, bg=self.btn3, fg=self.fgColor, activebackground=self.btn3A,
                           activeforeground=self.fgColor, text='EXIT', width=15, font=self.buttonFont, command=lambda :self.addFrom.destroy())
        self.exitAF.grid(row=0, column=2, padx=20)

        self.addFrom.mainloop()


    # FUNCTION TO GET FK VALUES FROM PARENT TABLE AND PASS IT TO COMBOBOX

    def resetForm(self):
        self.questionEntryAF.delete('0.0', END)


    def submitQuestion(self):

        # CODE TO GET ID FROM THE TOPIC TABLE USING NAME
        quest = self.questionEntryAF.get("1.0", 'end-1c')
        q = f"select * from topic where name = '{quest}'"
        self.cr.execute(q)
        result = self.cr.fetchall()
        print(result)

        if len(result) == 0:

            S = f"insert into topic values(null, '{quest}')"
            print(S)
            self.cr.execute(S)
            self.conn.commit()
            self.resetForm()
            self.getValues()
            msg.showinfo('ACTION SUCCESSFUL', 'Topic Successfully added', parent=self.root)

        else:
            msg.showerror('ACTION FAILED', 'Topic Exists Already', parent=self.root)









if __name__ == '__main__':
    topic()

