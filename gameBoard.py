from point import Point

class Cell:
    def __init__(self, position, is_alive):
        self.position = position
        self.is_alive = is_alive
        
class GameBoard:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.board = [[False] * grid_size[1] for x in range(grid_size[0])]

    def set_cell(self, position, is_alive):
        self.board[position.x][position.y] = is_alive

    def is_cell_alive(self, position):
        try:
            return self.board[position.x][position.y]
        except IndexError:
            return False

    def _adjacent_cell_positions(self, position):
        (x, y) = position

        def boundary_points():
            yield Point(x-1, y-1)
            yield Point(x, y-1)
            yield Point(x+1, y-1)

            yield Point(x-1, y)
            yield Point(x+1, y)

            yield Point(x-1, y+1)
            yield Point(x, y+1)
            yield Point(x+1, y+1)            

        for point in boundary_points():
            if self._is_valid_cell_location(point):
                yield point

    def _is_valid_cell_location(self, position):
        if position.x < 0 or position.y < 0:
            return False

        if position.x > self.grid_size[0] or position.y > self.grid_size[1]:
            return False

        return True

    def _adjacent_cells(self, position):
        for pos in self._adjacent_cell_positions(position):
            yield Cell(pos, self.is_cell_alive(pos))

    def _num_living_adjacent_cells(self, position):
        return sum(map(lambda cell: cell.is_alive, self._adjacent_cells(position)))
        
    def _should_be_alive_in_next_gen(self, position):
        living_adjacents = self._num_living_adjacent_cells(position)
        if self.board[position.x][position.y]:
            # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            if living_adjacents < 2:
                return False
            # Any live cell with two or three live neighbours lives on to the next generation.
            if living_adjacents == 2 or living_adjacents == 3:
                return True
            # Any live cell with more than three live neighbours dies, as if by overpopulation.
            return False
        else:
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if living_adjacents == 3:
                return True
            else:
                return False


    def next_generation(self):
        next = GameBoard(self.grid_size)
        for x in range(len(next.board)):
            for y in range(len(next.board[x])):
                next.board[x][y] = self._should_be_alive_in_next_gen(Point(x, y))
            
        return next     

    def cells(self) -> Cell:
        for (x, row) in enumerate(self.board):
            for (y, is_alive) in enumerate(row):
                yield Cell(Point(x, y), is_alive)


