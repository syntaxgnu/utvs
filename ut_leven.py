''' python unitttest module unittests for LevenshteinCalc '''

import unittest
import leven

class TestLeven(unittest.TestCase):
    ''' Unit test class for LevenshteinCalc '''
    def test_distance(self):
        ''' Test the Levenshtein distance '''
        levensthein_calc = leven.LevenshteinCalc()
        self.assertEqual(levensthein_calc.calculate_distance('foo', 'Foo'),1)

    def test_distance_ignore_case(self):
        ''' Test the Levenshtein distance
            and verify case is ignored'''
        levensthein_calc = leven.LevenshteinCalc()
        self.assertEqual(levensthein_calc.calculate_distance_ignore_case('foo', 'Foo'), 0)

if __name__ == '__main__':
    unittest.main()
