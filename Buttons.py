import Button
class Buttons:


    def __init__(self, width):
        alphabet_string = string.ascii_lowercase
        self.letters = list(alphabet_string)
        self.dict = {}


    def determineNumRowsNCols4Buttons():
        widthMinusMargin = width - 2 * Button.WIDTH
        numCols = widthMinusMargin // Button.WIDTH
        numRows = (26 // numCols) + 1
        return [numRows, numCols]

    def detemineButtonPos4All() {
        numR, numC = self.determineNumRowsNCols4Buttons()
        startX = (width - numC * Button.WIDTH) / 2.0
    }
    
