import unittest
from client3 import getDataPoint, getRatio

class TestClientFunctions(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        expected_results = [
            ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]

        for quote, expected in zip(quotes, expected_results):
            self.assertEqual(getDataPoint(quote), expected)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        expected_results = [
            ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]

        for quote, expected in zip(quotes, expected_results):
            self.assertEqual(getDataPoint(quote), expected)

    def test_getRatio(self):
        test_cases = [
            (100, 50, 2.0),
            (100, 0, 0),
            (0, 50, 0),
            (0, 0, 0)
        ]

        for price_a, price_b, expected_ratio in test_cases:
            self.assertEqual(getRatio(price_a, price_b), expected_ratio)

    # Optional: Add more unit tests if needed

if __name__ == '__main__':
    unittest.main()
