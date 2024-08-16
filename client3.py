################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """Calculate the ratio of stock price_a to stock price_b"""
    if price_b == 0:
        return 0  # Handle division by zero
    return price_a / price_b

def main():
    # Example quotes for demonstration purposes
    quote_a = {'stock': 'ABC', 'top_bid': {'price': '115.46'}, 'top_ask': {'price': '116.63'}}
    quote_b = {'stock': 'DEF', 'top_bid': {'price': '115.14'}, 'top_ask': {'price': '116.05'}}

    # Dictionary to store prices
    prices = {}

    # Fetch data points
    stock_a, bid_a, ask_a, price_a = getDataPoint(quote_a)
    stock_b, bid_b, ask_b, price_b = getDataPoint(quote_b)

    # Store prices in the dictionary
    prices[stock_a] = price_a
    prices[stock_b] = price_b

    # Calculate ratio using the prices from the dictionary
    ratio = getRatio(prices[stock_a], prices[stock_b])
    print(f"Quoted {stock_a} at (bid:{bid_a}, ask:{ask_a}, price:{price_a})")
    print(f"Quoted {stock_b} at (bid:{bid_b}, ask:{ask_b}, price:{price_b})")
    print(f"Ratio {ratio}")

if __name__ == "__main__":
    main()


