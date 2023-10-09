from typing import Dict, List

import numpy as np
from numpy.typing import NDArray


class GameOfLife:
    """
    Class that implements Conway's Game of Life
    """

    def __init__(self, grid: Dict = None, x: int = 50, y: int = 50):
        self.grid = self.parse_grid(grid) if grid else self.generate_grid(x, y)

    @staticmethod
    def generate_grid(x: int, y: int) -> NDArray[int]:
        """
            Generate the grid as matrix of 0 1 with size x and y
        """
        return np.random.choice([0, 1], (x, y))

    @staticmethod
    def parse_grid(grid: dict) -> NDArray[int]:
        """
            Parse existing grid from json
        """
        return np.array(grid['game'])

    def update_grid(self):
        """
        Update the grid by the rules specified on GameOfLife
        see https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
        """
        new_grid = self.grid.copy()
        rows, cols = self.grid.shape

        for x in range(rows):
            for y in range(cols):
                neighbors = np.sum(
                    self.grid[max(x - 1, 0):min(x + 2, rows), max(y - 1, 0):min(y + 2, cols)]
                ) - self.grid[x, y]

                if self.grid[x, y] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[x, y] = 0
                else:
                    if neighbors == 3:
                        new_grid[x, y] = 1

        self.grid = new_grid

    def get_grid(self) -> Dict[str, List[List[int]]]:
        """
        Retrieves the current state of the grid.
        :return: Dictionary with 'key' game and value grid of the game.
        """
        return {'game': self.grid.tolist()}

    def __str__(self):
        """
            :return: Matrix representation of the game as a string
        """
        return str(self.grid)
