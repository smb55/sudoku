import random

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
        self.column1 = [self.varDict[self.varList[index]] for index in range(0,72,9)]
        self.column2 = [self.varDict[self.varList[index]] for index in range(1,73,9)]
        self.column3 = [self.varDict[self.varList[index]] for index in range(2,74,9)]
        self.column4 = [self.varDict[self.varList[index]] for index in range(3,75,9)]
        self.column5 = [self.varDict[self.varList[index]] for index in range(4,76,9)]
        self.column6 = [self.varDict[self.varList[index]] for index in range(5,77,9)]
        self.column7 = [self.varDict[self.varList[index]] for index in range(6,78,9)]
        self.column8 = [self.varDict[self.varList[index]] for index in range(7,79,9)]
        self.column9 = [self.varDict[self.varList[index]] for index in range(8,80,9)]

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
