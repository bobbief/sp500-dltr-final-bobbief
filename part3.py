import matplotlib.pyplot as plt

prices = []

with open("/Users/bobbyfrigon/Desktop/DLTR_close.txt", "r") as file:
    for line in file:
        line = line.strip()

        if line == "":
            continue

        pieces = line.split(",")
        price = float(pieces[1])
        prices.append(price)

# x-axis should be integers 1 to N
days = list(range(1, len(prices) + 1))

plt.plot(days, prices, marker="o")

plt.title("DLTR Closing Price")
plt.xlabel("Trading day in January")
plt.ylabel("Closing price")

plt.xticks(days)

plt.savefig("/Users/bobbyfrigon/Desktop/DLTR_closing_price.png")
plt.show()

print("Saved DLTR_closing_price.png to your Desktop")