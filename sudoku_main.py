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
        
        self.a1 = tkinter.StringVar()
        self.a2 = tkinter.StringVar()
        self.a3 = tkinter.StringVar()
        self.a4 = tkinter.StringVar()
        self.a5 = tkinter.StringVar()
        self.a6 = tkinter.StringVar()
        self.a7 = tkinter.StringVar()
        self.a8 = tkinter.StringVar()
        self.a9 = tkinter.StringVar()
        self.b1 = tkinter.StringVar()
        self.b2 = tkinter.StringVar()
        self.b3 = tkinter.StringVar()
        self.b4 = tkinter.StringVar()
        self.b5 = tkinter.StringVar()
        self.b6 = tkinter.StringVar()
        self.b7 = tkinter.StringVar()
        self.b8 = tkinter.StringVar()
        self.b9 = tkinter.StringVar()
        self.c1 = tkinter.StringVar()
        self.c2 = tkinter.StringVar()
        self.c3 = tkinter.StringVar()
        self.c4 = tkinter.StringVar()
        self.c5 = tkinter.StringVar()
        self.c6 = tkinter.StringVar()
        self.c7 = tkinter.StringVar()
        self.c8 = tkinter.StringVar()
        self.c9 = tkinter.StringVar()
        self.d1 = tkinter.StringVar()
        self.d2 = tkinter.StringVar()
        self.d3 = tkinter.StringVar()
        self.d4 = tkinter.StringVar()
        self.d5 = tkinter.StringVar()
        self.d6 = tkinter.StringVar()
        self.d7 = tkinter.StringVar()
        self.d8 = tkinter.StringVar()
        self.d9 = tkinter.StringVar()
        self.e1 = tkinter.StringVar()
        self.e2 = tkinter.StringVar()
        self.e3 = tkinter.StringVar()
        self.e4 = tkinter.StringVar()
        self.e5 = tkinter.StringVar()
        self.e6 = tkinter.StringVar()
        self.e7 = tkinter.StringVar()
        self.e8 = tkinter.StringVar()
        self.e9 = tkinter.StringVar()
        self.f1 = tkinter.StringVar()
        self.f2 = tkinter.StringVar()
        self.f3 = tkinter.StringVar()
        self.f4 = tkinter.StringVar()
        self.f5 = tkinter.StringVar()
        self.f6 = tkinter.StringVar()
        self.f7 = tkinter.StringVar()
        self.f8 = tkinter.StringVar()
        self.f9 = tkinter.StringVar()
        self.g1 = tkinter.StringVar()
        self.g2 = tkinter.StringVar()
        self.g3 = tkinter.StringVar()
        self.g4 = tkinter.StringVar()
        self.g5 = tkinter.StringVar()
        self.g6 = tkinter.StringVar()
        self.g7 = tkinter.StringVar()
        self.g8 = tkinter.StringVar()
        self.g9 = tkinter.StringVar()
        self.h1 = tkinter.StringVar()
        self.h2 = tkinter.StringVar()
        self.h3 = tkinter.StringVar()
        self.h4 = tkinter.StringVar()
        self.h5 = tkinter.StringVar()
        self.h6 = tkinter.StringVar()
        self.h7 = tkinter.StringVar()
        self.h8 = tkinter.StringVar()
        self.h9 = tkinter.StringVar()
        self.i1 = tkinter.StringVar()
        self.i2 = tkinter.StringVar()
        self.i3 = tkinter.StringVar()
        self.i4 = tkinter.StringVar()
        self.i5 = tkinter.StringVar()
        self.i6 = tkinter.StringVar()
        self.i7 = tkinter.StringVar()
        self.i8 = tkinter.StringVar()
        self.i9 = tkinter.StringVar()

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
        self.topLeftTop = tkinter.Frame(self.topLeft)
        self.topLeftMid = tkinter.Frame(self.topLeft)
        self.topLeftBottom = tkinter.Frame(self.topLeft)

        self.topMiddleTop = tkinter.Frame(self.topMiddle)
        self.topMiddleMid = tkinter.Frame(self.topMiddle)
        self.topMiddleBottom = tkinter.Frame(self.topMiddle)

        self.topRightTop = tkinter.Frame(self.topRight)
        self.topRightMid = tkinter.Frame(self.topRight)
        self.topRightBottom = tkinter.Frame(self.topRight)

        self.middleLeftTop = tkinter.Frame(self.middleLeft)
        self.middleLeftMid = tkinter.Frame(self.middleLeft)
        self.middleLeftBottom = tkinter.Frame(self.middleLeft)

        self.middleMiddleTop = tkinter.Frame(self.middleMiddle)
        self.middleMiddleMid = tkinter.Frame(self.middleMiddle)
        self.middleMiddleBottom = tkinter.Frame(self.middleMiddle)

        self.middleRightTop = tkinter.Frame(self.middleRight)
        self.middleRightMid = tkinter.Frame(self.middleRight)
        self.middleRightBottom = tkinter.Frame(self.middleRight)

        self.bottomLeftTop = tkinter.Frame(self.bottomLeft)
        self.bottomLeftMid = tkinter.Frame(self.bottomLeft)
        self.bottomLeftBottom = tkinter.Frame(self.bottomLeft)

        self.bottomMiddleTop = tkinter.Frame(self.bottomMiddle)
        self.bottomMiddleMid = tkinter.Frame(self.bottomMiddle)
        self.bottomMiddleBottom = tkinter.Frame(self.bottomMiddle)

        self.bottomRightTop = tkinter.Frame(self.bottomRight)
        self.bottomRightMid = tkinter.Frame(self.bottomRight)
        self.bottomRightBottom = tkinter.Frame(self.bottomRight)

        #fill rows
        self.a1_Entry = tkinter.Entry(self.topLeftTop, width=3, textvariable=self.a1, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a2_Entry = tkinter.Entry(self.topLeftTop, width=3, textvariable=self.a2, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a3_Entry = tkinter.Entry(self.topLeftTop, width=3, textvariable=self.a3, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.b1_Entry = tkinter.Entry(self.topLeftMid, width=3, textvariable=self.b1, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b2_Entry = tkinter.Entry(self.topLeftMid, width=3, textvariable=self.b2, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b3_Entry = tkinter.Entry(self.topLeftMid, width=3, textvariable=self.b3, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.c1_Entry = tkinter.Entry(self.topLeftBottom, width=3, textvariable=self.c1, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c2_Entry = tkinter.Entry(self.topLeftBottom, width=3, textvariable=self.c2, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c3_Entry = tkinter.Entry(self.topLeftBottom, width=3, textvariable=self.c3, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.a4_Entry = tkinter.Entry(self.topMiddleTop, width=3, textvariable=self.a4, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a5_Entry = tkinter.Entry(self.topMiddleTop, width=3, textvariable=self.a5, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a6_Entry = tkinter.Entry(self.topMiddleTop, width=3, textvariable=self.a6, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.b4_Entry = tkinter.Entry(self.topMiddleMid, width=3, textvariable=self.b4, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b5_Entry = tkinter.Entry(self.topMiddleMid, width=3, textvariable=self.b5, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b6_Entry = tkinter.Entry(self.topMiddleMid, width=3, textvariable=self.b6, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.c4_Entry = tkinter.Entry(self.topMiddleBottom, width=3, textvariable=self.c4, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c5_Entry = tkinter.Entry(self.topMiddleBottom, width=3, textvariable=self.c5, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c6_Entry = tkinter.Entry(self.topMiddleBottom, width=3, textvariable=self.c6, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.a7_Entry = tkinter.Entry(self.topRightTop, width=3, textvariable=self.a7, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a8_Entry = tkinter.Entry(self.topRightTop, width=3, textvariable=self.a8, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a9_Entry = tkinter.Entry(self.topRightTop, width=3, textvariable=self.a9, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.b7_Entry = tkinter.Entry(self.topRightMid, width=3, textvariable=self.b7, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b8_Entry = tkinter.Entry(self.topRightMid, width=3, textvariable=self.b8, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b9_Entry = tkinter.Entry(self.topRightMid, width=3, textvariable=self.b9, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.c7_Entry = tkinter.Entry(self.topRightBottom, width=3, textvariable=self.c7, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c8_Entry = tkinter.Entry(self.topRightBottom, width=3, textvariable=self.c8, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c9_Entry = tkinter.Entry(self.topRightBottom, width=3, textvariable=self.c9, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
             
        self.d1_Entry = tkinter.Entry(self.middleLeftTop, width=3, textvariable=self.d1, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d2_Entry = tkinter.Entry(self.middleLeftTop, width=3, textvariable=self.d2, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d3_Entry = tkinter.Entry(self.middleLeftTop, width=3, textvariable=self.d3, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.e1_Entry = tkinter.Entry(self.middleLeftMid, width=3, textvariable=self.e1, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e2_Entry = tkinter.Entry(self.middleLeftMid, width=3, textvariable=self.e2, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e3_Entry = tkinter.Entry(self.middleLeftMid, width=3, textvariable=self.e3, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.f1_Entry = tkinter.Entry(self.middleLeftBottom, width=3, textvariable=self.f1, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f2_Entry = tkinter.Entry(self.middleLeftBottom, width=3, textvariable=self.f2, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f3_Entry = tkinter.Entry(self.middleLeftBottom, width=3, textvariable=self.f3, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.d4_Entry = tkinter.Entry(self.middleMiddleTop, width=3, textvariable=self.d4, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d5_Entry = tkinter.Entry(self.middleMiddleTop, width=3, textvariable=self.d5, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d6_Entry = tkinter.Entry(self.middleMiddleTop, width=3, textvariable=self.d6, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.e4_Entry = tkinter.Entry(self.middleMiddleMid, width=3, textvariable=self.e4, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e5_Entry = tkinter.Entry(self.middleMiddleMid, width=3, textvariable=self.e5, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e6_Entry = tkinter.Entry(self.middleMiddleMid, width=3, textvariable=self.e6, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.f4_Entry = tkinter.Entry(self.middleMiddleBottom, width=3, textvariable=self.f4, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f5_Entry = tkinter.Entry(self.middleMiddleBottom, width=3, textvariable=self.f5, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f6_Entry = tkinter.Entry(self.middleMiddleBottom, width=3, textvariable=self.f6, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.d7_Entry = tkinter.Entry(self.middleRightTop, width=3, textvariable=self.d7, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d8_Entry = tkinter.Entry(self.middleRightTop, width=3, textvariable=self.d8, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d9_Entry = tkinter.Entry(self.middleRightTop, width=3, textvariable=self.d9, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.e7_Entry = tkinter.Entry(self.middleRightMid, width=3, textvariable=self.e7, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e8_Entry = tkinter.Entry(self.middleRightMid, width=3, textvariable=self.e8, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e9_Entry = tkinter.Entry(self.middleRightMid, width=3, textvariable=self.e9, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.f7_Entry = tkinter.Entry(self.middleRightBottom, width=3, textvariable=self.f7, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f8_Entry = tkinter.Entry(self.middleRightBottom, width=3, textvariable=self.f8, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f9_Entry = tkinter.Entry(self.middleRightBottom, width=3, textvariable=self.f9, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1) 

        self.g1_Entry = tkinter.Entry(self.bottomLeftTop, width=3, textvariable=self.g1, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g2_Entry = tkinter.Entry(self.bottomLeftTop, width=3, textvariable=self.g2, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g3_Entry = tkinter.Entry(self.bottomLeftTop, width=3, textvariable=self.g3, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.h1_Entry = tkinter.Entry(self.bottomLeftMid, width=3, textvariable=self.h1, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h2_Entry = tkinter.Entry(self.bottomLeftMid, width=3, textvariable=self.h2, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h3_Entry = tkinter.Entry(self.bottomLeftMid, width=3, textvariable=self.h3, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.i1_Entry = tkinter.Entry(self.bottomLeftBottom, width=3, textvariable=self.i1, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i2_Entry = tkinter.Entry(self.bottomLeftBottom, width=3, textvariable=self.i2, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i3_Entry = tkinter.Entry(self.bottomLeftBottom, width=3, textvariable=self.i3, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.g4_Entry = tkinter.Entry(self.bottomMiddleTop, width=3, textvariable=self.g4, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g5_Entry = tkinter.Entry(self.bottomMiddleTop, width=3, textvariable=self.g5, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g6_Entry = tkinter.Entry(self.bottomMiddleTop, width=3, textvariable=self.g6, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.h4_Entry = tkinter.Entry(self.bottomMiddleMid, width=3, textvariable=self.h4, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h5_Entry = tkinter.Entry(self.bottomMiddleMid, width=3, textvariable=self.h5, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h6_Entry = tkinter.Entry(self.bottomMiddleMid, width=3, textvariable=self.h6, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.i4_Entry = tkinter.Entry(self.bottomMiddleBottom, width=3, textvariable=self.i4, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i5_Entry = tkinter.Entry(self.bottomMiddleBottom, width=3, textvariable=self.i5, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i6_Entry = tkinter.Entry(self.bottomMiddleBottom, width=3, textvariable=self.i6, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.g4_Entry = tkinter.Entry(self.bottomRightTop, width=3, textvariable=self.g7, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g5_Entry = tkinter.Entry(self.bottomRightTop, width=3, textvariable=self.g8, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g6_Entry = tkinter.Entry(self.bottomRightTop, width=3, textvariable=self.g9, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.h4_Entry = tkinter.Entry(self.bottomRightMid, width=3, textvariable=self.h7, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h5_Entry = tkinter.Entry(self.bottomRightMid, width=3, textvariable=self.h8, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h6_Entry = tkinter.Entry(self.bottomRightMid, width=3, textvariable=self.h9, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.i4_Entry = tkinter.Entry(self.bottomRightBottom, width=3, textvariable=self.i7, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i5_Entry = tkinter.Entry(self.bottomRightBottom, width=3, textvariable=self.i8, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i6_Entry = tkinter.Entry(self.bottomRightBottom, width=3, textvariable=self.i9, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        #pack rows
        self.topLeftTop.pack(side='top')
        self.topLeftMid.pack(side='top')
        self.topLeftBottom.pack(side='top')
        
        self.topMiddleTop.pack(side='top')
        self.topMiddleMid.pack(side='top')
        self.topMiddleBottom.pack(side='top')

        self.topRightTop.pack(side='top')
        self.topRightMid.pack(side='top')
        self.topRightBottom.pack(side='top')

        self.middleLeftTop.pack(side='top')
        self.middleLeftMid.pack(side='top')
        self.middleLeftBottom.pack(side='top')

        self.middleMiddleTop.pack(side='top')
        self.middleMiddleMid.pack(side='top')
        self.middleMiddleBottom.pack(side='top')

        self.middleRightTop.pack(side='top')
        self.middleRightMid.pack(side='top')
        self.middleRightBottom.pack(side='top')

        self.bottomLeftTop.pack(side='top')
        self.bottomLeftMid.pack(side='top')
        self.bottomLeftBottom.pack(side='top')

        self.bottomMiddleTop.pack(side='top')
        self.bottomMiddleMid.pack(side='top')
        self.bottomMiddleBottom.pack(side='top')

        self.bottomRightTop.pack(side='top')
        self.bottomRightMid.pack(side='top')
        self.bottomRightBottom.pack(side='top')

        #pack squares and heading        
        self.topLeft.pack(side='left', padx=2)
        self.topMiddle.pack(side='left', padx=2)
        self.topRight.pack(side='left', padx=2)
        self.middleLeft.pack(side='left', padx=2)
        self.middleMiddle.pack(side='left', padx=2)
        self.middleRight.pack(side='left', padx=2)
        self.bottomLeft.pack(side='left', padx=2)
        self.bottomMiddle.pack(side='left', padx=2)
        self.bottomRight.pack(side='left', padx=2)

        self.headingFrame.pack(side='top', padx=1, pady=1)
        self.top.pack(side='top', padx=1, pady=1)
        self.middle.pack(side='top', padx=1, pady=1)
        self.bottom.pack(side='top', padx=1, pady=1)
        self.bottom2.pack(side='top', pady=10)
        self.difficultyFrame.pack(side='top', pady=10)

        tkinter.mainloop()

    def solve_sudoku(self):
        # create a list of values to create the SudokuPuzzle object with
        self.values_list = [self.a1.get(), self.a2.get(), self.a3.get(), self.a4.get(), self.a5.get(), self.a6.get(), self.a7.get(), self.a8.get(),
                            self.a9.get(), self.b1.get(), self.b2.get(), self.b3.get(), self.b4.get(), self.b5.get(), self.b6.get(), self.b7.get(),
                            self.b8.get(), self.b9.get(), self.c1.get(), self.c2.get(), self.c3.get(), self.c4.get(), self.c5.get(), self.c6.get(),
                            self.c7.get(), self.c8.get(), self.c9.get(), self.d1.get(), self.d2.get(), self.d3.get(), self.d4.get(), self.d5.get(),
                            self.d6.get(), self.d7.get(), self.d8.get(), self.d9.get(), self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(),
                            self.e5.get(), self.e6.get(), self.e7.get(), self.e8.get(), self.e9.get(), self.f1.get(), self.f2.get(), self.f3.get(),
                            self.f4.get(), self.f5.get(), self.f6.get(), self.f7.get(), self.f8.get(), self.f9.get(), self.g1.get(), self.g2.get(),
                            self.g3.get(), self.g4.get(), self.g5.get(), self.g6.get(), self.g7.get(), self.g8.get(), self.g9.get(), self.h1.get(),
                            self.h2.get(), self.h3.get(), self.h4.get(), self.h5.get(), self.h6.get(), self.h7.get(), self.h8.get(), self.h9.get(),
                            self.i1.get(), self.i2.get(), self.i3.get(), self.i4.get(), self.i5.get(), self.i6.get(), self.i7.get(), self.i8.get(),
                            self.i9.get()]

        # create the SudokuPuzzle. Shows error dialoge if bad values are submitted.
        try:
            self.sudoku = sudoku.SudokuPuzzle(self.values_list)
            validInput = True
        except SudokuError:
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
        self.a1.set(self.sudoku.a1.get())
        self.a2.set(self.sudoku.a2.get())
        self.a3.set(self.sudoku.a3.get())
        self.a4.set(self.sudoku.a4.get())
        self.a5.set(self.sudoku.a5.get())
        self.a6.set(self.sudoku.a6.get())
        self.a7.set(self.sudoku.a7.get())
        self.a8.set(self.sudoku.a8.get())
        self.a9.set(self.sudoku.a9.get())
        self.b1.set(self.sudoku.b1.get())
        self.b2.set(self.sudoku.b2.get())
        self.b3.set(self.sudoku.b3.get())
        self.b4.set(self.sudoku.b4.get())
        self.b5.set(self.sudoku.b5.get())
        self.b6.set(self.sudoku.b6.get())
        self.b7.set(self.sudoku.b7.get())
        self.b8.set(self.sudoku.b8.get())
        self.b9.set(self.sudoku.b9.get())
        self.c1.set(self.sudoku.c1.get())
        self.c2.set(self.sudoku.c2.get())
        self.c3.set(self.sudoku.c3.get())
        self.c4.set(self.sudoku.c4.get())
        self.c5.set(self.sudoku.c5.get())
        self.c6.set(self.sudoku.c6.get())
        self.c7.set(self.sudoku.c7.get())
        self.c8.set(self.sudoku.c8.get())
        self.c9.set(self.sudoku.c9.get())
        self.d1.set(self.sudoku.d1.get())
        self.d2.set(self.sudoku.d2.get())
        self.d3.set(self.sudoku.d3.get())
        self.d4.set(self.sudoku.d4.get())
        self.d5.set(self.sudoku.d5.get())
        self.d6.set(self.sudoku.d6.get())
        self.d7.set(self.sudoku.d7.get())
        self.d8.set(self.sudoku.d8.get())
        self.d9.set(self.sudoku.d9.get())
        self.e1.set(self.sudoku.e1.get())
        self.e2.set(self.sudoku.e2.get())
        self.e3.set(self.sudoku.e3.get())
        self.e4.set(self.sudoku.e4.get())
        self.e5.set(self.sudoku.e5.get())
        self.e6.set(self.sudoku.e6.get())
        self.e7.set(self.sudoku.e7.get())
        self.e8.set(self.sudoku.e8.get())
        self.e9.set(self.sudoku.e9.get())
        self.f1.set(self.sudoku.f1.get())
        self.f2.set(self.sudoku.f2.get())
        self.f3.set(self.sudoku.f3.get())
        self.f4.set(self.sudoku.f4.get())
        self.f5.set(self.sudoku.f5.get())
        self.f6.set(self.sudoku.f6.get())
        self.f7.set(self.sudoku.f7.get())
        self.f8.set(self.sudoku.f8.get())
        self.f9.set(self.sudoku.f9.get())
        self.g1.set(self.sudoku.g1.get())
        self.g2.set(self.sudoku.g2.get())
        self.g3.set(self.sudoku.g3.get())
        self.g4.set(self.sudoku.g4.get())
        self.g5.set(self.sudoku.g5.get())
        self.g6.set(self.sudoku.g6.get())
        self.g7.set(self.sudoku.g7.get())
        self.g8.set(self.sudoku.g8.get())
        self.g9.set(self.sudoku.g9.get())
        self.h1.set(self.sudoku.h1.get())
        self.h2.set(self.sudoku.h2.get())
        self.h3.set(self.sudoku.h3.get())
        self.h4.set(self.sudoku.h4.get())
        self.h5.set(self.sudoku.h5.get())
        self.h6.set(self.sudoku.h6.get())
        self.h7.set(self.sudoku.h7.get())
        self.h8.set(self.sudoku.h8.get())
        self.h9.set(self.sudoku.h9.get())
        self.i1.set(self.sudoku.i1.get())
        self.i2.set(self.sudoku.i2.get())
        self.i3.set(self.sudoku.i3.get())
        self.i4.set(self.sudoku.i4.get())
        self.i5.set(self.sudoku.i5.get())
        self.i6.set(self.sudoku.i6.get())
        self.i7.set(self.sudoku.i7.get())
        self.i8.set(self.sudoku.i8.get())
        self.i9.set(self.sudoku.i9.get())

    def clear_boxes(self):
        '''Clear all the boxes in the GUI.'''
        for box in self.sudoku.rows:
            for value in box:
                value.set('')

        self.update_boxes()
   
# run everything:
gui = ProgramGUI()
