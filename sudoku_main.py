# sudoku builder/solver gui

import tkinter
import tkinter.messagebox
import random

# this section contains the sudoku classes

class SudokuError(Exception):
    pass

class SudokuValue:
    '''Define a class for the sudoku numbers. These numbers need to be objects so that
        they can be referenced from multiple different lists (rows, columns, and boxes) and
        be updated via any of these lists. The values in the objects should be saved as strings.'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

class SudokuPuzzle:
    '''define a class to hold the entire sudoku puzzle'''
    def __init__(self, values_list):
        '''create and set the SudokuValue objects from the argument list. requires a list of 81
           single character strings (values) as argument. Create lists of these objects for the rows and columns.'''

        # updating self.possibleValues enables letter and symbol sudokus
        self.possibleValues = {'1', '2', '3', '4', '5', '6', '7', '8', '9', ''}
        self.possibleCharacters = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        # basic error checking of initial values
        for value in values_list:
            if value not in self.possibleValues:
                raise SudokuError('Invalid sudoku character submitted in value_list arg.')
        if len(values_list) != 81:
            raise SudokuError('value_list arg is incorrect length. must be 81.')

        # convert characters into SudokuValue objects
        self.varList = []
        for letter in ['a','b','c','d','e','f','g','h','i']:
            for num in range(1,10):
                var_string = letter + str(num)
                self.varList.append(var_string)
                
        self.varDict = {var: SudokuValue(values_list[index]) for index, var in enumerate(self.varList)}
     
        # create lists for each box, column, and row so that we can check what numbers are in each later

        self.box1 = []
        self.box2 = []
        self.box3 = []
        self.box4 = []
        self.box5 = []
        self.box6 = []
        self.box7 = []
        self.box8 = []
        self.box9 = []
           
        self.boxes = [self.box1, self.box2, self.box3, self.box4, self.box5, self.box6, self.box7, self.box8, self.box9]
        self.startingIndicies = [0,3,6,27,30,33,54,57,60]
        self.boxStarts = zip(self.boxes, self.startingIndicies)
        # adding the variable objects to the box list is a little more complex. This system should assign the correct numbers to the correct boxes.
        # using the starting index and adding values with indexes set by the list num

        # the below lookup system uses the integers in the ranges to determine the box from 0-80 (left - right, top down)
        # it then references varList to get the name of the variable (eg a1)
        # it then looks up the name in the varDict to locate the specific object
        
        for box, startIndex in self.boxStarts:
            for num in [0,1,2,9,10,11,18,19,20]:
                box.append(self.varDict[self.varList[startIndex + num]])

        # rows are simple - just add variables in order across the line
        self.rowA = [self.varDict[self.varList[index]] for index in range(9)]
        self.rowB = [self.varDict[self.varList[index]] for index in range(9,18)]
        self.rowC = [self.varDict[self.varList[index]] for index in range(18,27)]
        self.rowD = [self.varDict[self.varList[index]] for index in range(27,36)]
        self.rowE = [self.varDict[self.varList[index]] for index in range(36,45)]
        self.rowF = [self.varDict[self.varList[index]] for index in range(45,54)]
        self.rowG = [self.varDict[self.varList[index]] for index in range(54,63)]
        self.rowH = [self.varDict[self.varList[index]] for index in range(63,72)]
        self.rowI = [self.varDict[self.varList[index]] for index in range(72,81)]

        # for colums, the index just goes up in multiples of 9
        self.column1 = [self.varDict[self.varList[index]] for index in range(0,73,9)]
        self.column2 = [self.varDict[self.varList[index]] for index in range(1,74,9)]
        self.column3 = [self.varDict[self.varList[index]] for index in range(2,75,9)]
        self.column4 = [self.varDict[self.varList[index]] for index in range(3,76,9)]
        self.column5 = [self.varDict[self.varList[index]] for index in range(4,77,9)]
        self.column6 = [self.varDict[self.varList[index]] for index in range(5,78,9)]
        self.column7 = [self.varDict[self.varList[index]] for index in range(6,79,9)]
        self.column8 = [self.varDict[self.varList[index]] for index in range(7,80,9)]
        self.column9 = [self.varDict[self.varList[index]] for index in range(8,81,9)]

        # create a list of rows
        self.rows = [self.rowA, self.rowB, self.rowC, self.rowD, self.rowE, self.rowF, self.rowG,
                     self.rowH, self.rowI]

        # create a list of all groups
        self.allGroups = [self.box1, self.box2, self.box3, self.box4, self.box5, self.box6, self.box7,
                          self.box8, self.box9, self.rowA, self.rowB, self.rowC, self.rowD, self.rowE,
                          self.rowF, self.rowG, self.rowH, self.rowI, self.column1, self.column2, self.column3,
                          self.column4, self.column5, self.column6, self.column7, self.column8, self.column9]

        # check for number clashes in the starting values
        for group in self.allGroups:
            groupList = []
            for value in group:
                groupList.append(value.get())

            for character in self.possibleCharacters:
                if groupList.count(str(character)) > 1:
                    raise SudokuError('Invalid sudoku: number clash')

    # this function sets the sudoku values based on a saved list. This is required to restore the board from a backup when a recursion chain
    # hits an impossibility and needs to return to a previous level.
    def set_values(self, values_list):
        for index, var in enumerate(self.varList):
            self.varDict[var].set(values_list[index])

        
    def assign_seeds(self):
        '''this function (somewhat) randomly assignes the seed boxes. seed boxes are staticly assigned,
            however values are three of each integer randomly placed in the static box positions.'''
        valueList = [value for value in self.possibleCharacters]
        random.shuffle(valueList)
        a = valueList.pop(0)
        b = valueList.pop(0)
        c = valueList.pop(0)
        d = valueList.pop(0)
        e = valueList.pop(0)
        f = valueList.pop(0)
        g = valueList.pop(0)
        h = valueList.pop(0)
        i = valueList.pop(0)
        
        # randomisation here could be better, but needs to be done in a way that ensures the puzzle is possible
        # this configuration will always be possible, so using this for now
        self.seedValues = [h, '', '', '', '', i, c, '', a, '', '', b, d, '', g, '',
                           '', f, f, '', '', '', '', b, '', '', '', '', '', '', '', '', a,
                           '', e, '', '', e, '', i, h, '', '', g, '', '', b, '', g, '',
                           c, '', '', '', '', '', '', c, '', '', '', '', d, '', h, d, '',
                           '', '', i, '', '', '', a, '', '', '', e, '', f, '']

        self.set_values(self.seedValues)


    def remove_values(self, difficulty):
        '''this function removes values from a solved sudoku to make an unsolved puzzle.'''
        if difficulty == '1':
            initialRemove = 20
            extraRemove = 30
        elif difficulty == '2':
            initialRemove = 20
            extraRemove = 33
        elif difficulty == '3':
            initialRemove = 23
            extraRemove = 33
        elif difficulty == '4':
            initialRemove = 23
            extraRemove = 36
        elif difficulty == '5':
            initialRemove = 26
            extraRemove = 36 

        # initially, remove initialRemove number of random values

        # need to fix this as the indexes wont work as list size changes the indexes change
        values = self.backup_values()
        valueIndexes = [i for i in range(81)]
        removeValues = random.sample(valueIndexes, initialRemove)

        for choice in removeValues:
            values[choice] = ''

        self.set_values(values)

        # then, remove the 30 values with least possibilities (this should make the puzzle easier, maybe change later)
        for i in range(extraRemove):
            square = self.select_remove()
            square.set('')

    def select_remove(self):
        '''this function selects and returns the solved square with the least possibilities.'''
        minPos = 10
        for row in self.rows:
            for square in row:
                if not square.get() == '':
                    possibilities = {i for i in self.possibleCharacters}
                    for group in self.allGroups:
                        if square in group:
                            for value in group:
                                if value.get() in possibilities:
                                    possibilities.remove(value.get())

                    numPos = len(possibilities)
                    if numPos < minPos:
                        minPos = numPos
                        bestSquare = square
        return bestSquare
               

    # this is required to restore the board before checking the next possibility
    def backup_values(self):
        '''this function saves a copy of the current state of the sudoku board.''' 
        backupValues = []
        for row in self.rows:
            for square in row:
                backupValues.append(square.get())
        return backupValues

    def select_square(self):
        '''this function selects and returns the square with the least possibilities
            for solutions. it also determines whether the puzzle is complete or impossible.
            returns either "complete", "impossible", or a SudokuValue object plus the set of possibilities.'''
        minPos = 10
        for row in self.rows:
            for square in row:
                if square.get() == '':
                    possibilities = {i for i in self.possibleCharacters}
                    for group in self.allGroups:
                        if square in group:
                            for value in group:
                                if value.get() in possibilities:
                                    possibilities.remove(value.get())

                    numPos = len(possibilities)
                    if numPos < minPos:
                        minPos = numPos
                        bestSquare = square
                        bestSquarePoss = possibilities

        if minPos == 10:
            return 'completed', None
        elif minPos == 0:
            return 'impossible', None
        else:
            return bestSquare, bestSquarePoss

    def solve(self):
        '''this is a recursive function that solves the puzzle by adding values one at a time to the
            square with the least possibilities and testing whether a solution can be found'''
        backup = self.backup_values()
        square, possibilities = self.select_square()
        
        if square == 'impossible':
            return 'impossible'
        
        elif square == 'completed':
            return 'completed'

        else:
            for possibilty in possibilities:
                self.set_values(backup)
                square.set(possibilty)

                # run itself again
                if self.solve() == 'completed':
                    return 'completed'

            # if all possible values result in impossible, return to the layer above and try the next value there
            return 'impossible'


#
#
# this section contains the GUI and running code
#
#

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
            self.sudoku_instance = SudokuPuzzle(self.values_list)
            validInput = True
        except SudokuError:
            validInput = False
            tkinter.messagebox.showerror('Error!', 'Error creating sudoku. There is either a number clash or invalid symbols present.')
            
        if validInput:
            # run the solve function and either update the boxes with the solution, or advise the problem is impossible
            result = self.sudoku_instance.solve()
            if result == 'completed':
                self.update_boxes()
            elif result == 'impossible':
                tkinter.messagebox.showerror('Error!', 'This sudoku is impossible.')

    def build_sudoku(self, difficulty):
        '''create a new sudoku puzzle'''
        emptyValues = ['' for i in range(81)]
        self.sudoku_instance = SudokuPuzzle(emptyValues)
        self.sudoku_instance.assign_seeds()
        self.sudoku_instance.solve()
        self.sudoku_instance.remove_values(difficulty)
        self.update_boxes()
        
    def update_boxes(self):
        '''Update the GUI boxes with the characters from the solved SudokuPuzzle'''

        for var in self.varList:
            self.varDict[var].set(self.sudoku_instance.varDict[var].get())
            
    def clear_boxes(self):
        '''Clear all the boxes in the GUI.'''
        for box in self.sudoku_instance.rows:
            for value in box:
                value.set('')

        self.update_boxes()
   
# run everything:
gui = ProgramGUI()
