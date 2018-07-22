import unittest


class TestAddition(unittest.TestCase):
    def setUp(self):
        print("Setting up the test")

    def tearDown(self):
        print("Tearing down the test")

    def test_two_plus_two(self):
        total = 2 + 2
        self.assertEqual(4, total)  # 1st is Expected, 2nd is Actual

    def test_two_plus_three(self):
        total = 2 + 3
        self.assertEqual(5, total)  # 1st is Expected, 2nd is Actual


if __name__ == '__main__':
    unittest.main()
