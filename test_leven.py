''' pytest unittests for LevenshteinCalc '''
import leven

class TestLeven():
    ''' Unit test class for LevenshteinCalc '''
    def setup_method(self):
        ''' setup function to create the class instance '''
        self.levensthein_calc = leven.LevenshteinCalc(False)

    def test_distance(self):
        ''' Test the Levenshtein distance '''
        assert self.levensthein_calc.calculate_distance('foo', 'Foo') == 1

    def test_distance_ignore_case(self):
        ''' Test the Levenshtein distance
        and verify case is ignored'''
        assert self.levensthein_calc.calculate_distance_ignore_case('foo', 'Foo') == 0
