from pathlib import Path

data_directory = Path("..") / "data"
price_path = data_directory / "prices.txt"
report_path = data_directory / "price_report.txt"

prices = []

with open(price_path, "r", encoding="utf-8") as file:
    for line in file:
        price = float(line)
        prices.append(price)

count = len(prices)
total = round(sum(prices))
average = round(total / count)

output = [str(count), str(total), str(average)]

with open(report_path, "a", encoding="utf-8") as file:
    file.write("Count: " + output[0] + "\n")
    file.write("Total: " + output[1] + "\n")
    file.write("Average: " + output[2])


