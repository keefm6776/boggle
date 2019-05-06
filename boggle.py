def make_grid(width, height):
    """
    Creates a grid that will hold all of the tiles
    for a boggle game.
    """
    return {(row,col):' ' for row in range(height)
        for col in range(width)
    }
    
def test_grid_coordinates(self):
    """
    Test to ensure that all of the coordinates
    inside the grid can be accessed
    """
    
    grid = boggle.make_grid(2, 2)
    self.assertIn((0,0),grid)
    self.assertIn((0,1),grid)
    self.assertIn((1,0),grid)
    self.assertIn((1,1),grid)
    self.assertNotIn((2,2),grid)
    
    