import string

import Button
class Buttons:


    def __init__(self, width):
        self.width = width
        alphabet_string = string.ascii_lowercase
        self.letters = list(alphabet_string)
        self.dict = {}


    def determineNumRowsNCols4Buttons(self):
        widthMinusMargin = self.width - 2 * Button.WIDTH
        numCols = widthMinusMargin // Button.WIDTH
        numRows = (26 // numCols) + 1
        return [numRows, numCols]

    def determineButtonPos4All(self):
        numR, numC = self.determineNumRowsNCols4Buttons()
        startX = (self.width - numC * Button.WIDTH) / 2.0
        # UNDONE

    
