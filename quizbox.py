import tkinter
import tkinter.messagebox


class ProgramGUI: # define a ProgramGUI class
    def __init__(self):        
        self.main = tkinter.Tk()
        self.main.title('Quiz Box')

        self.top = tkinter.Frame(self.main, padx=8, pady=4)
        self.middle = tkinter.Frame(self.main)
        self.bottom = tkinter.Frame(self.main, padx=8, pady=4)

        self.heightPrompt = tkinter.Label(self.top, width=25, height=2, justify='right', text='Question text Goes here')
        self.heightPrompt.pack()
        self.heightPrompt = tkinter.Label(self.top, width=25, height=2, text='Timer')
        self.heightPrompt.pack()

        self.answer1 = tkinter.Button(self.middle, text='Answer1', width=10, command=self.showBox)
        self.answer2 = tkinter.Button(self.middle, text='Answer2', width=10, command=self.showForm)
        self.answer3 = tkinter.Button(self.middle, text='Answer3', width=10, command=self.showBox)
        self.answer4 = tkinter.Button(self.middle, text='Answer4', width=10, command=self.showBox)

        self.answer1.pack(side='left')
        self.answer2.pack(side='left')
        self.answer3.pack(side='left')
        self.answer4.pack(side='left')

        self.score = tkinter.Label(self.bottom, width=6, height=2, justify='right', text='Score:')
        self.score.pack(side='left')
        self.score1 = tkinter.Label(self.bottom, height=2, text='0')
        self.score1.pack(side='left')
        

        self.top.pack()
        self.middle.pack()
        self.bottom.pack()
        tkinter.mainloop()

    def showBox(self):
        tkinter.messagebox.showinfo('Well Done', 'You clicked it!')
    def showForm(self):
        tkinter.messagebox.showinfo('Well Done', 'You clicked it!')


gui = ProgramGUI() # create a ProgramGUI object
