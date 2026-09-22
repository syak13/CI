import unittest
from duckfine import DuckFine

class TestDuckFine(unittest.TestCase):
    def setUp(self):
        self.fine = DuckFine("M001")  # Initialize DuckFine with a member ID

    def test_charge_returns_a_fee_for_a_late_duck(self):
        """Test that a fee is charged for a late duck."""
        self.assertEqual(self.fine.charge(5), 1.50)  # Assuming (5 - 2) * 0.50 = 1.50

    def test_deluxe_duck_costs_more(self):
        """Test that deluxe ducks incur a higher fee."""
        regular_fee = self.fine.charge(5)
        deluxe_fee = self.fine.charge(5, deluxe=True)
        self.assertEqual(deluxe_fee, 3.0)  # Deluxe fee should be double: (5 - 2) * 0.50 * 2

    def test_no_fee_when_returned_on_time(self):
        """Test that no fee is charged when the duck is returned on time."""
        self.assertEqual(self.fine.charge(0), 0.0)

    def test_negative_days_raises(self):
        """Test that negative days late raises a ValueError."""
        with self.assertRaises(ValueError):
            self.fine.charge(-1)

    def test_max_fee_is_enforced(self):
        """Test that the maximum fee is enforced."""
        fee = self.fine.charge(20)  # Assuming max fee is $5.00
        self.assertEqual(fee, 5.0)

if __name__ == "__main__":
    unittest.main()