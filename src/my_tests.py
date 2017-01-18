import unittest

class MyTests(unittest.TestCase):
    def testPEP498(self):
        import format_example as fe
        self.assertEqual(fe.compute_sum(3.5, 1.2, 2), "3.5 + 1.2 = 4.7")
        self.assertEqual(fe.compute_sum(1.2345, 0.2, 2), "1.2345 + 0.2 = 1.4")
        self.assertEqual(fe.compute_sum(3.1415, 5, 3), "3.1415 + 5 = 8.14")
        self.assertEqual(fe.compute_sum(3.5, 1.2, 1), "3.5 + 1.2 = 5e+00")
