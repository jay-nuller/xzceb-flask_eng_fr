import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Man'), 'Homme')
        self.assertEqual(englishToFrench('Woman'), 'Femme')
        #self.assertIsNone(englishToFrench(None))
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Homme'), 'Man')
        self.assertEqual(frenchToEnglish('Femme'), 'Woman')
        #self.assertIsNone(frenchToEnglish(None))
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()