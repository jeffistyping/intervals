from interval import Interval
import unittest

class TestIntervalMethods(unittest.TestCase):

    def test_add(self):
        interval = Interval()
        interval.Add((1,4))
        self.assertEqual(str(interval), 'Intervals: {[(1, 4)]}')

    def test_delete(self):
        interval = Interval([(1,10)])
        interval.Delete((6,10))
        self.assertEqual(str(interval), 'Intervals: {[(1, 6)]}')

    def test_get(self):
        interval = Interval([(1,10)])
        self.assertEqual(str(interval.Get((1,20))), '[(1, 10)]')

if __name__ == '__main__':
    unittest.main()
