import random

import ledwall.components as comp

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

S_SHAPE_TEMPLATE = [
    [".....", ".....", "..OO.", ".OO..", "....."],
    [".....", "..O..", "..OO.", "...O.", "....."],
]

Z_SHAPE_TEMPLATE = [
    [".....", ".....", ".OO..", "..OO.", "....."],
    [".....", "..O..", ".OO..", ".O...", "....."],
]

I_SHAPE_TEMPLATE = [
    ["..O..", "..O..", "..O..", "..O..", "....."],
    [".....", ".....", "OOOO.", ".....", "....."],
]

O_SHAPE_TEMPLATE = [[".....", ".....", ".OO..", ".OO..", "....."]]

P_SHAPE_TEMPLATE = [[".....", ".....", "..O..", ".....", "....."]]

J_SHAPE_TEMPLATE = [
    [".....", ".O...", ".OOO.", ".....", "....."],
    [".....", "..OO.", "..O..", "..O..", "....."],
    [".....", ".....", ".OOO.", "...O.", "....."],
    [".....", "..O..", "..O..", ".OO..", "....."],
]

L_SHAPE_TEMPLATE = [
    [".....", "...O.", ".OOO.", ".....", "....."],
    [".....", "..O..", "..O..", "..OO.", "....."],
    [".....", ".....", ".OOO.", ".O...", "....."],
    [".....", ".OO..", "..O..", "..O..", "....."],
]

T_SHAPE_TEMPLATE = [
    [".....", "..O..", ".OOO.", ".....", "....."],
    [".....", "..O..", "..OO.", "..O..", "....."],
    [".....", ".....", ".OOO.", "..O..", "....."],
    [".....", "..O..", ".OO..", "..O..", "....."],
]

C_SHAPE_TEMPLATE = [
    [".....", "..O..", "..OO.", ".....", "....."],
    [".....", ".....", "..OO.", "..O..", "....."],
    [".....", ".....", ".OO..", "..O..", "....."],
    [".....", "..O..", ".OO..", ".....", "....."],
]

D_SHAPE_TEMPLATE = [
    [".....", "..O..", "..O..", ".....", "....."],
    [".....", ".....", ".OO..", ".....", "....."],
]

BLANK = "."

PIECES = {
    "S": S_SHAPE_TEMPLATE,
    "Z": Z_SHAPE_TEMPLATE,
    "I": I_SHAPE_TEMPLATE,
    "J": J_SHAPE_TEMPLATE,
    "L": L_SHAPE_TEMPLATE,
    "O": O_SHAPE_TEMPLATE,
    "T": T_SHAPE_TEMPLATE,
    "P": P_SHAPE_TEMPLATE,
    "C": C_SHAPE_TEMPLATE,
    "D": D_SHAPE_TEMPLATE,
}

PIECES_COLOR = {
    "S": (47, 20, 201),
    "Z": (47, 20, 201),
    "I": (47, 20, 201),
    "J": (47, 20, 201),
    "L": (47, 20, 201),
    "O": (47, 20, 201),
    "T": (47, 20, 201),
    "P": (47, 20, 201),
    "C": (47, 20, 201),
    "D": (47, 20, 201),
    BLANK: (0, 0, 0),
    "B": (255, 0, 0),
}


"""
PIECES_COLOR = {'S': (255, 0, 0),
                'Z': (255, 255, 0),
                'I': (0, 255, 0),
                'J': (0, 255, 255),
                'L': (255, 0, 255),
                'O': (0, 0, 255),
                'T': (255, 100, 255),
                'P': (86, 244, 66),
                'C': (255, 249, 226),
                'D': (152, 47, 175),
                BLANK: (0, 0, 0),
                'B': (255, 255, 255),
                }
"""

# PIECES_ORDER = {'S': 0,'Z': 1,'I': 2,'J': 3,'L': 4,'O': 5,'T': 6}


class Tetris(object):
    OVERFLOW_LEFT = 0
    OVERFLOW_RIGHT = 1
    OVERFLOW_BOTTOM = 2
    OVERFLOW_TOP = 3
    COLLISION = 4
    VALID_POSITION = 5

    def __init__(self, display):
        self._display = display
        self._currentPiece = self.get_new_piece()
        self._matrix = [[BLANK for x in range(display.columns)] for y in range(display.rows)]
        self._falling_speed = 0.1

    @property
    def piece(self):
        return self._currentPiece

    @property
    def matrix(self):
        return self._matrix

    @property
    def width(self):
        return self._display.columns

    @property
    def height(self):
        return self._display.rows

    def set_block_color(self, block_id, color):
        if block_id not in PIECES.keys():
            raise ValueError("Uknown block id")
        PIECES_COLOR[block_id] = tuple(comp.Color.convert(color))

    def set_background_color(self, color):
        PIECES_COLOR[BLANK] = tuple(comp.Color.convert(color))

    @property
    def block_ids(self):
        return PIECES.keys()

    def fallDown(self):
        if self._currentPiece is None:
            return False

    def clearMatrix(self):
        for x in range(self.width):
            for y in range(self.height):
                self.matrix[x][y] = BLANK

    def isRowComplete(self, row):
        for x in range(self.width):
            if self.matrix[x][row] == BLANK:
                return False
        return True

    def isColumnComplete(self, column):
        if column < 0 or column >= self.width:
            raise ValueError("Column value out of range")

        for y in range(self.height):
            if self.matrix[column][y] == BLANK:
                return False
        return True

    def dissolveColumn(self, column):
        for y in range(self.height):
            self._matrix[column][y] = "B"

        for val in range(255, 0, -25):
            # Set the color for the column
            PIECES_COLOR["B"] = (val, val, val)
            self.writeMatrixToDisplay()
            # self._display.update()

        PIECES_COLOR["B"] = [255, 255, 255]

    def getCompletedColumns(self):
        result = []
        for x in range(self.width):
            if self.isColumnComplete(x):
                result += [x]
        return result

    def getCompletedRows(self):
        result = []
        for y in range(self.height):
            if self.isRowComplete(y):
                result += [y]
        return result

    def deleteRow(self, row):
        # Move rows down.
        for y in range(row - 1, -1, -1):
            for x in range(self.width):
                self._matrix[x][y + 1] = self._matrix[x][y]

        # Insert a new blank row at he top.
        for x in range(self.width):
            self._matrix[x][0] = BLANK

    def deleteColumn(self, column):
        for y in range(self.height):
            self._matrix[column][y] = BLANK

    def deleteCompleteRows(self):
        deletedRows = 0
        for y in range(self.height - 1, -1, -1):
            while self.isRowComplete(y):
                deletedRows += 1
                self.deleteRow(y)
        return deletedRows

    def deleteCompleteColumns(self):
        for c in self.getCompletedColumns():
            self.deleteColumn(c)

    def getShape(self, piece=None):
        piece = self.__ensurePiece(piece)

        return PIECES[piece["shape"]][piece["rotation"]]

    def update(self):
        self.writeMatrixToDisplay()
        if self._currentPiece:
            self.drawPiece(self._currentPiece)
        # self._display.update()

    def writePieceToMatrix(self, piece=None):
        piece = self.__ensurePiece(piece)

        shape = self.getShape(piece)
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if shape[y][x] != BLANK:
                    mx = x + piece["x"]
                    my = y + piece["y"]
                    if not (not (0 <= mx < self.width) or not (0 <= my < self.height)):
                        self.matrix[mx][my] = piece["shape"]

    def writeMatrixToDisplay(self):
        for x in range(self.width):
            for y in range(self.height):
                shape = self.matrix[x][y]
                self._display.set_pixel(x, y, PIECES_COLOR[shape])

    def setBrickAt(self, x, y):
        self.matrix[x][y] = "B"

    def rotateCW(self, piece=None):
        piece = self.__ensurePiece(piece)

        shape = piece["shape"]
        piece["rotation"] += 1
        piece["rotation"] %= len(PIECES[shape])

    def rotateCCW(self, piece=None):
        piece = self.__ensurePiece(piece)

        shape = piece["shape"]
        piece["rotation"] += len(PIECES[shape])
        piece["rotation"] -= 1
        piece["rotation"] %= len(PIECES[shape])

    def new_piece(self):
        self._currentPiece = self.get_new_piece()

    def get_new_piece(self):
        # return a random new piece in a random rotation and color
        shape = random.choice(list(PIECES.keys()))
        new_piece = {
            "shape": shape,
            "rotation": random.randint(0, len(PIECES[shape]) - 1),
            "x": int(self.width / 2) - int(TEMPLATEWIDTH / 2),
            "y": -3,  # start it above the board (i.e. less than 0)
            "color": (124, 218, 255),
        }
        return new_piece

    def checkForCollision(self, piece=None, dx=0, dy=0):
        piece = self.__ensurePiece(piece)

        shapeToTest = self.getShape(piece)
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                mx = x + piece["x"] + dx
                my = y + piece["y"] + dy
                if mx >= 0 and mx < self.width and my >= 0 and my < self.height:
                    if shapeToTest[y][x] != BLANK and self.matrix[mx][my] != BLANK:
                        return Tetris.COLLISION
        return Tetris.VALID_POSITION

    def isOnBoard(self, piece=None, dx=0, dy=0):
        """Test if the bounds of the piece are on the
           display. It is ok that the piece extends the upper
           border.
        """
        piece = self.__ensurePiece(piece)
        x = piece["x"] + dx
        y = piece["y"] + dy

        return x >= 0 and x + TEMPLATEWIDTH < self.width and y + TEMPLATEHEIGHT < self.height

    def __ensurePiece(self, piece):
        if piece is None:
            piece = self._currentPiece
        if piece is None:
            raise ValueError("Provided pice is None and we have no 'currentPiece'")
        return piece

    def moveX(self, piece=None, val=0):
        piece = self.__ensurePiece(piece)
        piece["x"] += val

    def testOverflowX(self, piece=None, dx=0, dy=0):
        piece = self.__ensurePiece(piece)
        shapeToTest = self.getShape(piece)

        px = piece["x"] + dx
        # py = piece['y'] + dy

        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if px + x < 0 and shapeToTest[y][x] != BLANK:
                    return Tetris.OVERFLOW_LEFT

                elif px + x >= self.width and shapeToTest[y][x] != BLANK:
                    return Tetris.OVERFLOW_RIGHT
        return Tetris.VALID_POSITION

    def testOverflowY(self, piece=None, dx=0, dy=0):
        piece = self.__ensurePiece(piece)
        shapeToTest = self.getShape(piece)

        # px = piece['x'] + dx
        py = piece["y"] + dy

        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if py + y >= self.height and shapeToTest[y][x] != BLANK:
                    return Tetris.OVERFLOW_BOTTOM
                if py + y < 0 and shapeToTest[y][x] != BLANK:
                    return Tetris.OVERFLOW_TOP

        return Tetris.VALID_POSITION

    def isValidPosition(self, piece=None, dx=0, dy=0):
        piece = self.__ensurePiece(piece)
        if self.isOnBoard(piece, dx, dy):
            return not self.checkForCollision(piece, dx, dy)

        shapeToTest = self.getShape(piece)
        px = piece["x"] + dx
        py = piece["y"] + dy

        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if px + x < 0 and shapeToTest[y][x] != BLANK:
                    return Tetris.OVERFLOW_LEFT

                elif px + x >= self.width and shapeToTest[y][x] != BLANK:
                    return Tetris.OVERFLOW_RIGHT

                if py + y >= self.height and shapeToTest[y][x] != BLANK:
                    return Tetris.OVERFLOW_BOTTOM

                if shapeToTest[y][x] != BLANK and self.matrix[px + x][py + y] != BLANK:
                    return Tetris.COLLISION
        return Tetris.VALID_POSITION

    def copyRow(self, src, dst):
        for x in range(self.width):
            self.matrix[x][dst] = self.matrix[x][src]

    def drawPiece(self, piece=None, pixelx=None, pixely=None):
        piece = self.__ensurePiece(piece)
        shapeToDraw = self.getShape(piece)
        if pixelx == None and pixely == None:
            # if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
            pixelx = piece["x"]
            pixely = piece["y"]

        # draw each of the boxes that make up the piece
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if shapeToDraw[y][x] != BLANK:
                    px = x + pixelx
                    py = y + pixely
                    if py >= 0 and py < self.height and px >= 0 and py < self.width:
                        self._display.set_pixel(px, py, piece["color"])
