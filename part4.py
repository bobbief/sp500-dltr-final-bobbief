dates = []
prices = []

with open("/Users/bobbyfrigon/Desktop/DLTR_close.txt", "r") as file:
    for line in file:
        line = line.strip()

        if line == "":
            continue

        pieces = line.split(",")

        date = pieces[0]
        price = float(pieces[1])

        dates.append(date)
        prices.append(price)

# Start assuming best buying day is the first day
lowest_price = prices[0]
lowest_price_day = 0

largest_profit = 0
best_buy_day = 0
best_sell_day = 0

# Go day by day and ask:
# "If sold today, what is the profit that could be made?"
for i in range(1, len(prices)):
    possible_profit = prices[i] - lowest_price

    if possible_profit > largest_profit:
        largest_profit = possible_profit
        best_buy_day = lowest_price_day
        best_sell_day = i

    # Update the lowest buying price after checking profit
    if prices[i] < lowest_price:
        lowest_price = prices[i]
        lowest_price_day = i

print("Dollar Tree largest possible profit")
print("Best buying date:", dates[best_buy_day])
print("Buying price:", round(prices[best_buy_day], 4))
print("Best selling date:", dates[best_sell_day])
print("Selling price:", round(prices[best_sell_day], 4))
print("Largest possible profit:", round(largest_profit, 4))
