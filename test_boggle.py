import unittest
import boggle


class TestBoggle(unittest.TestCase):
    """
    Out Test Suire for boggle solver
    """
        
    def test_can_can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty grid
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid),0)
    
    def test_grid_size_is_width_times_height(self):
        """
        Test is to ensure that the total size of the grid
        is equsl to width * height
        """
        grid = boggle.make_grid(2,3)
        self.assertEqual(len(grid),6)
