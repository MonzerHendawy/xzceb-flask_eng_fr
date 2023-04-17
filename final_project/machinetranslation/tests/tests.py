"""
script to test englishToFrench and frenchToEnglish functions
"""
import unittest
from translator import englishToFrench, frenchToEnglish

class testEnglishToFrench(unittest.TestCase):
    #tests for englishToFrench function
    def test1(self):
        #test translation of hello equals bonjour
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        #test translation of null text is not equal to null
        self.assertNotEqual(englishToFrench(""),"")

class testFrenchToEnglish(unittest.TestCase):
    #tests for frenchToEnglish function
    def test1(self):
        #test translation of bonjour equals hello
        self.assertEqual(frenchToEnglish("bonjour"), "Hello")
        #test translation of null text is not equal to null
        self.assertNotEqual(frenchToEnglish(""),"")

unittest.main()
