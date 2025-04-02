import unittest
import random
from Api.main import calculate_price

class TestCryptoCalculator(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test fixtures
        self.test_cases = [
            (random.uniform(1000, 100000), random.uniform(0.1, 10))
            for _ in range(5)
        ]

    def test_calculate_price(self):
        for crypto_price, amount in self.test_cases:
            # Expected result should be price * amount * 2
            expected = crypto_price * amount 
            
            # Actual result from our function
            result = calculate_price(crypto_price, amount)
            
            # Test will fail because we expect the doubled value
            self.assertEqual(result, expected, 
                f"Failed for price={crypto_price}, amount={amount}. "
                f"Expected {expected}, but got {result}")

    def test_zero_amount(self):
        # Test with zero amount
        result = calculate_price(50000, 0)
        self.assertEqual(result, 0, "Zero amount should return 0")

    def test_negative_values(self):
        # Test should handle negative values
        with self.assertRaises(ValueError):
            calculate_price(-5000, 1)
        with self.assertRaises(ValueError):
            calculate_price(5000, -1)

if __name__ == '__main__':
    unittest.main() 