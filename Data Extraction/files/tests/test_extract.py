import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import extract

# TODO: Unit Tests for extract.py
class TestExtract(unittest.TestCase):
    
    def test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()