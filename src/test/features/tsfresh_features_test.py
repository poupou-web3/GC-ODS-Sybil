import unittest

import numpy as np

from src.main.features.custom.extract import time_since_first, time_since_last, ratio_tx_time_since_time, ratio_tx_time_since_last_tx, ratio_above_mean, ratio_above, ratio_between_quartiles


class TsfreshFeaturesTests(unittest.TestCase):
    x_ones = np.ones(10)
    x_add_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    current_time = 11

    def test_time_since_first(self):
        result = time_since_first(self.x_add_1, self.current_time)
        self.assertEqual(10, result)
    
    def test_time_since_last(self):
        result = time_since_first(self.x_add_1, time)
        self.assertEqual(1, result)

    def test_ratio_tx_time_since_time(self):
        time = 3
        result = ratio_tx_time_since_time(self.x_add_1, self.current_time, time)
        self.assertEqual(2/9, result)

    def test_ratio_tx_time_since_last_tx(self):
        time = 3
        result = ratio_tx_time_since_time(self.x_add_1, time)
        self.assertEqual(4/9, result)

    def test_ratio_above_mean(self):
        time = 3
        result = ratio_above_mean(self.x_add_1)
        self.assertEqual(0, result)

    def test_ratio_above(self):
        time = 3
        result = ratio_above(self.x_add_1, 5)
        self.assertEqual(5/9, result)

    def test_ratio_between_quartiles(self):
        result = ratio_above(self.x_add_1, 20, 80)
        self.assertEqual(7/9, result)


if __name__ == '__main__':
    unittest.main()
