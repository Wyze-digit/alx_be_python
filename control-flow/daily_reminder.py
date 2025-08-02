# This script will ask the user for a single task, its priority level, and if it is 
# time-sensitive. The program will then provide a customized reminder for that task, 
# demonstrating control flow and loops without relying on data structures to store 
# multiple tasks.

# Get task input from user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes or no): ").lower()

# Initialize base reminder message
reminder = f"Task: {task}\nPriority: {priority.capitalize()}\nReminder: '{task}' "

# Match-case for priority level
match priority:
    case "high":
        if time_bound == "yes":
            reminder += "is a high priority task that requires immediate attention today!"
        elif time_bound == "no":
            reminder += "is a high priority task that requires attention before end of today!"
        else:
            reminder += "has unclear time-bound status."

    case "medium":
        if time_bound == "yes":
            reminder += "is medium priority schedule for tomorrow earliest"
        elif time_bound == "no":
            reminder += "is medium priority, relax. Get help later tomorrow"
        else:
            reminder += "has unclear time-bound status."

    case "low":
        if time_bound == "yes":
            reminder += "is a low priority task. Consider to remind your friend to help tomorrow"
        elif time_bound == "no":
            reminder += "is a low priority task. Consider completing it when you have free time."
        else:
            reminder += "has unclear time-bound status."

#    case _:
#        reminder = f"Task: {task}\nPriority: Unknown\nStatus: Task priority is unrecognized. Please enter high, medium, or low."

# Output the final structured reminder
print("")
print(reminder)
