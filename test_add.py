from main_add import sum
import unittest

class AddFunctions(unittest.TestCase):

    def setUp(self):
        self.int1 = 5
        self.int2 = 8
        self.int3 = 3
        self.float1 = 4.5
        self.float2 = 9.2
        self.string = "hai"
        self.bool1 = True
        self.bool2 = False

    def test_one_argument(self):
        self.assertTrue(sum(self.int1, self.int2))

    def test_one_argument(self):
        self.assertTrue(sum(self.float1, self.float1))

    def test_one_argument(self):
        self.assertFalse(sum(self.string, self.int1), msg="The input argument should not be a string")

    def test_one_argument(self):
        self.assertFalse(sum(self.int1, self.int2, self.int3), msg="The number  of input arguments must always be 2")

    def test_one_argument(self):
        self.assertFalse(sum(self.bool1, self.bool2), msg="The input argument should not contain boolean value")