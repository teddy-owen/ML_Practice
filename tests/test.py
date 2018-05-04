import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))


from package import main


class TestMain(unittest.TestCase):

    def test_add_one_1(self):
        self.assertEqual(main.add_one(1), 2)

    def test_add_one_negative(self):
        self.assertEqual(main.add_one(-20), -19)

    def test_add_one_zero(self):
        self.assertEqual(main.add_one(0), 1)

    def test_add_one_float(self):
        self.assertEqual(main.add_one(0.1), 1.1)


if __name__ == '__main__':
    unittest.main()
