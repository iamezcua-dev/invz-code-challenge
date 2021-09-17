from unittest import TestCase

from modules.functions import evolve_matrix


class MyTestCase(TestCase):

    def test_evolve_matrix(self):
        matrix = [[0, 0, 1],
                  [0, 1, 0],
                  [1, 0, 0]]

        expected = [[0, 1, 1],
                    [1, 1, 1],
                    [1, 1, 0]]

        actual = evolve_matrix(matrix)
        self.assertListEqual(expected, actual)
