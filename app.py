from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow) -> None:

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ### Back End

        """
            I am using a matrix to store the position of the pieces on the board, every integer 
            corresponds exactly to either an empty cell or a piece of the board.

            0 => Empty Cell
            1 => White Pawn
            2 => Black Pawn
            3 => White Queen
            4 => Black Queen

            I am using a state variable to determine whether the user has already selected the piece
            and he is choosing the cell where he wants to move it or he still hasn't selected it

            0 => Piece to move hasn't been chosen
            1 => Piece to move has been chosen

            I am using a turn variable to determine which player has to play (0 White - 1 Black)

        """
        self.board = [
                [2, 0, 2, 0, 2, 0, 2, 0],
                [0, 2, 0, 2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2, 0, 2, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
        ]
        self.state = 0
        self.turn = 0
        self.winner = None
        self.selected_piece_row = None
        self.selected_piece_col = None

        ### UI

        self.boardUI = []       # Container of the Buttons
        self.cell_side = 50     

        ## Creates Start Menu
        self.start_menu_title = QtWidgets.QLabel('Arial font', self.centralwidget)
        self.start_menu_title.setGeometry(QtCore.QRect(150, 50, 120, 100))
        self.start_menu_title.setFont(QtGui.QFont('Arial', 20))
        self.start_menu_title.setText("Checkers")

        self.start_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_menu_button.setGeometry(QtCore.QRect(100, 150, 200, 60))
        self.start_menu_button.setFont(QtGui.QFont('Arial', 20))
        self.start_menu_button.setText("Start Game")
        self.start_menu_button.clicked.connect(self.startGame)

        ## Creates Restart Menu
        self.restart_menu_title = QtWidgets.QLabel('Arial font', self.centralwidget)
        self.restart_menu_title.setGeometry(QtCore.QRect(20, 50, 350, 100))
        self.restart_menu_title.setFont(QtGui.QFont('Arial', 20))
        self.restart_menu_title.setAlignment(QtCore.Qt.AlignCenter)
        self.restart_menu_title.hide()

        self.restart_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.restart_menu_button.setGeometry(QtCore.QRect(100, 150, 200, 60))
        self.restart_menu_button.setFont(QtGui.QFont('Arial', 20))
        self.restart_menu_button.setText("Start Game")
        self.restart_menu_button.clicked.connect(self.startGame)
        self.restart_menu_button.hide()

        ## Creates Buttons 
        for row in range(8):
            board_row = []  
            for col in range(8):

                # Computes Position of the Button
                x = col * (self.cell_side - 1)              # -1 is needed to make the Buttons    
                y = row * (self.cell_side - 1)              # look nicer when together
                side = self.cell_side
                board = self.board

                # Creates the Button and Adds it to the Row
                button = QtWidgets.QPushButton(self.centralwidget)
                button.setGeometry(QtCore.QRect(x, y, side, side))
                board_row.append(button)

            # Adds the Row to the board 
            self.boardUI.append(board_row)

        # self.displayBoard()
        self.displayStartMenu()

        ## Links the specific Event to every single Button
        self.boardUI[0][0].clicked.connect(lambda: self.cellClicked(0,0))
        self.boardUI[0][2].clicked.connect(lambda: self.cellClicked(0,2))
        self.boardUI[0][4].clicked.connect(lambda: self.cellClicked(0,4))
        self.boardUI[0][6].clicked.connect(lambda: self.cellClicked(0,6))
        self.boardUI[1][1].clicked.connect(lambda: self.cellClicked(1,1))
        self.boardUI[1][3].clicked.connect(lambda: self.cellClicked(1,3))
        self.boardUI[1][5].clicked.connect(lambda: self.cellClicked(1,5))
        self.boardUI[1][7].clicked.connect(lambda: self.cellClicked(1,7))
        self.boardUI[2][0].clicked.connect(lambda: self.cellClicked(2,0))
        self.boardUI[2][2].clicked.connect(lambda: self.cellClicked(2,2))
        self.boardUI[2][4].clicked.connect(lambda: self.cellClicked(2,4))
        self.boardUI[2][6].clicked.connect(lambda: self.cellClicked(2,6))
        self.boardUI[3][1].clicked.connect(lambda: self.cellClicked(3,1))
        self.boardUI[3][3].clicked.connect(lambda: self.cellClicked(3,3))
        self.boardUI[3][5].clicked.connect(lambda: self.cellClicked(3,5))
        self.boardUI[3][7].clicked.connect(lambda: self.cellClicked(3,7))
        self.boardUI[4][0].clicked.connect(lambda: self.cellClicked(4,0))
        self.boardUI[4][2].clicked.connect(lambda: self.cellClicked(4,2))
        self.boardUI[4][4].clicked.connect(lambda: self.cellClicked(4,4))
        self.boardUI[4][6].clicked.connect(lambda: self.cellClicked(4,6))
        self.boardUI[5][1].clicked.connect(lambda: self.cellClicked(5,1))
        self.boardUI[5][3].clicked.connect(lambda: self.cellClicked(5,3))
        self.boardUI[5][5].clicked.connect(lambda: self.cellClicked(5,5))
        self.boardUI[5][7].clicked.connect(lambda: self.cellClicked(5,7))
        self.boardUI[6][0].clicked.connect(lambda: self.cellClicked(6,0))
        self.boardUI[6][2].clicked.connect(lambda: self.cellClicked(6,2))
        self.boardUI[6][4].clicked.connect(lambda: self.cellClicked(6,4))
        self.boardUI[6][6].clicked.connect(lambda: self.cellClicked(6,6))
        self.boardUI[7][1].clicked.connect(lambda: self.cellClicked(7,1))
        self.boardUI[7][3].clicked.connect(lambda: self.cellClicked(7,3))
        self.boardUI[7][5].clicked.connect(lambda: self.cellClicked(7,5))
        self.boardUI[7][7].clicked.connect(lambda: self.cellClicked(7,7))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Function Called when a Square is Pressed
    def cellClicked(self, row: int, col: int) -> None:

        # Selecting the Piece to Move
        if (self.state == 0):
            piece = self.board[row][col]
            if (self.turn == 0 and piece == 1 or piece == 3):      # White Player
                self.selected_piece_row = row
                self.selected_piece_col = col
                self.state = 1
            elif(self.turn == 1 and piece == 2 or piece == 4):     # Black Player
                self.selected_piece_row = row
                self.selected_piece_col = col
                self.state = 1

        elif (self.state == 1):

            # If the Cell contains a Piece of the Same Color then Switch the Selected Piece
            piece = self.board[row][col]
            if (self.turn == 0 and piece == 1 or piece == 3):      # White Player
                self.selected_piece_row = row
                self.selected_piece_col = col
                self.state = 1
            elif(self.turn == 1 and piece == 2 or piece == 4):     # Black Player
                self.selected_piece_row = row
                self.selected_piece_col = col
                self.state = 1

            # Moves the Pawn if it can be Moved
            elif self.move(row, col):
                self.state = 0
                self.turn = 1 if (self.turn == 0) else 0
                self.checkPromotion()
            self.displayBoard()

            # Checks if Game has Ended
            if self.gameEnded():
                self.displayRestartMenu()

    # Checks if a Piece can eat 
    def checkForcedMove(self) -> None:

        # White Player
        if (self.turn == 0):

            for row, row_of_pieces in enumerate(self.board):
                for col, piece in enumerate(row_of_pieces):
                    
                    # Checks if Pawn can eat
                    if (piece == 1):

                        row_displacement = -2
                        col_displacements = [-2, 2]
                        for col_displacement in col_displacements:

                            final_row = row + row_displacement
                            final_col = col + col_displacement
                            mid_row = row + row_displacement//2
                            mid_col = col + col_displacement//2

                            if ((final_row >= 0 and final_row < 8 and final_col >= 0 and final_col < 8) and
                                (self.board[final_row][final_col] == 0 and self.board[mid_row][mid_col] == 2)):
                                return True

                    # Checks if King can eat
                    if (piece == 3):
                        
                        # King eats diagonally
                        row_displacements = [-2, 2]
                        col_displacements = [-2, 2]
                        for row_displacement in row_displacements:
                            for col_displacement in col_displacements:

                                final_row = row + row_displacement
                                final_col = col + col_displacement
                                mid_row = row + row_displacement//2
                                mid_col = col + col_displacement//2

                                if ((final_row >= 0 and final_row < 8 and final_col > 0 and final_col < 8) and
                                    (self.board[final_row][final_col] == 0 and 
                                    (self.board[mid_row][mid_col] == 2 or self.board[mid_row][mid_col] == 4))):
                                    return True


        # Black Player
        else:

            for row, row_of_pieces in enumerate(self.board):
                for col, piece in enumerate(row_of_pieces):
                    
                    # Checks if Pawn can eat
                    if (piece == 2):

                        row_displacement = 2
                        col_displacements = [-2, 2]
                        for col_displacement in col_displacements:

                            final_row = row + row_displacement
                            final_col = col + col_displacement
                            mid_row = row + row_displacement//2
                            mid_col = col + col_displacement//2

                            if ((final_row >= 0 and final_row < 8 and final_col >= 0 and final_col < 8) and 
                                (self.board[final_row][final_col] == 0 and self.board[mid_row][mid_col] == 1)):
                                return True

                    # Checks if King can eat
                    if (piece == 4):
                        
                        # King eats diagonally
                        row_displacements = [-2, 2]
                        col_displacements = [-2, 2]
                        for row_displacement in row_displacements:
                            for col_displacement in col_displacements:

                                final_row = row + row_displacement
                                final_col = col + col_displacement
                                mid_row = row + row_displacement//2
                                mid_col = col + col_displacement//2

                                if ((final_row >= 0 and final_row < 8 and final_col >= 0 and final_col < 8) and
                                    (self.board[final_row][final_col] == 0 and 
                                    (self.board[mid_row][mid_col] == 1 or self.board[mid_row][mid_col] == 3))):
                                    return True

        return False



    # Moves the Pawn if Possible and returns True if the Piece was Moved
    def move(self, row: int, col: int) -> None:

        # Utility Variables
        row_dist = row - self.selected_piece_row
        col_dist = col - self.selected_piece_col
        cell_value = self.board[row][col]
        piece_value = self.board[self.selected_piece_row][self.selected_piece_col]

        # Cell is not Empty
        if (cell_value != 0):
            return False

        ### White Turn
        if (self.turn == 0):

            ## Moves Forward
            # Pawn
            if (piece_value == 1 and row_dist == -1 and abs(col_dist) == 1): 
                if (self.checkForcedMove()):
                    return False;
                self.board[row][col] = 1
                self.board[self.selected_piece_row][self.selected_piece_col] = 0
                return True

            # King
            if (piece_value == 3 and abs(row_dist) == 1 and abs(col_dist) == 1):
                if (self.checkForcedMove()):
                    return False;
                self.board[row][col] = 3
                self.board[self.selected_piece_row][self.selected_piece_col] = 0
                return True

            ## Eats A Piece
            # Pawn
            if (piece_value == 1 and row_dist == -2 and abs(col_dist) == 2): 
                piece_in_between = self.board[row - row_dist//2][col - col_dist//2]
                if (piece_in_between == 2):
                    self.board[row][col] = 1
                    self.board[self.selected_piece_row][self.selected_piece_col] = 0
                    self.board[row - row_dist//2][col - col_dist//2] = 0
                    return True

            # King
            if (piece_value == 3 and abs(row_dist) == 2 and abs(col_dist) == 2):
                piece_in_between = self.board[row - row_dist//2][col - col_dist//2]
                if (piece_in_between == 2 or piece_in_between == 4):
                    self.board[row][col] = 3
                    self.board[self.selected_piece_row][self.selected_piece_col] = 0
                    self.board[row - row_dist//2][col - col_dist//2] = 0
                    return True

            ## Eats Two Pieces
            # Pawn
            if (piece_value == 1 and row_dist == -4):

                # Diagonal Pattern
                if (abs(col_dist) == 4):
                    piece_in_between1 = self.board[row - row_dist//4][col - col_dist//4]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col - 3*col_dist//4]
                    if (piece_in_between1 == 2 and piece_in_between2 == 2):
                        self.board[row][col] = 1
                        self.board[row - row_dist//4][col - col_dist//4] = 0
                        self.board[row - 3*row_dist//4][col - 3*col_dist//4] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                # Z-like Pattern 
                elif (col_dist == 0):

                    # The Pawn eats to the Left (Looking at the Chess Board) 
                    piece_in_between1 = self.board[row - row_dist//4][col - 1]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col - 1]
                    if (piece_in_between1 == 2 and piece_in_between2 == 2):
                        self.board[row][col] = 1
                        self.board[row - row_dist//4][col - 1] = 0
                        self.board[row - 3*row_dist//4][col - 1] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                    # The Pawn eats to the Right (Looking at the Chess Board) 
                    piece_in_between1 = self.board[row - row_dist//4][col + 1]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col + 1]
                    if (piece_in_between1 == 2 and piece_in_between2 == 2):
                        self.board[row][col] = 1
                        self.board[row - row_dist//4][col + 1] = 0
                        self.board[row - 3*row_dist//4][col + 1] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

            # King
            if (piece_value == 3):

                # Diagonal Pattern
                if (abs(row_dist) == 4 and abs(col_dist) == 4):
                    piece_in_between1 = self.board[row - row_dist//4][col - col_dist//4]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col - 3*col_dist//4]
                    if ((piece_in_between1 == 2 or piece_in_between1 == 4) and 
                            (piece_in_between2 == 2 or piece_in_between2 == 4)):
                        self.board[row][col] = 3
                        self.board[row - row_dist//4][col - col_dist//4] = 0
                        self.board[row - 3*row_dist//4][col - 3*col_dist//4] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                # Z-Like Pattern Vertically
                if (abs(row_dist) == 4 and col_dist == 0):

                    # The King eats to the Left (Looking at the Chess Board) 
                    piece_in_between1 = self.board[row - row_dist//4][col - 1]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col - 1]
                    if ((piece_in_between1 == 2 or piece_in_between1 == 4) and 
                            (piece_in_between2 == 2 or piece_in_between2 == 4)):
                        self.board[row][col] = 3
                        self.board[row - row_dist//4][col - 1] = 0
                        self.board[row - 3*row_dist//4][col - 1] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                    # The King eats to the Right (Looking at the Chess Board) 
                    piece_in_between1 = self.board[row - row_dist//4][col + 1]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col + 1]
                    if ((piece_in_between1 == 2 or piece_in_between1 == 4) and 
                            (piece_in_between2 == 2 or piece_in_between2 == 4)):
                        self.board[row][col] = 3
                        self.board[row - row_dist//4][col + 1] = 0
                        self.board[row - 3*row_dist//4][col + 1] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                # Z-like Pattern Horizontally
                if (abs(col_dist) == 4 and row_dist == 0):

                    # The King eats ahead 
                    piece_in_between1 = self.board[row - 1][col - col_dist//4]
                    piece_in_between2 = self.board[row - 1][col - 3*col_dist//4]
                    if ((piece_in_between1 == 2 or piece_in_between1 == 4) and 
                            (piece_in_between2 == 2 or piece_in_between2 == 4)):
                        self.board[row][col] = 3
                        self.board[row - 1][col - col_dist//4] = 0
                        self.board[row - 1][col - 3*col_dist//4] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                    # The King eats behind
                    piece_in_between1 = self.board[row + 1][col - col_dist//4]
                    piece_in_between2 = self.board[row + 1][col - 3*col_dist//4]
                    if ((piece_in_between1 == 2 or piece_in_between1 == 4) and 
                            (piece_in_between2 == 2 or piece_in_between2 == 4)):
                        self.board[row][col] = 3
                        self.board[row + 1][col - col_dist//4] = 0
                        self.board[row + 1][col - 3*col_dist//4] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True


        ### Black Turn
        if (self.turn == 1): # Black

            ## Moves Forward
            # Pawn
            if (piece_value == 2 and row_dist == 1 and abs(col_dist) == 1): 
                if (self.checkForcedMove()):
                    return False;
                self.board[row][col] = 2
                self.board[self.selected_piece_row][self.selected_piece_col] = 0
                return True

            # King
            if (piece_value == 4 and abs(row_dist) == 1 and abs(col_dist) == 1):
                if (self.checkForcedMove()):
                    return False;
                self.board[row][col] = 4
                self.board[self.selected_piece_row][self.selected_piece_col] = 0
                return True

            ## Eats a Piece
            # Pawn
            if (piece_value == 2 and row_dist == 2 and abs(col_dist) == 2): 
                piece_in_between = self.board[row - row_dist//2][col - col_dist//2]
                if (piece_in_between == 1):
                    self.board[row][col] = 2
                    self.board[self.selected_piece_row][self.selected_piece_col] = 0
                    self.board[row - row_dist//2][col - col_dist//2] = 0
                    return True
            # King
            if (piece_value == 4 and abs(row_dist) == 2 and abs(col_dist) == 2):
                piece_in_between = self.board[row - row_dist//2][col - col_dist//2]
                if (piece_in_between == 1 or piece_in_between == 3):
                    self.board[row][col] = 4
                    self.board[self.selected_piece_row][self.selected_piece_col] = 0
                    self.board[row - row_dist//2][col - col_dist//2] = 0
                    return True

            ## Eats Two Pieces
            # Pawn
            if (piece_value == 2 and row_dist == 4):

                # Diagonal Pattern
                if (abs(col_dist) == 4):
                    piece_in_between1 = self.board[row - row_dist//4][col - col_dist//4]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col - 3*col_dist//4]
                    if (piece_in_between1 == 1 and piece_in_between2 == 1):
                        self.board[row][col] = 2
                        self.board[row - row_dist//4][col - col_dist//4] = 0
                        self.board[row - 3*row_dist//4][col - 3*col_dist//4] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                # Z-like Pattern 
                elif (col_dist == 0):

                    # The Pawn eats to the Left (Looking at the Chess Board) 
                    piece_in_between1 = self.board[row - row_dist//4][col - 1]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col - 1]
                    if (piece_in_between1 == 1 and piece_in_between2 == 1):
                        self.board[row][col] = 2
                        self.board[row - row_dist//4][col - 1] = 0
                        self.board[row - 3*row_dist//4][col - 1] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                    # The Pawn eats to the Right (Looking at the Chess Board) 
                    piece_in_between1 = self.board[row - row_dist//4][col + 1]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col + 1]
                    if (piece_in_between1 == 1 and piece_in_between2 == 1):
                        self.board[row][col] = 2
                        self.board[row - row_dist//4][col + 1] = 0
                        self.board[row - 3*row_dist//4][col + 1] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

            # King
            if (piece_value == 4):

                # Diagonal Pattern
                if (abs(row_dist) == 4 and abs(col_dist) == 4):
                    piece_in_between1 = self.board[row - row_dist//4][col - col_dist//4]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col - 3*col_dist//4]
                    if ((piece_in_between1 == 1 or piece_in_between1 == 3) and 
                            (piece_in_between2 == 1 or piece_in_between2 == 3)):
                        self.board[row][col] = 4
                        self.board[row - row_dist//4][col - col_dist//4] = 0
                        self.board[row - 3*row_dist//4][col - 3*col_dist//4] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                # Z-like Pattern Horizontally
                if (abs(col_dist) == 4 and row_dist == 0):

                    # The King eats ahead 
                    piece_in_between1 = self.board[row - 1][col - col_dist//4]
                    piece_in_between2 = self.board[row - 1][col - 3*col_dist//4]
                    if ((piece_in_between1 == 1 or piece_in_between1 == 3) and 
                            (piece_in_between2 == 1 or piece_in_between2 == 3)):
                        self.board[row][col] = 4
                        self.board[row - 1][col - col_dist//4] = 0
                        self.board[row - 1][col - 3*col_dist//4] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                    # The King eats behind
                    piece_in_between1 = self.board[row + 1][col - col_dist//4]
                    piece_in_between2 = self.board[row + 1][col - 3*col_dist//4]
                    if ((piece_in_between1 == 1 or piece_in_between1 == 3) and 
                            (piece_in_between2 == 1 or piece_in_between2 == 3)):
                        self.board[row][col] = 4
                        self.board[row + 1][col - col_dist//4] = 0
                        self.board[row + 1][col - 3*col_dist//4] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                # Z-like Pattern Vertically
                if (abs(row_dist) == 4 and col_dist == 0):

                    # The King eats to the right
                    piece_in_between1 = self.board[row - row_dist//4][col + 1]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col + 1]
                    if ((piece_in_between1 == 1 or piece_in_between1 == 3) and 
                            (piece_in_between2 == 1 or piece_in_between2 == 3)):
                        self.board[row][col] = 4
                        self.board[row - row_dist//4][col + 1] = 0
                        self.board[row - 3*row_dist//4][col + 1] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

                    # The King eats the left
                    piece_in_between1 = self.board[row - row_dist//4][col - 1]
                    piece_in_between2 = self.board[row - 3*row_dist//4][col - 1]
                    if ((piece_in_between1 == 1 or piece_in_between1 == 3) and 
                            (piece_in_between2 == 1 or piece_in_between2 == 3)):
                        self.board[row][col] = 4
                        self.board[row - row_dist//4][col - 1] = 0
                        self.board[row - 3*row_dist//4][col - 1] = 0
                        self.board[self.selected_piece_row][self.selected_piece_col] = 0
                        return True

        return False

    # Controls Whether a Pawn has to be Promoted to King
    def checkPromotion(self) -> None:
        
        # White Promotion
        for col, piece in enumerate(self.board[0]): 
            if (piece == 1):
                self.board[0][col] = 3
        # Black Promotion
        for col, piece in enumerate(self.board[7]):
            if (piece == 2):
                self.board[7][col] = 4

    # Starts the Game
    def startGame(self) -> None:

        # Hides Start Menu and Displays the Board
        for row in self.boardUI:
            for button in row:
                button.show()
        self.displayBoard()
        self.start_menu_button.hide()
        self.start_menu_title.hide()

    # Checks if Game has Ended
    def gameEnded(self) -> None:

        # Check if White Player has Won
        self.winner = "White"
        for row in self.board:
            for piece in row:
                if piece == 2 or piece == 4:
                    self.winner = None
                    break

        if self.winner is not None:
            return True

        # Check if Black Player has Won
        self.winner = "Black"
        for row in self.board:
            for piece in row:
                if piece == 1 or piece == 3:
                    self.winner = None
                    break

        return False if (self.winner is None) else True

    # Displays Restart Menu
    def displayRestartMenu(self) -> None:

        # Hides Board and Displays Menu
        for row in self.boardUI:
            for piece in row:
                piece.hide()
        if self.winner is None:
            title = "Draw"
        else:
            title = "{Player} has Won!".format(Player=self.winner)
        self.restart_menu_title.setText(title)
        self.restart_menu_title.show()
        self.restart_menu_button.show()

        # Restart Game
        self.board = [
                [2, 0, 2, 0, 2, 0, 2, 0],
                [0, 2, 0, 2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2, 0, 2, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
        ]
        self.state = 0
        self.turn = 0
        self.winner = None
        self.selected_piece_row = None
        self.selected_piece_col = None

    # Displays the Start Menu
    def displayStartMenu(self) -> None:

        # Hides Button and Displays Menu
        for row in self.boardUI:
            for button in row:
                button.hide()
        self.start_menu_button.show()
        self.start_menu_title.show()

    # Displays the board
    def displayBoard(self) -> None:

        for row, row_cells in enumerate(self.board):
            for col, cell in enumerate(row_cells):

                # Adds the Image to the Button
                if (cell == 2):
                    image = "assets/BlackPawn.png"
                elif (cell == 1):
                    image = "assets/WhitePawn.png"
                elif (cell == 3):
                    image = "assets/WhiteKing.png"
                elif (cell == 4):
                    image = "assets/BlackKing.png"
                elif (cell == 0):
                    color = "Black" if ((row + col) % 2 == 0) else "White"
                    image = "assets/{}Empty.png".format(color)
                self.boardUI[row][col].setIcon(QtGui.QIcon(image))
                self.boardUI[row][col].setIconSize(QtCore.QSize(self.cell_side, self.cell_side))


    def retranslateUi(self, MainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
