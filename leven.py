''' Example to test different unit test frameworks '''
import nltk

class LevenshteinCalc():
    ''' Simple class to calculate Levenshtein distance '''
    def __init__(self, ignore_case):
        ''' Constructor that accepts option to ignore case '''
        self.ignore_case = ignore_case

    def calculate_distance(self, word_a, word_b):
        ''' Calculate and return the Levenshtein distance '''
        if self.ignore_case == True:
            word_a = word_a.lower()
            word_b = word_b.lower()
        distance = nltk.edit_distance(word_a, word_b)
        return distance

    def calculate_distance_ignore_case(self, word_a, word_b):
        ''' Calculate and return the Levenshtein distance
            but ignore upper or lower case '''
        distance = self.calculate_distance(word_a.lower(), word_b.lower())
        return distance
