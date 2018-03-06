# coding=utf-8
import unittest


class StringTestCase(unittest.TestCase):
    def setUp(self):
        self.test_string = "This is a string"

    def testReverse(self):
        self.assertEqual("gnirts a si sihT", self.test_string[::-1])

    def testSplit(self):
        expected = ["This", "is", "a", "string"]
        self.assertEqual(expected, self.test_string.split(" "))
        self.assertEqual(expected, self.test_string.split())

    def testLower(self):
        self.assertEqual("this is a string", self.test_string.lower())

    def testUpper(self):
        self.assertEqual("THIS IS A STRING", self.test_string.upper())

    def testRstrip(self):
        string = "This is a string            "
        self.assertEqual(self.test_string, string.rstrip())

    def testLstrip(self):
        string = "         This is a string"
        self.assertEqual(self.test_string, string.strip())


if __name__ == '__main__':
    unittest.main()
