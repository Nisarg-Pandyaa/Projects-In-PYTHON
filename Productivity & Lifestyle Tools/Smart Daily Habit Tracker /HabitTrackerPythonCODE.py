import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Greet the user
print("🧠 Welcome to your Smart Daily Habit Tracker! 🧠")
username = input("Please enter your name: ").strip()
today = datetime.now().strftime("%A")  # Gets the current day name (e.g., Monday)

# Define the filename based on the user's name
filename = f"{username}_habits.csv"

# Load or create habit list
if not os.path.exists(filename):
    habit_count = int(input("How many habits would you like to track? "))
    habits = []
    for i in range(habit_count):
        habit_name = input(f"Enter the name of habit #{i+1}: ").strip()
        habits.append(habit_name)

    # Create a new CSV file with habit headers
    with open(filename, 'w') as file:
        header = "Day," + ",".join(habits) + "\n"
        file.write(header)
    print("🎉 Habit list created successfully!\n")
else:
    # Read existing habit names from file
    with open(filename, 'r') as file:
        habits = file.readline().strip().split(",")[1:]
    print("📂 Existing habit list loaded.\n")

# Log today's habit status
daily_log = []
for habit in habits:
    response = input(f"Did you complete '{habit}' today? (yes/no): ").strip().lower()
    daily_log.append("1" if response == "yes" else "0")

# Append today's data to the CSV file
with open(filename, 'a') as file:
    file.write(today + "," + ",".join(daily_log) + "\n")

print("✅ Your progress for today has been saved!\n")

# Function to generate and display a weekly report
def generate_report(filepath):
    df = pd.read_csv(filepath)
    
    print("📊 Your Weekly Habit Progress:")
    print(df)

    # Calculate percentage of completion per habit
    percentages = df.iloc[:, 1:].astype(int).sum() / len(df) * 100
    print("\n📈 Completion Rate (in %):")
    print(percentages.round(2))

    # Visual representation using a bar chart
    percentages.plot(kind="bar", color="cornflowerblue", title="Habit Completion Overview")
    plt.ylabel("Completion %")
    plt.tight_layout()
    plt.show()

# Check for duplicate habits
if len(set(habits)) < len(habits):
    print("⚠️ Warning: You have duplicate habits in your list. Please review them next time!")

# Ask user if they want to see the report
show = input("Would you like to view your weekly habit report? (yes/no): ").strip().lower()
if show == "yes":
    generate_report(filename)

