class Cell:
    def __init__(self, position, isAlive):
        self.position = position
        self.isAlive = isAlive
        
class GameBoard:
    def __init__(self, gridSize):
        self.gridSize = gridSize
        self.board = []
        for x in range(gridSize[0]):
            row = []
            for y in range(gridSize[1]):
                row.append(False)
            
            self.board.append(row)

    def setCell(self, position, isAlive):
        (x, y) = position
        self.board[x][y] = isAlive

    def isCellAlive(self, position):
        (x, y) = position
        if x < 0 or y < 0:
            return False

        if x >= len(self.board) or y >= len(self.board[0]):
            return False

        return self.board[x][y]

    def adjacentCellPositions(self, position):
        (x, y) = position
        yield (x-1, y-1)
        yield (x, y-1)
        yield (x+1, y-1)

        yield (x-1, y)
        yield (x+1, y)

        yield (x-1, y+1)
        yield (x, y+1)
        yield (x+1, y+1)            

    def adjacentCells(self, position):
        for pos in self.adjacentCellPositions(position):
            yield (pos[0], pos[1], self.isCellAlive(pos))

    def numLivingAdjacentCells(self, position):
        return sum(map(lambda x: x[2] , self.adjacentCells(position)))
        
    def shouldBeAliveInNextGen(self, position):
        (x, y) = position
        livingAdjacents = self.numLivingAdjacentCells(position)
        if self.board[x][y]:
            # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            if livingAdjacents < 2:
                return False
            # Any live cell with two or three live neighbours lives on to the next generation.
            if livingAdjacents == 2 or livingAdjacents == 3:
                return True
            # Any live cell with more than three live neighbours dies, as if by overpopulation.
            return False
        else:
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if livingAdjacents == 3:
                return True
            else:
                return False


    def nextGeneration(self):
        next = GameBoard(self.gridSize)
        for x in range(len(next.board)):
            for y in range(len(next.board[x])):
                next.board[x][y] = self.shouldBeAliveInNextGen((x, y))
            
        return next     

    def cells(self):
        for (x, row) in enumerate(self.board):
            for (y, isAlive) in enumerate(row):
                yield Cell((x, y), isAlive)


