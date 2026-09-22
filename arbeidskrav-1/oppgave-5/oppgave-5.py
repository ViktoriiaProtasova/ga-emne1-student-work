# Oppgave 5 – Miniprosjekt: aktivitetsplanlegger

from datetime import datetime

activities = []


class Activity:
    def __init__(self, title, category, date, estimated_minutes, status="planned"):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    def show_activity(self):
        print(f"Activity: {self.title:<10} {self.category:<8}  {self.date}  {self.estimated_minutes}  {self.status}")

    def save_activity(self):
        return f"{self.title}|{self.category}|{self.date}|{self.estimated_minutes}|{self.status}"

    def complete_activity(self):
        self.status = "completed"
        print(f"Activity's {self.title} {self.status}")


def get_date():
    is_date_valid = False

    while not is_date_valid:
        try:
            date = datetime.strptime(input("Enter date (dd.mm.yyyy): "), "%d.%m.%Y")
            is_date_valid = True

            return date

        except ValueError:
            print("Invalid date. Please try again.")

    return None


def get_duration():
    is_duration_valid = False

    while not is_duration_valid:
        try:
            duration = int(input("Enter duration in minutes: "))

            if duration <= 0:
                print("Invalid duration. Please try again.")
            else:
                is_duration_valid = True

                return duration

        except ValueError:
            print("Invalid duration. Please try again.")

    return None


def register_activity():
    while True:
        title = input("Enter activity title: ").strip()

        if not title:
            print("Invalid title. Please try again.")
        else:
            break
    while True:
        category = input("Enter activity category: ").strip()

        if not category:
            print("Invalid category. Please try again.")
        else:
            break

    date = get_date().strftime("%d.%m.%Y")
    estimated_minutes = get_duration()
    activity = Activity(title, category, date, estimated_minutes)

    return activity


while True:
    print("=== Activities Planner ===\n"
          "1. Register and show activities\n"
          "2. Search activities\n"
          "3. Filter activities\n"
          "4. Sort activities\n"
          "5. Mark activity as completed\n"
          "6. Show statistics\n"
          "7. File management\n"
          "8. Exit")

    option = input("Choose an option (1-8): ").strip()

    if option == "8":
        print("____")
        print("Goodbye!")
        break

    elif option == "1":
        while True:
            print("____")
            print("1. Register activity\n"
                  "2. Show all activities\n"
                  "3. Back")
            option = input("Choose an option (1-3): ").strip()
            if option == "3":
                break

            elif option == "1":
                new_activity = register_activity()
                activities.append(new_activity)
                print("Activity successfully registered!")
                new_activity.show_activity()

            elif option == "2":
                if activities:
                    for activity in activities:
                        activity.show_activity()
                else:
                    print("No activities yet.\n")
            else:
                print("Invalid option. Try again.\n")

    elif option == "2":
        while True:
            print("____")
            print("1. Search by title\n"
                  "2. Search by category\n"
                  "3. Back")
            option = input("Choose an option (1-3): ").strip()
            if option == "3":
                break

            elif option == "1":
                while True:
                    title = input("Enter title for search: ").strip()
                    if title:
                        break
                    else:
                        print("Invalid title. Try again.\n")
                if activities:
                    found = False

                    for activity in activities:
                        if title.lower() in activity.title.lower():
                            print(f"== Title '{title}' found in the activity ==")
                            activity.show_activity()
                            found = True
                    if not found:
                        print("No activities found.")
                else:
                    print("No activities yet.\n")

            elif option == "2":
                while True:
                    category = input("Enter category for search: ").strip()

                    if category:
                        break
                    else:
                        print("Invalid category. Try again.\n")
                if activities:
                    found = False

                    for activity in activities:
                        if category.lower() in activity.category.lower():
                            print(f"== Category '{category}' found in the activity ==")
                            activity.show_activity()
                            found = True
                    if not found:
                        print("No activities found.")
                else:
                    print("No activities yet.\n")
            else:
                print("Invalid option. Try again.\n")


    elif option == "3":
        while True:
            print("____")
            print("1. Show planned activities\n"
                  "2. Show completed activities\n"
                  "3. Back")
            option = input("Choose an option (1-3): ").strip()
            if option == "3":
                break

            elif option == "1":
                if activities:
                    found = False
                    print("== Planned activities ==")

                    for activity in activities:
                        if activity.status == "planned":
                            activity.show_activity()
                            found = True
                    if not found:
                        print("No activities found.")
                else:
                    print("No activities yet.\n")

            elif option == "2":
                if activities:
                    found = False
                    print("== Completed activities ==")
                    for activity in activities:
                        if activity.status == "completed":
                            activity.show_activity()
                            found = True
                    if not found:
                        print("No activities found.")
                else:
                    print("No activities yet.\n")
            else:
                print("Invalid option. Try again.\n")

    elif option == "4":
        while True:
            print("____")
            print("1. Sort by date\n"
                  "2. Sort by duration\n"
                  "3. Back")
            option = input("Choose an option (1-3): ").strip()
            if option == "3":
                break

            elif option == "1":
                if activities:
                    sorted_activities = sorted(activities,
                                               key=lambda activity: datetime.strptime(activity.date, "%d.%m.%Y"),
                                               reverse=True)
                    print("== Activities sorted by date  ==")

                    for activity in sorted_activities:
                        activity.show_activity()
                else:
                    print("No activities yet.\n")

            elif option == "2":
                if activities:
                    sorted_activities = sorted(activities, key=lambda activity: activity.estimated_minutes,
                                               reverse=True)
                    print("== Activities sorted by duration  ==")

                    for activity in sorted_activities:
                        activity.show_activity()
                else:
                    print("No activities yet.\n")

            else:
                print("Invalid option. Try again.\n")

    elif option == "5":
        if activities:
            for number, activity in enumerate(activities, start=1):
                print(f"{number}.", end=" ")
                activity.show_activity()
            while True:
                found = False
                try:
                    activity_number = int(input("Enter activity's number: "))
                    for number, activity in enumerate(activities, start=1):
                        if activity_number == number:
                            activity.complete_activity()
                            found = True
                except ValueError:
                    print("Invalid number. Try again.\n")
                    continue

                if not found:
                    print("Invalid activity number. Try again.")
                else:
                    break
        else:
            print("No activities yet.\n")


    elif option == "6":
        print(f"Number of activities: {len(activities)}")
        total_minutes = 0
        completed_count = 0

        for activity in activities:
            total_minutes += activity.estimated_minutes

            if activity.status == "completed":
                completed_count += 1
        print(f"Total estimated time: {total_minutes} minutes")
        print(f"Completed activities: {completed_count}")

    elif option == "7":
        while True:
            print("____")
            print("1. Save activities\n"
                  "2. Load activities\n"
                  "3. Back")
            option = input("Choose an option (1-3): ").strip()

            if option == "3":
                break

            elif option == "1":
                with open("activities.txt", "w", encoding="utf-8") as file:

                    for activity in activities:
                        file.write(f"{activity.save_activity()}\n")
                print("Activities saved successfully.")

            elif option == "2":
                try:
                    with open("activities.txt", "r", encoding="utf-8") as file:
                        activities.clear()

                        for line in file:
                            line = line.strip()
                            data = line.split("|")

                            if len(data) != 5:
                                print("Invalid data format. Skipping line.")
                                continue

                            title, category, date, estimated_minutes, status = data

                            try:
                                estimated_minutes = int(estimated_minutes)
                            except ValueError:
                                print("Invalid data. Minutes is not an integer")
                                continue

                            if status not in ("planned", "completed"):
                                print("Invalid data. Status is not valid.")
                                continue

                            activity = Activity(
                                title,
                                category,
                                date,
                                estimated_minutes,
                                status
                            )

                            activities.append(activity)

                        print("Activities loaded successfully.\n")

                except FileNotFoundError:
                    print("No saved activities found. Starting with an empty list.\n")
