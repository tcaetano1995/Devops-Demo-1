import pytest
import random
from API.main import calculate_price

class TestCryptoCalculator:
    @pytest.fixture
    def test_cases(self):
        return [(0, 100)] + [
            (random.uniform(1000, 100000), random.uniform(0.1, 10))
            for _ in range(5)
        ]

    def test_calculate_price(self, test_cases):
        """Test basic price calculation"""
        for crypto_price, amount in test_cases:
            expected = crypto_price * amount
            result = calculate_price(crypto_price, amount)
            
            assert result == expected, (
                f"\n{'='*50}\n"
                f"💰 Price Calculation Test Failed!\n"
                f"📈 Input Price:     ${crypto_price:,.2f}\n"
                f"📊 Input Amount:    {amount:,.4f}\n"
                f"✨ Expected Result: ${expected:,.2f}\n"
                f"❌ Actual Result:   ${result:,.2f}\n"
                f"❗ Hint: The calculation should be a simple multiplication\n"
                f"{'='*50}"
            )

    def test_zero_amount(self):
        """Test calculation with zero amount"""
        result = calculate_price(0, 100)
        assert result == 0, "Zero amount should return 0"


    def test_negative_values(self):
        """Test handling of negative values"""
        with pytest.raises(ValueError, match="must be non-negative"):
            calculate_price(-5000, 1)
        with pytest.raises(ValueError, match="must be non-negative"):
            calculate_price(5000, -1) 