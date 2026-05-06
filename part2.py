import statistics

prices = []

with open("/Users/bobbyfrigon/Desktop/DLTR_close.txt", "r") as file:
    for line in file:
        line = line.strip()

        if line == "":
            continue

        # Each line looks like: date,price
        pieces = line.split(",")

        price = float(pieces[1])
        prices.append(price)

mean_price = statistics.mean(prices)
std_price = statistics.stdev(prices)

print("Dollar Tree daily closing prices")
print("Number of trading days:", len(prices))
print("Mean closing price:", round(mean_price, 4))
print("Standard deviation:", round(std_price, 4))