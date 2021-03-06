import unittest

from latexfixer import fix

class Test_LatexTest(unittest.TestCase):

    def setUp(self):
        self.lf = fix.LatexText

    def init(self, text):
        self.tm = self.lf(text)

    def test_tostring(self):
        string = 'Hello world'
        self.init(string)
        string = self.tm.tostring()
        self.assertIsInstance(string, str)
        self.assertNotIsInstance(string, self.lf)
        
    def test__sentence_to_interstitial_spacing(self):
        test_strings = [('Hello world.', 'Hello world.'),
                        ('A greeting, e.g. to a friend.',
                            'A greeting, e.g.\ to a friend.'),
                        ('Hello, Prof. World', 'Hello, Prof.~World')]
        for phrase, processed_phrase in test_strings:
            self.init(phrase)
            self.assertEqual(self.tm, processed_phrase)

    def test__interstitial_to_sentence_spacing(self):
        pass

    def test__latex_symbols(self):
        pass

    def test__whitespace_substitution(self):
        pass

    def test__hyphens_to_dashes(self):
        pass

    def test__str_replacement(self):
        pass

    def test__regex_replacement(self):
        pass