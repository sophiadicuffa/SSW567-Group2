import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import get_numeric_score as numscore

# TODO: Unit Tests for get_numeric_score.py
class TestGetNumericScore(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()