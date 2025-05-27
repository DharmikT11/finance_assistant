# agents/api_agent.py

from nsetools import Nse
import datetime

class APIAgent:
    def __init__(self):
        self.nse = Nse()
        self.tech_stocks = ["TCS", "INFY", "WIPRO", "HCLTECH"]

    def get_stock_data(self):
        stock_data = {}
        for symbol in self.tech_stocks:
            try:
                quote = self.nse.get_quote(symbol)
                price = quote['lastPrice']
                previous_close = quote['previousClose']
                change_percent = ((price - previous_close) / previous_close) * 100
                stock_data[symbol] = {
                    'price': price,
                    'previous_close': previous_close,
                    'change_%': round(change_percent, 2)
                }
            except Exception as e:
                stock_data[symbol] = {'error': str(e)}
        return stock_data

    def get_portfolio_exposure(self):
        # Dummy example for now
        return {
            "India_Tech": {
                "current_allocation": "25%",
                "previous_allocation": "21%"
            }
        }

# Test
if __name__ == "__main__":
    agent = APIAgent()
    print("📈 Indian Stock Data:", agent.get_stock_data())
    print("💼 Portfolio Exposure:", agent.get_portfolio_exposure())
