import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import auto_score as asc

class TestAutoScore(unittest.TestCase):

    def test_score_python(self):
        """Test automatic scoring of Python code"""
        # TODO: Write a better test
        results = asc.score_python("example", 1) # Run to get (previous run) added to actual

        self.assertEqual(len(results), 1)
    
    def test_score_java(self):
        # TODO: Write Test
        pass

    def test_score_javascript(self):
        # TODO: Write Test
        pass

    def test_score_html(self):
        # TODO: Write Test
        pass

    def test_score_css(self):
        # TODO: Write Test
        pass

    def test_score_sql(self):
        # TODO: Write Test
        pass

    def test_score_csharp(self):
        # TODO: Write Test
        pass

    def test_score_cpp(self):
        # TODO: Write Test
        pass

    def test_score_c(self):
        # TODO: Write Test
        pass


if __name__ == '__main__':
    unittest.main()