import pandas as pd

ticker = "DLTR"

df = pd.read_csv("SP500.min.2023Jan.bars.csv")

print("Columns in the file:")
print(df.columns)

ticker_column = "ticker"
datetime_column = "Unnamed: 0"
close_column = "close"

# Keep only rows for Dollar Tree
stock = df[df[ticker_column] == ticker].copy()

# Convert the unnamed column into a real date/time column
stock[datetime_column] = pd.to_datetime(stock[datetime_column])

# Sort from earliest to latest
stock = stock.sort_values(datetime_column)

# Create a date-only column
stock["date"] = stock[datetime_column].dt.date

# For each day, keep the last row of that day
daily_close = stock.groupby("date").tail(1)

# Keep only the date and closing price
daily_close = daily_close[["date", close_column]]

# Save the file directly to your Desktop
daily_close.to_csv("/Users/bobbyfrigon/Desktop/DLTR_close.txt", index=False, header=False)

print(daily_close)
print("Saved DLTR_close.txt to your Desktop")