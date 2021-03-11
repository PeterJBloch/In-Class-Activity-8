import unittest
import fibonacci

class Test_Fibonacci(unittest.TestCase):
    def test_good(self):
        self.assertEqual(fibonacci.fib(0),1)
        self.assertEqual(fibonacci.fib(5),8)

    def test_bad(self):
        with self.assertRaises(RecursionError):
            fibonacci.fib(-1)

if __name__ == "__main__":
    unittest.main()