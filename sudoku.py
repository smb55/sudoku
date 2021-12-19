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
        self.a1 = SudokuValue(values_list[0])
        self.a2 = SudokuValue(values_list[1])
        self.a3 = SudokuValue(values_list[2])
        self.a4 = SudokuValue(values_list[3])
        self.a5 = SudokuValue(values_list[4])
        self.a6 = SudokuValue(values_list[5])
        self.a7 = SudokuValue(values_list[6])
        self.a8 = SudokuValue(values_list[7])
        self.a9 = SudokuValue(values_list[8])
        self.b1 = SudokuValue(values_list[9])
        self.b2 = SudokuValue(values_list[10])
        self.b3 = SudokuValue(values_list[11])
        self.b4 = SudokuValue(values_list[12])
        self.b5 = SudokuValue(values_list[13])
        self.b6 = SudokuValue(values_list[14])
        self.b7 = SudokuValue(values_list[15])
        self.b8 = SudokuValue(values_list[16])
        self.b9 = SudokuValue(values_list[17])
        self.c1 = SudokuValue(values_list[18])
        self.c2 = SudokuValue(values_list[19])
        self.c3 = SudokuValue(values_list[20])
        self.c4 = SudokuValue(values_list[21])
        self.c5 = SudokuValue(values_list[22])
        self.c6 = SudokuValue(values_list[23])
        self.c7 = SudokuValue(values_list[24])
        self.c8 = SudokuValue(values_list[25])
        self.c9 = SudokuValue(values_list[26])
        self.d1 = SudokuValue(values_list[27])
        self.d2 = SudokuValue(values_list[28])
        self.d3 = SudokuValue(values_list[29])
        self.d4 = SudokuValue(values_list[30])
        self.d5 = SudokuValue(values_list[31])
        self.d6 = SudokuValue(values_list[32])
        self.d7 = SudokuValue(values_list[33])
        self.d8 = SudokuValue(values_list[34])
        self.d9 = SudokuValue(values_list[35])
        self.e1 = SudokuValue(values_list[36])
        self.e2 = SudokuValue(values_list[37])
        self.e3 = SudokuValue(values_list[38])
        self.e4 = SudokuValue(values_list[39])
        self.e5 = SudokuValue(values_list[40])
        self.e6 = SudokuValue(values_list[41])
        self.e7 = SudokuValue(values_list[42])
        self.e8 = SudokuValue(values_list[43])
        self.e9 = SudokuValue(values_list[44])
        self.f1 = SudokuValue(values_list[45])
        self.f2 = SudokuValue(values_list[46])
        self.f3 = SudokuValue(values_list[47])
        self.f4 = SudokuValue(values_list[48])
        self.f5 = SudokuValue(values_list[49])
        self.f6 = SudokuValue(values_list[50])
        self.f7 = SudokuValue(values_list[51])
        self.f8 = SudokuValue(values_list[52])
        self.f9 = SudokuValue(values_list[53])
        self.g1 = SudokuValue(values_list[54])
        self.g2 = SudokuValue(values_list[55])
        self.g3 = SudokuValue(values_list[56])
        self.g4 = SudokuValue(values_list[57])
        self.g5 = SudokuValue(values_list[58])
        self.g6 = SudokuValue(values_list[59])
        self.g7 = SudokuValue(values_list[60])
        self.g8 = SudokuValue(values_list[61])
        self.g9 = SudokuValue(values_list[62])
        self.h1 = SudokuValue(values_list[63])
        self.h2 = SudokuValue(values_list[64])
        self.h3 = SudokuValue(values_list[65])
        self.h4 = SudokuValue(values_list[66])
        self.h5 = SudokuValue(values_list[67])
        self.h6 = SudokuValue(values_list[68])
        self.h7 = SudokuValue(values_list[69])
        self.h8 = SudokuValue(values_list[70])
        self.h9 = SudokuValue(values_list[71])
        self.i1 = SudokuValue(values_list[72])
        self.i2 = SudokuValue(values_list[73])
        self.i3 = SudokuValue(values_list[74])
        self.i4 = SudokuValue(values_list[75])
        self.i5 = SudokuValue(values_list[76])
        self.i6 = SudokuValue(values_list[77])
        self.i7 = SudokuValue(values_list[78])
        self.i8 = SudokuValue(values_list[79])
        self.i9 = SudokuValue(values_list[80])

        # create lists for each box, column, and row so that we can check what numbers are in each later

        self.box1 = [self.a1, self.a2, self.a3, self.b1, self.b2, self.b3, self.c1, self.c2, self.c3]
        self.box2 = [self.a4, self.a5, self.a6, self.b4, self.b5, self.b6, self.c4, self.c5, self.c6]
        self.box3 = [self.a7, self.a8, self.a9, self.b7, self.b8, self.b9, self.c7, self.c8, self.c9]
        self.box4 = [self.d1, self.d2, self.d3, self.e1, self.e2, self.e3, self.f1, self.f2, self.f3]
        self.box5 = [self.d4, self.d5, self.d6, self.e4, self.e5, self.e6, self.f4, self.f5, self.f6]
        self.box6 = [self.d7, self.d8, self.d9, self.e7, self.e8, self.e9, self.f7, self.f8, self.f9]
        self.box7 = [self.g1, self.g2, self.g3, self.h1, self.h2, self.h3, self.i1, self.i2, self.i3]
        self.box8 = [self.g4, self.g5, self.g6, self.h4, self.h5, self.h6, self.i4, self.i5, self.i6]
        self.box9 = [self.g7, self.g8, self.g9, self.h7, self.h8, self.h9, self.i7, self.i8, self.i9]

        self.rowA = [self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9]
        self.rowB = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        self.rowC = [self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9]
        self.rowD = [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9]
        self.rowE = [self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7, self.e8, self.e9]
        self.rowF = [self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8, self.f9]
        self.rowG = [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8, self.g9]
        self.rowH = [self.h1, self.h2, self.h3, self.h4, self.h5, self.h6, self.h7, self.h8, self.h9]
        self.rowI = [self.i1, self.i2, self.i3, self.i4, self.i5, self.i6, self.i7, self.i8, self.i9]

        self.column1 = [self.a1, self.b1, self.c1, self.d1, self.e1, self.f1, self.g1, self.h1, self.i1]
        self.column2 = [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2, self.g2, self.h2, self.i2]
        self.column3 = [self.a3, self.b3, self.c3, self.d3, self.e3, self.f3, self.g3, self.h3, self.i3]
        self.column4 = [self.a4, self.b4, self.c4, self.d4, self.e4, self.f4, self.g4, self.h4, self.i4]
        self.column5 = [self.a5, self.b5, self.c5, self.d5, self.e5, self.f5, self.g5, self.h5, self.i5]
        self.column6 = [self.a6, self.b6, self.c6, self.d6, self.e6, self.f6, self.g6, self.h6, self.i6]
        self.column7 = [self.a7, self.b7, self.c7, self.d7, self.e7, self.f7, self.g7, self.h7, self.i7]
        self.column8 = [self.a8, self.b8, self.c8, self.d8, self.e8, self.f8, self.g8, self.h8, self.i8]
        self.column9 = [self.a9, self.b9, self.c9, self.d9, self.e9, self.f9, self.g9, self.h9, self.i9]

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

    # this is required to restore the board from a backup in the case of an impossible chain
    def set_values(self, values_list):
        self.a1.set(values_list[0])
        self.a2.set(values_list[1])
        self.a3.set(values_list[2])
        self.a4.set(values_list[3])
        self.a5.set(values_list[4])
        self.a6.set(values_list[5])
        self.a7.set(values_list[6])
        self.a8.set(values_list[7])
        self.a9.set(values_list[8])
        self.b1.set(values_list[9])
        self.b2.set(values_list[10])
        self.b3.set(values_list[11])
        self.b4.set(values_list[12])
        self.b5.set(values_list[13])
        self.b6.set(values_list[14])
        self.b7.set(values_list[15])
        self.b8.set(values_list[16])
        self.b9.set(values_list[17])
        self.c1.set(values_list[18])
        self.c2.set(values_list[19])
        self.c3.set(values_list[20])
        self.c4.set(values_list[21])
        self.c5.set(values_list[22])
        self.c6.set(values_list[23])
        self.c7.set(values_list[24])
        self.c8.set(values_list[25])
        self.c9.set(values_list[26])
        self.d1.set(values_list[27])
        self.d2.set(values_list[28])
        self.d3.set(values_list[29])
        self.d4.set(values_list[30])
        self.d5.set(values_list[31])
        self.d6.set(values_list[32])
        self.d7.set(values_list[33])
        self.d8.set(values_list[34])
        self.d9.set(values_list[35])
        self.e1.set(values_list[36])
        self.e2.set(values_list[37])
        self.e3.set(values_list[38])
        self.e4.set(values_list[39])
        self.e5.set(values_list[40])
        self.e6.set(values_list[41])
        self.e7.set(values_list[42])
        self.e8.set(values_list[43])
        self.e9.set(values_list[44])
        self.f1.set(values_list[45])
        self.f2.set(values_list[46])
        self.f3.set(values_list[47])
        self.f4.set(values_list[48])
        self.f5.set(values_list[49])
        self.f6.set(values_list[50])
        self.f7.set(values_list[51])
        self.f8.set(values_list[52])
        self.f9.set(values_list[53])
        self.g1.set(values_list[54])
        self.g2.set(values_list[55])
        self.g3.set(values_list[56])
        self.g4.set(values_list[57])
        self.g5.set(values_list[58])
        self.g6.set(values_list[59])
        self.g7.set(values_list[60])
        self.g8.set(values_list[61])
        self.g9.set(values_list[62])
        self.h1.set(values_list[63])
        self.h2.set(values_list[64])
        self.h3.set(values_list[65])
        self.h4.set(values_list[66])
        self.h5.set(values_list[67])
        self.h6.set(values_list[68])
        self.h7.set(values_list[69])
        self.h8.set(values_list[70])
        self.h9.set(values_list[71])
        self.i1.set(values_list[72])
        self.i2.set(values_list[73])
        self.i3.set(values_list[74])
        self.i4.set(values_list[75])
        self.i5.set(values_list[76])
        self.i6.set(values_list[77])
        self.i7.set(values_list[78])
        self.i8.set(values_list[79])
        self.i9.set(values_list[80])

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
        '''this is a recursive function that solves the puzzle by adding values
            one at a time and testing whether a solution can be found'''
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
