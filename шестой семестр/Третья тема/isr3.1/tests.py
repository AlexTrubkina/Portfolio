import main
import unittest

class EqTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.solve(0, 0, None), None)
        
    def test_2(self):
        self.assertEqual(main.solve(2, -1, 81), [2.5, -2])
        
    def test_3(self):
        self.assertEqual(main.diskriminant(-5, -12, 3), 204)
        
    def test_4(self):
        self.assertEqual(main.diskriminant(1, 2, 3), -8)
        
if __name__ == '__main__':
    unittest.main()
