# sudoku builder/solver gui

import tkinter
import tkinter.messagebox
import sudoku

class ProgramGUI:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('Sudoku Builder')

        # initialise attributes
        fontDetails = 'Calibri 14'

        self.difficulty = tkinter.StringVar()
        self.difficulty.set('1')

        # create 81 StringVar()
        self.varList = []
        for letter in ['a','b','c','d','e','f','g','h','i']:
            for num in range(1,10):
                var_string = letter + str(num)
                self.varList.append(var_string)
        self.varDict = {var: tkinter.StringVar() for var in self.varList}

        #create main frames
        self.headingFrame = tkinter.Frame(self.main)
        self.top = tkinter.Frame(self.main)
        self.middle = tkinter.Frame(self.main)
        self.bottom = tkinter.Frame(self.main)
        self.bottom2 = tkinter.Frame(self.main)
        self.difficultyFrame = tkinter.Frame(self.main)

        #fill the heading frame
        self.headingLabel = tkinter.Label(self.headingFrame, text='Create or Solve a Sudoku:', font='Calibri 16 bold').pack(side='left')

        #fill the bottom2 frame
        self.createButton = tkinter.Button(self.bottom2, text='Create', font='Calibri 16 bold', command=lambda: self.build_sudoku(self.difficulty.get())).pack(side='left', padx=15)
        self.solveButton = tkinter.Button(self.bottom2, text='Solve', font='Calibri 16 bold', command=lambda: self.solve_sudoku()).pack(side='left', padx=15)
        self.clearButton = tkinter.Button(self.bottom2, text='Clear', font='Calibri 16 bold', command=lambda: self.clear_boxes()).pack(side='left', padx=15)

        #fill the bottom3 frame
        self.difficultyLabel = tkinter.Label(self.difficultyFrame, text='Difficulty:', font='Calibri 14 bold').pack(side='left')
        tkinter.Radiobutton(self.difficultyFrame, text='Easy', variable=self.difficulty, value='1').pack(side='left')
        tkinter.Radiobutton(self.difficultyFrame, text='Medium', variable=self.difficulty, value='2').pack(side='left')
        tkinter.Radiobutton(self.difficultyFrame, text='Hard', variable=self.difficulty, value='3').pack(side='left')
        tkinter.Radiobutton(self.difficultyFrame, text='Extreme', variable=self.difficulty, value='4').pack(side='left')
        tkinter.Radiobutton(self.difficultyFrame, text='Insane', variable=self.difficulty, value='5').pack(side='left')

        #create the nine square frames        
        self.topLeft = tkinter.Frame(self.top)
        self.topMiddle = tkinter.Frame(self.top)
        self.topRight = tkinter.Frame(self.top)
        self.middleLeft = tkinter.Frame(self.middle)
        self.middleMiddle = tkinter.Frame(self.middle)
        self.middleRight = tkinter.Frame(self.middle)
        self.bottomLeft = tkinter.Frame(self.bottom)
        self.bottomMiddle = tkinter.Frame(self.bottom)
        self.bottomRight = tkinter.Frame(self.bottom)
        
        # create rows inside squares
        self.rowList = ['topLeftTop', 'topLeftMid', 'topLeftBottom', 'topMiddleTop', 'topMiddleMid', 'topMiddleBottom', 'topRightTop', 'topRightMid', 'topRightBottom', 'middleLeftTop', 'middleLeftMid', 'middleLeftBottom',
                   'middleMiddleTop', 'middleMiddleMid', 'middleMiddleBottom', 'middleRightTop', 'middleRightMid', 'middleRightBottom', 'bottomLeftTop', 'bottomLeftMid', 'bottomLeftBottom', 'bottomMiddleTop',
                   'bottomMiddleMid', 'bottomMiddleBottom', 'bottomRightTop', 'bottomRightMid', 'bottomRightBottom']

        self.rowList2 = ['topLeftTop', 'topMiddleTop', 'topRightTop', 'topLeftMid', 'topMiddleMid',  'topRightMid',  'topLeftBottom', 'topMiddleBottom', 'topRightBottom', 'middleLeftTop', 'middleMiddleTop', 'middleRightTop',
                        'middleLeftMid', 'middleMiddleMid', 'middleRightMid', 'middleLeftBottom', 'middleMiddleBottom', 'middleRightBottom', 'bottomLeftTop', 'bottomMiddleTop', 'bottomRightTop', 'bottomLeftMid',
                        'bottomMiddleMid','bottomRightMid', 'bottomLeftBottom', 'bottomMiddleBottom', 'bottomRightBottom']
        
        self.squareList = [self.topLeft, self.topMiddle, self.topRight, self.middleLeft, self.middleMiddle, self.middleRight, self.bottomLeft, self.bottomMiddle, self.bottomRight]
        # there are three rows in each square, so in order to match rows to squares there needs to be three of each square in the list
        self.squareList_exp = []
        for square in self.squareList:
            self.squareList_exp.append(square)
            self.squareList_exp.append(square)
            self.squareList_exp.append(square)

        self.rowDict = {row: tkinter.Frame(square) for row, square in zip(self.rowList, self.squareList_exp)}
        
        #fill rows
        self.rowList_exp = []
        for row in self.rowList2:
            self.rowList_exp.append(self.rowDict[row])
            self.rowList_exp.append(self.rowDict[row])
            self.rowList_exp.append(self.rowDict[row])

        self.entryDict = {var: tkinter.Entry(row, width=3, textvariable=self.varDict[var], font=fontDetails, justify='center').pack(side='left', padx=1, pady=1) for var, row in zip(self.varList, self.rowList_exp)}
                               
        #pack rows
        for row in self.rowList:
            self.rowDict[row].pack(side='top')
        
        #pack squares and heading        
        for square in self.squareList:
            square.pack(side='left', padx=2)

        self.headingFrame.pack(side='top', padx=1, pady=1)
        self.top.pack(side='top', padx=1, pady=1)
        self.middle.pack(side='top', padx=1, pady=1)
        self.bottom.pack(side='top', padx=1, pady=1)
        self.bottom2.pack(side='top', pady=10)
        self.difficultyFrame.pack(side='top', pady=10)

        tkinter.mainloop()

    def solve_sudoku(self):
        # create a list of values to create the SudokuPuzzle object with
        self.values_list = [self.varDict[var].get() for var in self.varList]

        # create the SudokuPuzzle. Shows error dialoge if bad values are submitted.
        try:
            self.sudoku = sudoku.SudokuPuzzle(self.values_list)
            validInput = True
        except sudoku.SudokuError:
            validInput = False
            tkinter.messagebox.showerror('Error!', 'Error creating sudoku. There is either a number clash or invalid symbols present.')
            
        if validInput:
            # run the solve function and either update the boxes with the solution, or advise the problem is impossible
            result = self.sudoku.solve()
            if result == 'completed':
                self.update_boxes()
            elif result == 'impossible':
                tkinter.messagebox.showerror('Error!', 'This sudoku is impossible.')

    def build_sudoku(self, difficulty):
        '''create a new sudoku puzzle'''
        emptyValues = ['' for i in range(81)]
        self.sudoku = sudoku.SudokuPuzzle(emptyValues)
        self.sudoku.assign_seeds()
        self.sudoku.solve()
        self.sudoku.remove_values(difficulty)
        self.update_boxes()
        
    def update_boxes(self):
        '''Update the GUI boxes with the characters from the solved SudokuPuzzle'''

        for var in self.varList:
            self.varDict[var].set(self.sudoku.varDict[var].get())
            
    def clear_boxes(self):
        '''Clear all the boxes in the GUI.'''
        for box in self.sudoku.rows:
            for value in box:
                value.set('')

        self.update_boxes()
   
# run everything:
gui = ProgramGUI()
