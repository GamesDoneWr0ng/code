class Template:
    def __init__(self, board, notes) -> None:
        self.board = board
        self.notes = notes

    def getCol(self, idx):
        return self.board[:,idx]
    
    def getRow(self, idx):
        return self.board[idx]
    
    def getBox(self, idx):
        return self.board[3*(idx//3):3*(idx//3)+3, 3*(idx%3):3*(idx%3)+3].flatten()
    
    def noteGetCol(self, idx):
        return self.notes[:,idx]
    
    def noteGetRow(self, idx):
        return self.notes[idx]
    
    def noteGetBox(self, idx):
        return self.notes[3*(idx//3):3*(idx//3)+3, 3*(idx%3):3*(idx%3)+3].reshape(9,9)