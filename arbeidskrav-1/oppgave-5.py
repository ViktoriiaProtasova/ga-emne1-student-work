# Oppgave 5 – Miniprosjekt: aktivitetsplanlegger

#  activity = {"title": "", "category": "", "date": "", "estimated_minutes": 0, "status": ""}

activities = []

class Activity:
    def __init__(self, title, category, date, estimated_minutes, status):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    def complete_activity(self):
        self.status = "completed"
        print(f"Status: {self.status}")
    #
    # def remove_activity(self, activity):
    #     if activity in self.activities:
    #         self.activities.remove(activity)
    #         print(f"Removed: {activity}")

    def show_activity(self):
        print(f"Activity '{self.title}': {self.category} - {self.date} - {self.estimated_minutes} - {self.status}")


    # def show_activities(self):
    #     print(f"Activities '{self.title}':")
    #     for activity in self.activities:
    #         print(f"- {activity}")
    #
    # def __len__(self):
    #     return len(self)



a = Activity("Cross", "sport", "12.05.2026", 60, "planned")
b = Activity("Cross", "sport", "12.05.2026", 60, "planned")
a.show_activity()

activities.append(a)
activities.append(b)
print(len(activities))
a.complete_activity()
# a.show_activity()
for activity in activities:
    activity.show_activity()