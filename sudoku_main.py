# sudoku builder/solver gui

import tkinter
import tkinter.messagebox
import sudoku

class ProgramGUI:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('Sudoku Builder')

        #initialise attributes
        fontDetails = 'Calibri 14'

        self.difficulty = tkinter.StringVar()
        self.difficulty.set('1')
        
        self.a1_ = tkinter.StringVar()
        self.a2_ = tkinter.StringVar()
        self.a3_ = tkinter.StringVar()
        self.a4_ = tkinter.StringVar()
        self.a5_ = tkinter.StringVar()
        self.a6_ = tkinter.StringVar()
        self.a7_ = tkinter.StringVar()
        self.a8_ = tkinter.StringVar()
        self.a9_ = tkinter.StringVar()
        self.b1_ = tkinter.StringVar()
        self.b2_ = tkinter.StringVar()
        self.b3_ = tkinter.StringVar()
        self.b4_ = tkinter.StringVar()
        self.b5_ = tkinter.StringVar()
        self.b6_ = tkinter.StringVar()
        self.b7_ = tkinter.StringVar()
        self.b8_ = tkinter.StringVar()
        self.b9_ = tkinter.StringVar()
        self.c1_ = tkinter.StringVar()
        self.c2_ = tkinter.StringVar()
        self.c3_ = tkinter.StringVar()
        self.c4_ = tkinter.StringVar()
        self.c5_ = tkinter.StringVar()
        self.c6_ = tkinter.StringVar()
        self.c7_ = tkinter.StringVar()
        self.c8_ = tkinter.StringVar()
        self.c9_ = tkinter.StringVar()
        self.d1_ = tkinter.StringVar()
        self.d2_ = tkinter.StringVar()
        self.d3_ = tkinter.StringVar()
        self.d4_ = tkinter.StringVar()
        self.d5_ = tkinter.StringVar()
        self.d6_ = tkinter.StringVar()
        self.d7_ = tkinter.StringVar()
        self.d8_ = tkinter.StringVar()
        self.d9_ = tkinter.StringVar()
        self.e1_ = tkinter.StringVar()
        self.e2_ = tkinter.StringVar()
        self.e3_ = tkinter.StringVar()
        self.e4_ = tkinter.StringVar()
        self.e5_ = tkinter.StringVar()
        self.e6_ = tkinter.StringVar()
        self.e7_ = tkinter.StringVar()
        self.e8_ = tkinter.StringVar()
        self.e9_ = tkinter.StringVar()
        self.f1_ = tkinter.StringVar()
        self.f2_ = tkinter.StringVar()
        self.f3_ = tkinter.StringVar()
        self.f4_ = tkinter.StringVar()
        self.f5_ = tkinter.StringVar()
        self.f6_ = tkinter.StringVar()
        self.f7_ = tkinter.StringVar()
        self.f8_ = tkinter.StringVar()
        self.f9_ = tkinter.StringVar()
        self.g1_ = tkinter.StringVar()
        self.g2_ = tkinter.StringVar()
        self.g3_ = tkinter.StringVar()
        self.g4_ = tkinter.StringVar()
        self.g5_ = tkinter.StringVar()
        self.g6_ = tkinter.StringVar()
        self.g7_ = tkinter.StringVar()
        self.g8_ = tkinter.StringVar()
        self.g9_ = tkinter.StringVar()
        self.h1_ = tkinter.StringVar()
        self.h2_ = tkinter.StringVar()
        self.h3_ = tkinter.StringVar()
        self.h4_ = tkinter.StringVar()
        self.h5_ = tkinter.StringVar()
        self.h6_ = tkinter.StringVar()
        self.h7_ = tkinter.StringVar()
        self.h8_ = tkinter.StringVar()
        self.h9_ = tkinter.StringVar()
        self.i1_ = tkinter.StringVar()
        self.i2_ = tkinter.StringVar()
        self.i3_ = tkinter.StringVar()
        self.i4_ = tkinter.StringVar()
        self.i5_ = tkinter.StringVar()
        self.i6_ = tkinter.StringVar()
        self.i7_ = tkinter.StringVar()
        self.i8_ = tkinter.StringVar()
        self.i9_ = tkinter.StringVar()

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
        self.a1_Entry = tkinter.Entry(self.topLeftTop, width=3, textvariable=self.a1_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a2_Entry = tkinter.Entry(self.topLeftTop, width=3, textvariable=self.a2_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a3_Entry = tkinter.Entry(self.topLeftTop, width=3, textvariable=self.a3_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.b1_Entry = tkinter.Entry(self.topLeftMid, width=3, textvariable=self.b1_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b2_Entry = tkinter.Entry(self.topLeftMid, width=3, textvariable=self.b2_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b3_Entry = tkinter.Entry(self.topLeftMid, width=3, textvariable=self.b3_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.c1_Entry = tkinter.Entry(self.topLeftBottom, width=3, textvariable=self.c1_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c2_Entry = tkinter.Entry(self.topLeftBottom, width=3, textvariable=self.c2_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c3_Entry = tkinter.Entry(self.topLeftBottom, width=3, textvariable=self.c3_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.a4_Entry = tkinter.Entry(self.topMiddleTop, width=3, textvariable=self.a4_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a5_Entry = tkinter.Entry(self.topMiddleTop, width=3, textvariable=self.a5_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a6_Entry = tkinter.Entry(self.topMiddleTop, width=3, textvariable=self.a6_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.b4_Entry = tkinter.Entry(self.topMiddleMid, width=3, textvariable=self.b4_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b5_Entry = tkinter.Entry(self.topMiddleMid, width=3, textvariable=self.b5_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b6_Entry = tkinter.Entry(self.topMiddleMid, width=3, textvariable=self.b6_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.c4_Entry = tkinter.Entry(self.topMiddleBottom, width=3, textvariable=self.c4_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c5_Entry = tkinter.Entry(self.topMiddleBottom, width=3, textvariable=self.c5_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c6_Entry = tkinter.Entry(self.topMiddleBottom, width=3, textvariable=self.c6_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.a7_Entry = tkinter.Entry(self.topRightTop, width=3, textvariable=self.a7_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a8_Entry = tkinter.Entry(self.topRightTop, width=3, textvariable=self.a8_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.a9_Entry = tkinter.Entry(self.topRightTop, width=3, textvariable=self.a9_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.b7_Entry = tkinter.Entry(self.topRightMid, width=3, textvariable=self.b7_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b8_Entry = tkinter.Entry(self.topRightMid, width=3, textvariable=self.b8_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.b9_Entry = tkinter.Entry(self.topRightMid, width=3, textvariable=self.b9_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.c7_Entry = tkinter.Entry(self.topRightBottom, width=3, textvariable=self.c7_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c8_Entry = tkinter.Entry(self.topRightBottom, width=3, textvariable=self.c8_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.c9_Entry = tkinter.Entry(self.topRightBottom, width=3, textvariable=self.c9_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
             
        self.d1_Entry = tkinter.Entry(self.middleLeftTop, width=3, textvariable=self.d1_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d2_Entry = tkinter.Entry(self.middleLeftTop, width=3, textvariable=self.d2_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d3_Entry = tkinter.Entry(self.middleLeftTop, width=3, textvariable=self.d3_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.e1_Entry = tkinter.Entry(self.middleLeftMid, width=3, textvariable=self.e1_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e2_Entry = tkinter.Entry(self.middleLeftMid, width=3, textvariable=self.e2_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e3_Entry = tkinter.Entry(self.middleLeftMid, width=3, textvariable=self.e3_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.f1_Entry = tkinter.Entry(self.middleLeftBottom, width=3, textvariable=self.f1_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f2_Entry = tkinter.Entry(self.middleLeftBottom, width=3, textvariable=self.f2_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f3_Entry = tkinter.Entry(self.middleLeftBottom, width=3, textvariable=self.f3_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.d4_Entry = tkinter.Entry(self.middleMiddleTop, width=3, textvariable=self.d4_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d5_Entry = tkinter.Entry(self.middleMiddleTop, width=3, textvariable=self.d5_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d6_Entry = tkinter.Entry(self.middleMiddleTop, width=3, textvariable=self.d6_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.e4_Entry = tkinter.Entry(self.middleMiddleMid, width=3, textvariable=self.e4_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e5_Entry = tkinter.Entry(self.middleMiddleMid, width=3, textvariable=self.e5_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e6_Entry = tkinter.Entry(self.middleMiddleMid, width=3, textvariable=self.e6_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.f4_Entry = tkinter.Entry(self.middleMiddleBottom, width=3, textvariable=self.f4_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f5_Entry = tkinter.Entry(self.middleMiddleBottom, width=3, textvariable=self.f5_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f6_Entry = tkinter.Entry(self.middleMiddleBottom, width=3, textvariable=self.f6_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.d7_Entry = tkinter.Entry(self.middleRightTop, width=3, textvariable=self.d7_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d8_Entry = tkinter.Entry(self.middleRightTop, width=3, textvariable=self.d8_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.d9_Entry = tkinter.Entry(self.middleRightTop, width=3, textvariable=self.d9_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.e7_Entry = tkinter.Entry(self.middleRightMid, width=3, textvariable=self.e7_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e8_Entry = tkinter.Entry(self.middleRightMid, width=3, textvariable=self.e8_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.e9_Entry = tkinter.Entry(self.middleRightMid, width=3, textvariable=self.e9_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.f7_Entry = tkinter.Entry(self.middleRightBottom, width=3, textvariable=self.f7_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f8_Entry = tkinter.Entry(self.middleRightBottom, width=3, textvariable=self.f8_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.f9_Entry = tkinter.Entry(self.middleRightBottom, width=3, textvariable=self.f9_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1) 

        self.g1_Entry = tkinter.Entry(self.bottomLeftTop, width=3, textvariable=self.g1_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g2_Entry = tkinter.Entry(self.bottomLeftTop, width=3, textvariable=self.g2_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g3_Entry = tkinter.Entry(self.bottomLeftTop, width=3, textvariable=self.g3_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.h1_Entry = tkinter.Entry(self.bottomLeftMid, width=3, textvariable=self.h1_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h2_Entry = tkinter.Entry(self.bottomLeftMid, width=3, textvariable=self.h2_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h3_Entry = tkinter.Entry(self.bottomLeftMid, width=3, textvariable=self.h3_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.i1_Entry = tkinter.Entry(self.bottomLeftBottom, width=3, textvariable=self.i1_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i2_Entry = tkinter.Entry(self.bottomLeftBottom, width=3, textvariable=self.i2_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i3_Entry = tkinter.Entry(self.bottomLeftBottom, width=3, textvariable=self.i3_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.g4_Entry = tkinter.Entry(self.bottomMiddleTop, width=3, textvariable=self.g4_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g5_Entry = tkinter.Entry(self.bottomMiddleTop, width=3, textvariable=self.g5_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g6_Entry = tkinter.Entry(self.bottomMiddleTop, width=3, textvariable=self.g6_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.h4_Entry = tkinter.Entry(self.bottomMiddleMid, width=3, textvariable=self.h4_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h5_Entry = tkinter.Entry(self.bottomMiddleMid, width=3, textvariable=self.h5_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h6_Entry = tkinter.Entry(self.bottomMiddleMid, width=3, textvariable=self.h6_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.i4_Entry = tkinter.Entry(self.bottomMiddleBottom, width=3, textvariable=self.i4_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i5_Entry = tkinter.Entry(self.bottomMiddleBottom, width=3, textvariable=self.i5_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i6_Entry = tkinter.Entry(self.bottomMiddleBottom, width=3, textvariable=self.i6_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.g4_Entry = tkinter.Entry(self.bottomRightTop, width=3, textvariable=self.g7_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g5_Entry = tkinter.Entry(self.bottomRightTop, width=3, textvariable=self.g8_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.g6_Entry = tkinter.Entry(self.bottomRightTop, width=3, textvariable=self.g9_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.h4_Entry = tkinter.Entry(self.bottomRightMid, width=3, textvariable=self.h7_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h5_Entry = tkinter.Entry(self.bottomRightMid, width=3, textvariable=self.h8_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.h6_Entry = tkinter.Entry(self.bottomRightMid, width=3, textvariable=self.h9_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

        self.i4_Entry = tkinter.Entry(self.bottomRightBottom, width=3, textvariable=self.i7_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i5_Entry = tkinter.Entry(self.bottomRightBottom, width=3, textvariable=self.i8_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)
        self.i6_Entry = tkinter.Entry(self.bottomRightBottom, width=3, textvariable=self.i9_, font=fontDetails, justify='center').pack(side='left', padx=1, pady=1)

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
        self.values_list = [self.a1_.get(), self.a2_.get(), self.a3_.get(), self.a4_.get(), self.a5_.get(), self.a6_.get(), self.a7_.get(), self.a8_.get(),
                            self.a9_.get(), self.b1_.get(), self.b2_.get(), self.b3_.get(), self.b4_.get(), self.b5_.get(), self.b6_.get(), self.b7_.get(),
                            self.b8_.get(), self.b9_.get(), self.c1_.get(), self.c2_.get(), self.c3_.get(), self.c4_.get(), self.c5_.get(), self.c6_.get(),
                            self.c7_.get(), self.c8_.get(), self.c9_.get(), self.d1_.get(), self.d2_.get(), self.d3_.get(), self.d4_.get(), self.d5_.get(),
                            self.d6_.get(), self.d7_.get(), self.d8_.get(), self.d9_.get(), self.e1_.get(), self.e2_.get(), self.e3_.get(), self.e4_.get(),
                            self.e5_.get(), self.e6_.get(), self.e7_.get(), self.e8_.get(), self.e9_.get(), self.f1_.get(), self.f2_.get(), self.f3_.get(),
                            self.f4_.get(), self.f5_.get(), self.f6_.get(), self.f7_.get(), self.f8_.get(), self.f9_.get(), self.g1_.get(), self.g2_.get(),
                            self.g3_.get(), self.g4_.get(), self.g5_.get(), self.g6_.get(), self.g7_.get(), self.g8_.get(), self.g9_.get(), self.h1_.get(),
                            self.h2_.get(), self.h3_.get(), self.h4_.get(), self.h5_.get(), self.h6_.get(), self.h7_.get(), self.h8_.get(), self.h9_.get(),
                            self.i1_.get(), self.i2_.get(), self.i3_.get(), self.i4_.get(), self.i5_.get(), self.i6_.get(), self.i7_.get(), self.i8_.get(),
                            self.i9_.get()]

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
        self.a1_.set(self.sudoku.a1.get())
        self.a2_.set(self.sudoku.a2.get())
        self.a3_.set(self.sudoku.a3.get())
        self.a4_.set(self.sudoku.a4.get())
        self.a5_.set(self.sudoku.a5.get())
        self.a6_.set(self.sudoku.a6.get())
        self.a7_.set(self.sudoku.a7.get())
        self.a8_.set(self.sudoku.a8.get())
        self.a9_.set(self.sudoku.a9.get())
        self.b1_.set(self.sudoku.b1.get())
        self.b2_.set(self.sudoku.b2.get())
        self.b3_.set(self.sudoku.b3.get())
        self.b4_.set(self.sudoku.b4.get())
        self.b5_.set(self.sudoku.b5.get())
        self.b6_.set(self.sudoku.b6.get())
        self.b7_.set(self.sudoku.b7.get())
        self.b8_.set(self.sudoku.b8.get())
        self.b9_.set(self.sudoku.b9.get())
        self.c1_.set(self.sudoku.c1.get())
        self.c2_.set(self.sudoku.c2.get())
        self.c3_.set(self.sudoku.c3.get())
        self.c4_.set(self.sudoku.c4.get())
        self.c5_.set(self.sudoku.c5.get())
        self.c6_.set(self.sudoku.c6.get())
        self.c7_.set(self.sudoku.c7.get())
        self.c8_.set(self.sudoku.c8.get())
        self.c9_.set(self.sudoku.c9.get())
        self.d1_.set(self.sudoku.d1.get())
        self.d2_.set(self.sudoku.d2.get())
        self.d3_.set(self.sudoku.d3.get())
        self.d4_.set(self.sudoku.d4.get())
        self.d5_.set(self.sudoku.d5.get())
        self.d6_.set(self.sudoku.d6.get())
        self.d7_.set(self.sudoku.d7.get())
        self.d8_.set(self.sudoku.d8.get())
        self.d9_.set(self.sudoku.d9.get())
        self.e1_.set(self.sudoku.e1.get())
        self.e2_.set(self.sudoku.e2.get())
        self.e3_.set(self.sudoku.e3.get())
        self.e4_.set(self.sudoku.e4.get())
        self.e5_.set(self.sudoku.e5.get())
        self.e6_.set(self.sudoku.e6.get())
        self.e7_.set(self.sudoku.e7.get())
        self.e8_.set(self.sudoku.e8.get())
        self.e9_.set(self.sudoku.e9.get())
        self.f1_.set(self.sudoku.f1.get())
        self.f2_.set(self.sudoku.f2.get())
        self.f3_.set(self.sudoku.f3.get())
        self.f4_.set(self.sudoku.f4.get())
        self.f5_.set(self.sudoku.f5.get())
        self.f6_.set(self.sudoku.f6.get())
        self.f7_.set(self.sudoku.f7.get())
        self.f8_.set(self.sudoku.f8.get())
        self.f9_.set(self.sudoku.f9.get())
        self.g1_.set(self.sudoku.g1.get())
        self.g2_.set(self.sudoku.g2.get())
        self.g3_.set(self.sudoku.g3.get())
        self.g4_.set(self.sudoku.g4.get())
        self.g5_.set(self.sudoku.g5.get())
        self.g6_.set(self.sudoku.g6.get())
        self.g7_.set(self.sudoku.g7.get())
        self.g8_.set(self.sudoku.g8.get())
        self.g9_.set(self.sudoku.g9.get())
        self.h1_.set(self.sudoku.h1.get())
        self.h2_.set(self.sudoku.h2.get())
        self.h3_.set(self.sudoku.h3.get())
        self.h4_.set(self.sudoku.h4.get())
        self.h5_.set(self.sudoku.h5.get())
        self.h6_.set(self.sudoku.h6.get())
        self.h7_.set(self.sudoku.h7.get())
        self.h8_.set(self.sudoku.h8.get())
        self.h9_.set(self.sudoku.h9.get())
        self.i1_.set(self.sudoku.i1.get())
        self.i2_.set(self.sudoku.i2.get())
        self.i3_.set(self.sudoku.i3.get())
        self.i4_.set(self.sudoku.i4.get())
        self.i5_.set(self.sudoku.i5.get())
        self.i6_.set(self.sudoku.i6.get())
        self.i7_.set(self.sudoku.i7.get())
        self.i8_.set(self.sudoku.i8.get())
        self.i9_.set(self.sudoku.i9.get())

    def clear_boxes(self):
        '''Clear all the boxes in the GUI.'''
        for box in self.sudoku.rows:
            for value in box:
                value.set('')

        self.update_boxes()
   
# run everything:
gui = ProgramGUI()
