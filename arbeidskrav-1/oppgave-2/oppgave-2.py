study_sessions = [
    {"topic": "Python loops",         "duration_minutes": 45,  "status": "completed"},
    {"topic": "Norwegian grammar",    "duration_minutes": 60,  "status": "completed"},
    {"topic": "Databases",            "duration_minutes": 90,  "status": "planned"},
    {"topic": "HTML and CSS",         "duration_minutes": 30,  "status": "completed"},
    {"topic": "English reading",      "duration_minutes": 120, "status": "planned"},
]

while True:
    print("=== Study Session Planner ===\n"
          "1. Add study session\n"
          "2. Show all sessions\n"
          "3. Show completed sessions\n"
          "4. Search word in topic\n"
          "5. Sort by duration\n"
          "6. Show total and average duration\n"
          "7. Exit")

    option = input("Choose an option (1-7): ")
    print("___\n")

    if option == "7":
        print("___\n")
        print("Goodbye!")
        break

    elif option == "1":

        while True:
            topic = input("Enter topic: ").strip()
            if topic == "":
                print("___\n")
                print("Invalid topic. Try again.")
            else:
                break

        is_duration_valid = False

        while not is_duration_valid:
            try:
                duration_minutes = int(input("Enter duration in minutes: "))
                if duration_minutes <= 0:
                    print("Invalid duration. Please try again.")
                else:
                    is_duration_valid = True
            except ValueError:
                print("___\n")
                print("Invalid duration. Try again.")

        while True:
            status = input("Enter status (planned/completed): ").strip().lower()
            if status not in ("planned", "completed"):
                print("___\n")
                print("Invalid status. Try again.")
            else:
                break

        print("___\n")
        new_session = {
            "topic": topic,
            "duration_minutes": duration_minutes,
            "status": status
        }

        study_sessions.append(new_session)

        print("== The new session ==")
        print(f"Topic: {new_session['topic']}")
        print(f"Duration: {new_session['duration_minutes']} minutes")
        print(f"Status: {new_session['status']}\n")


    elif option == "2":
        print("== All study sessions ==")

        for session in study_sessions:
            print(f"Topic: {session['topic']}")
            print(f"Duration: {session['duration_minutes']} minutes")
            print(f"Status: {session['status']}\n")

    elif option == "3":
        print("== Completed study sessions ==")

        for session in study_sessions:
            if session['status'] == "completed":
                print(f"Topic: {session['topic']}")
                print(f"Duration: {session['duration_minutes']} minutes")
                print(f"Status: {session['status']}\n")

    elif option == "4":
        search_word = input("Enter a word to search: ").strip()

        found_sessions = []

        for session in study_sessions:
            if search_word.lower() in session['topic'].lower():
                found_sessions.append(session)

        if not found_sessions:
            print("___\n")
            print(f"Word '{search_word}' not found.")
        else:
            print("___\n")
            print(f"== Word '{search_word}' found in the topic ==")

            for session in found_sessions:
                print(f"Topic: {session['topic']}")
                print(f"Duration: {session['duration_minutes']} minutes")
                print(f"Status: {session['status']}\n")

    elif option == "5":
        sorted_session = sorted(study_sessions, key=lambda session: session["duration_minutes"], reverse=True)
        print("== Study sessions sorted by duration  ==")

        for session in sorted_session:
            print(f"Topic: {session['topic']}")
            print(f"Duration: {session['duration_minutes']} minutes")
            print(f"Status: {session['status']}\n")

    elif option == "6":
        if not study_sessions:
            print("No sessions yet.\n")
        else:
            total = 0
            count = 0

            for session in study_sessions:
                if session['status'] == "completed":
                    total += session["duration_minutes"]
                    count += 1

            if count > 0:
                print("== Total and average duration for completed sessions ==")
                print(f"Total: {total} minutes")
                print(f"Average: {total / count:.1f} minutes\n")
            else:
                print("No completed sessions yet.\n")

    else:
        print("Invalid option. Try again.\n")

















