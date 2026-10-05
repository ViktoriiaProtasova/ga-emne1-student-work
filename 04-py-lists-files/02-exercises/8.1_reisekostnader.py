# Oppgave 8.1: Reisekostnader

from pathlib import  Path

prices_path = Path("..") / "data" / "travel_costs.txt"
travel_report_path = Path("..") / "data" / "travel_report.txt"

# with open(prices_path, "r", encoding="utf-8") as file:
#     travel_costs = [float(price) for price in file]

# with open(travel_report_path, "w", encoding="utf-8") as file:
#     file.write(f"Count: {len(travel_costs)}\n")
#     file.write(f"Total: {sum(travel_costs)}\n")
#     file.write(f"Average: {(sum(travel_costs) / len(travel_costs)):.2f}\n")
#     file.write(f"Lowest: {min(travel_costs)}\n")
#     file.write(f"Highest: {max(travel_costs)}\n")

def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        travel_costs = [float(price) for price in file]
        return travel_costs

def write_file(path, data):
    with open(path, "w", encoding="utf-8") as file:
        file.write(f"Count: {len(data)}\n")
        file.write(f"Total: {sum(data)}\n")
        file.write(f"Average: {(sum(data) / len(data)):.2f}\n")
        file.write(f"Lowest: {min(data)}\n")
        file.write(f"Highest: {max(data)}\n")

write_file(travel_report_path, read_file(prices_path))