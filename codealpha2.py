"""
╔══════════════════════════════════════════════════════╗
║      STOCK PORTFOLIO TRACKER — CodeAlpha Internship   ║
║      Task 2 | Python Programming                     ║
╚══════════════════════════════════════════════════════╝
"""

import csv
from datetime import datetime

# ─── Hardcoded stock prices (per share, in USD) ───────
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420,
    "NFLX": 670,
    "META": 480,
}


def display_available_stocks():
    """Show the user which stocks are available to invest in."""
    print("\n  Available stocks:")
    print("  " + "-" * 28)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} ${price}/share")
    print("  " + "-" * 28)


def get_stock_symbol():
    """Prompt for a valid stock symbol, or 'done' to finish."""
    while True:
        symbol = input(
            "\n  Enter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            return None

        if symbol in STOCK_PRICES:
            return symbol

        print(f"  ⚠  '{symbol}' not found. Choose from the list above.")


def get_quantity(symbol):
    """Prompt for a valid positive integer quantity."""
    while True:
        qty_input = input(f"  Enter quantity of {symbol}: ").strip()
        try:
            qty = int(qty_input)
            if qty <= 0:
                print("  ⚠  Quantity must be a positive number.")
                continue
            return qty
        except ValueError:
            print("  ⚠  Please enter a valid whole number.")


def build_portfolio():
    """Collect stock symbols and quantities from the user."""
    portfolio = {}  # symbol -> quantity

    print("\n" + "=" * 50)
    print("      STOCK PORTFOLIO TRACKER — CodeAlpha")
    print("=" * 50)

    display_available_stocks()

    while True:
        symbol = get_stock_symbol()
        if symbol is None:
            break

        qty = get_quantity(symbol)

        # If stock already added, add to existing quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + qty
        print(f"  ✅  Added {qty} share(s) of {symbol}.")

    return portfolio


def calculate_investment(portfolio):
    """
    Calculate per-stock investment value and total.
    Returns a list of rows: [(symbol, qty, price, value), ...] and the grand total.
    """
    rows = []
    total = 0

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = qty * price
        rows.append((symbol, qty, price, value))
        total += value

    return rows, total


def display_summary(rows, total):
    """Print a formatted investment summary table."""
    print("\n" + "=" * 50)
    print("              PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"  {'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("  " + "-" * 36)

    for symbol, qty, price, value in rows:
        print(f"  {symbol:<8}{qty:<8}${price:<9}${value:<9}")

    print("  " + "-" * 36)
    print(f"  TOTAL INVESTMENT: ${total:,.2f}")
    print("=" * 50)


def save_to_txt(rows, total, filename="portfolio_summary.txt"):
    """Save the portfolio summary to a plain text file."""
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 40 + "\n")
        f.write(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
        f.write("-" * 36 + "\n")

        for symbol, qty, price, value in rows:
            f.write(f"{symbol:<8}{qty:<8}${price:<9}${value:<9}\n")

        f.write("-" * 36 + "\n")
        f.write(f"TOTAL INVESTMENT: ${total:,.2f}\n")

    print(f"  📄  Summary saved to '{filename}'")


def save_to_csv(rows, total, filename="portfolio_summary.csv"):
    """Save the portfolio summary to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["Stock", "Quantity", "Price Per Share", "Total Value"])

        for symbol, qty, price, value in rows:
            writer.writerow([symbol, qty, price, value])

        writer.writerow([])
        writer.writerow(["", "", "Total Investment", total])

    print(f"  📄  Summary saved to '{filename}'")


def ask_to_save(rows, total):
    """Ask the user whether and how to save the results."""
    choice = input(
        "\n  Save summary to a file? (txt / csv / no): ").strip().lower()

    if choice == "txt":
        save_to_txt(rows, total)
    elif choice == "csv":
        save_to_csv(rows, total)
    elif choice in ("no", "n", ""):
        print("  Skipped saving.")
    else:
        print("  ⚠  Unrecognized option. Skipped saving.")


def main():
    portfolio = build_portfolio()

    if not portfolio:
        print("\n  No stocks were added. Exiting.")
        return

    rows, total = calculate_investment(portfolio)
    display_summary(rows, total)
    ask_to_save(rows, total)

    print("\n  Thanks for using Stock Portfolio Tracker — CodeAlpha Internship\n")


if __name__ == "__main__":
    main()
