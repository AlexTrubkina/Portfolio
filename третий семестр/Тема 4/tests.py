from vsr import fact
import unittest


class TestFunFact(unittest.TestCase):

    def test1(self):
        self.assertEqual(fact(1), 1)

    def test2(self):
        self.assertEqual(fact(2), 2)

    def test3(self):
        self.assertEqual(fact(4), 24)

    def test4(self):
        with self.assertRaises(ValueError):
            fact("")

    def test5(self):
        with self.assertRaises(ValueError):
            fact([2, 5, 6])

    def test6(self):
        with self.assertRaises(ValueError):
            fact([1])

    def test7(self):
        with self.assertRaises(ValueError):
            fact({3})

    def test8(self):
        with self.assertRaises(ValueError):
            fact(5.1)

    def test9(self):
        with self.assertRaises(ValueError):
            fact(-1)



if __name__ == '__main__':
    unittest.main()
