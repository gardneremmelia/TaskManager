"""
Emmelia Gardner
Class: CS 521 - Spring 1
Date: 3/1/2025
Final Project: Task Manager and Productivity Tracker
Command-line interface for Task Manager
"""
from task_manager import TaskManager

def main():
    # CLI interacting with Task Manager
    manager = TaskManager()
    manager.load_tasks()

    while True:
        print("\n==================================")
        print("      Task Manager Menu")
        print("==================================")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Tasks by Category")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Save & Exit")
        print("==================================")
        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                title = input("Enter Task Title: ").strip()
                category = input("Enter Category (Work, Personal, School, etc.): ").strip()
                priority = input("Enter Priority (High, Medium, Low): ").strip()
                due_date = input("Enter Due Date (YYYY-MM-DD): ").strip()
                manager.add_task(title, category, priority, due_date)
                print(f"Task '{title}' added successfully!")

            case "2":
                show_completed = input("Show completed tasks? (yes/no): ").strip().lower() == "yes"
                manager.list_tasks(show_completed=show_completed)

            case "3":
                category = input("Enter category to filter by (Work, Personal, School, etc.): ").strip()
                show_completed = input("Show completed tasks? (yes/no): ").strip().lower() == "yes"
                manager.list_tasks(category=category, show_completed=show_completed)

            case "4":
                title = input("Enter Task Title to mark as completed: ").strip()
                manager.mark_task_completed(title)

            case "5":
                title = input("Enter Task Title to delete: ").strip()
                manager.remove_task(title)

            case "6":
                manager.save_tasks()
                print("Exiting Task Manager. Goodbye!")
                break

            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()