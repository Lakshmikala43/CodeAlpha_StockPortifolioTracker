# Stock Portfolio Tracker

# Hardcoded stock prices (you can add more)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 140,
    "MSFT": 320
}

portfolio = {}  # to store user input (stock: quantity)

print("📈 Welcome to the Stock Portfolio Tracker 📊")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not available. Try again.")
        continue
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\n📊 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value = ${total_value}")

# Optionally save to file
save = input("Do you want to save results to a file? (y/n): ").lower()
if save == "y":
    filename = "portfolio.csv"
    with open(filename, "w") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock},{qty},{price},{value}\n")
        f.write(f"Total Investment,,,{total_value}\n")
    print(f"✅ Portfolio saved to {filename}")
