import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )


    def test_maze_create_cells_with_win(self):
        num_cols = 15
        num_rows = 13
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_with_win_and_draw(self):
        num_cols = 8
        num_rows = 6
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        # Check if cells are drawn correctly
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertIsNotNone(m1._Maze__cells[i][j])
                self.assertTrue(hasattr(m1._Maze__cells[i][j], 'draw'))
                self.assertTrue(hasattr(m1._Maze__cells[i][j], 'has_left_wall'))
                self.assertTrue(hasattr(m1._Maze__cells[i][j], 'has_top_wall'))
                self.assertTrue(hasattr(m1._Maze__cells[i][j], 'has_right_wall'))
                self.assertTrue(hasattr(m1._Maze__cells[i][j], 'has_bottom_wall'))
                self.assertTrue(hasattr(m1._Maze__cells[i][j], 'draw_move'))
    
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )


if __name__ == "__main__":
    unittest.main()