# Create a program that schedules study sessions

from datetime import datetime, timedelta


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


def get_start_time():
    is_time_valid = False

    while not is_time_valid:
        try:
            start_time = datetime.strptime(input("Enter start time (H:M): "), "%H:%M")
            is_time_valid = True
            return start_time

        except ValueError:
            print("Invalid time. Please try again.")
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


def show_the_date(date):
    try:
        date = date.strftime("%d.%m.%Y")
        return date
    except ValueError:
        print("Invalid date. Please try again.")


def show_end_time(start_time, duration):
    end_time = (start_time + timedelta(minutes=duration)).strftime("%H:%M")
    return end_time


def show_difference():
    date_1 = get_date()
    date_2 = get_date()
    difference = abs(date_2 - date_1).days
    date_1 = date_1.strftime("%d.%m.%Y")
    date_2 = date_2.strftime("%d.%m.%Y")
    if difference == 1:
        return f"There are {difference} day between {date_1} and {date_2}."
    else:
        return f"There are {difference} days between {date_1} and {date_2}."


def show_sorted_dates(list_of_dates):
    list_of_dates = sorted(list_of_dates)
    return list_of_dates


def plan_study_session():
    list_of_dates = []
    while True:
        print("=== Study Session Planner ===\n"
              "1. Plan a study session\n"
              "2. Show all sessions in date order\n"
              "3. Count days between two dates\n"
              "4. Exit")
        option = input("Choose an option (1-4): ")
        if option == "4":
            print("Goodbye!")
            break
        elif option == "1":
            date = get_date()
            list_of_dates.append(date)
            time = get_start_time()
            start_time = time.strftime("%H:%M")
            duration = get_duration()
            print(f"Study session planned!\n"
                  f"Date: {show_the_date(date)}\n"
                  f"Time: {start_time} - {show_end_time(time, duration)} ({duration} minutes)")
        elif option == "2":
            if list_of_dates == []:
                print("No study sessions planned yet.")
            else:
                sorted_dates = show_sorted_dates(list_of_dates)
                for date in sorted_dates:
                    sorted_dates = date.strftime("%d.%m.%Y")
                    print(sorted_dates)
        elif option == "3":
            print(show_difference())
        else:
            print("Invalid option. Please try again.")


plan_study_session()
