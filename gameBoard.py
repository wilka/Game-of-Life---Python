from point import Point

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
        self.board[position.x][position.y] = isAlive

    def isCellAlive(self, position):
        try:
            return self.board[position.x][position.y]
        except IndexError:
            return False

    def adjacentCellPositions(self, position):
        (x, y) = position
        yield Point(x-1, y-1)
        yield Point(x, y-1)
        yield Point(x+1, y-1)

        yield Point(x-1, y)
        yield Point(x+1, y)

        yield Point(x-1, y+1)
        yield Point(x, y+1)
        yield Point(x+1, y+1)            

    def adjacentCells(self, position):
        for pos in self.adjacentCellPositions(position):
            yield Cell(pos, self.isCellAlive(pos))

    def numLivingAdjacentCells(self, position):
        return sum(map(lambda cell: cell.isAlive, self.adjacentCells(position)))
        
    def shouldBeAliveInNextGen(self, position):
        livingAdjacents = self.numLivingAdjacentCells(position)
        if self.board[position.x][position.y]:
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
                next.board[x][y] = self.shouldBeAliveInNextGen(Point(x, y))
            
        return next     

    def cells(self) -> Cell:
        for (x, row) in enumerate(self.board):
            for (y, isAlive) in enumerate(row):
                yield Cell(Point(x, y), isAlive)


