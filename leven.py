''' Example to test different unit test frameworks '''
import nltk

class LevenshteinCalc():
    ''' Simple class to calculate Levenshtein distance '''
    def calculate_distance(self, word_a, word_b):
        ''' Calculate and return the Levenshtein distance '''
        distance = nltk.edit_distance(word_a, word_b)
        return distance
    def calculate_distance_ignore_case(self, word_a, word_b):
        ''' Calculate and return the Levenshtein distance
            but ignore upper or lower case '''
        distance = self.calculate_distance(word_a.lower(), word_b.lower())
        return distance
