import unittest
from gameBoard import GameBoard
from point import Point

class TestGameBoard(unittest.TestCase):
    def test_blinker_oscillator(self):
        # https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns
        # Blinker is an oscillator with period 2

        board = GameBoard((10, 10))

        # Make a blinker starting vertical
        # -X-
        # -X-
        # -X-

        board.set_cell(Point(4, 1), True)
        board.set_cell(Point(4, 2), True)
        board.set_cell(Point(4, 3), True)

        # Move to next generation
        board = board.next_generation()

        # The blinker should switch to horizontal
        # ---
        # XXX
        # ---
        self.assertFalse(board.is_cell_alive(Point(4, 1)))
        self.assertFalse(board.is_cell_alive(Point(4, 3)))

        self.assertTrue(board.is_cell_alive(Point(3, 2)))
        self.assertTrue(board.is_cell_alive(Point(4, 2)))
        self.assertTrue(board.is_cell_alive(Point(5, 2)))


        # Move to next generation again
        board = board.next_generation()

        # The blinker should switch back to vertical
        # -X-
        # -X-
        # -X-
        self.assertTrue(board.is_cell_alive(Point(4, 1)))
        self.assertTrue(board.is_cell_alive(Point(4, 2)))
        self.assertTrue(board.is_cell_alive(Point(4, 3)))

        self.assertFalse(board.is_cell_alive(Point(3, 2)))
        self.assertFalse(board.is_cell_alive(Point(5, 2)))        

        

if __name__ == '__main__':
    unittest.main()