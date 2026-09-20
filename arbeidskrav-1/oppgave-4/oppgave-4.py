# Oppgave 4.1 – Les og kontroller data

import csv

file_name = "supporthenvendelser.csv"

try:
    with open(file_name, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        row_number = 0
        valid_requests = []

        for row in reader:
            row_number += 1
            if not row["id"] or not row["category"] or not row["minutes"] or not row["is_resolved"]:
                print(f"Error on line {row_number}: a field is missing")
                continue

            try:
                id_value = int(row["id"])
                row["id"] = id_value
                if id_value <= 0:
                    print(f"Error on line {row_number}: id is not a positive integer")
                    continue
            except ValueError:
                print(f"Error on line {row_number}: id is not an integer")
                continue

            try:
                minutes_value = int(row["minutes"])
                row["minutes"] = minutes_value
                if minutes_value < 0:
                    print(f"Error on line {row_number}: minutes is not an integer of zero or greater")
                    continue
            except ValueError:
                print(f"Error on line {row_number}: minutes is not an integer")
                continue

            if row["is_resolved"] != 'yes' and row["is_resolved"] != 'no':
                print(f"Error on line {row_number}: is_resolved is not either 'yes' or 'no'")
                continue

            valid_requests.append(row)

except FileNotFoundError:
    print(f"Error: {file_name} was not found")
    quit()

# Oppgave 4.2 – Analyser data

valid_requests_count = len(valid_requests)
print(f"Number of valid requests: {valid_requests_count}")

category_counts = {}

for row in valid_requests:
    category = row["category"]
    category_counts[category] = category_counts.get(category, 0) + 1

for key, value in category_counts.items():
    print(key, value)

total_time = 0

for row in valid_requests:
    total_time += row["minutes"]
print(f"Total time: {total_time} minutes")
print(f"Average time: {total_time / len(valid_requests):.1f} minutes")

resolved_inquiries = 0
unresolved_inquiries = []

for row in valid_requests:
    if row["is_resolved"] == "yes":
        resolved_inquiries += 1
    else:
        unresolved_inquiries.append(row)

print(f"Number of resolved inquiries: {resolved_inquiries}")
print(f"Number of unresolved inquiries: {len(valid_requests) - resolved_inquiries}")

most_inquiries_category = ""

for key, value in category_counts.items():
    if value == max(category_counts.values()):
        print(f"The most inquiries category: {key}")
        most_inquiries_category = key

time_consuming_inquiries = sorted(unresolved_inquiries, key=lambda row: row["minutes"], reverse=True)

for row in time_consuming_inquiries:
    print(f"ID: {row['id']}, Category: {row['category']}, Minutes: {row['minutes']}")

# Oppgave 4.3 – Skriv rapport


with open("support-rapport.txt", "w", encoding="utf-8") as report:
    report.write("   ===Support Report===\n"
                 "\n"
                 f"1. Number of valid requests: {valid_requests_count}\n")
    report.write("2. Category        Count\n")
    report.write("   --------------------\n")

    for category, count in category_counts.items():
        report.write(f"   {category:<15}{count:>5}\n")

    report.write(f"3. Total time: {total_time} minutes\n")
    report.write(f"4. Average time: {total_time / len(valid_requests):.1f} minutes\n")
    report.write(f"5. Number of resolved inquiries: {resolved_inquiries}\n")
    report.write(f"6. Number of unresolved inquiries: {len(valid_requests) - resolved_inquiries}\n")
    report.write(f"7. The most inquiries category: {most_inquiries_category}\n")
    report.write(f"8. Unresolved inquiries sorted by time spent:\n")
    report.write("   --------------------\n")
    for row in time_consuming_inquiries:
        report.write(f"   ID: {row['id']}, Category: {row['category']}, Minutes: {row['minutes']}\n")


# Oppgave 4.4 – Finn og rett feil



def sum_resolved_minutes(requests: list[dict[str, str | int]]) -> int:
    total = 0
    for request in requests:
        if request["is_resolved"] == "yes":
            total += request["minutes"]
    return total

print(sum_resolved_minutes(valid_requests))


