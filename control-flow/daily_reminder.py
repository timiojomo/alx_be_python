task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        reminder = "is a high priority task"
    case "medium":
        reminder = "is a medium priority task"
    case "low":
        reminder = "is a low priority task"

if time == "yes":
    print(f"'{task}' {reminder} hat requires immediate attention today!")
elif time == "no":
    print(f"'{task}' {reminder}. Consider completing it when you have free time.")

