"""
Emmelia Gardner
Class: CS 521 - Spring 1
Date: 3/1/2025
Final Project: Task Manager and Productivity Tracker
Task Manager Class: Manage a list of tasks, including adding, removing, marking complete, and saving/loading tasks
"""
from task import Task

class TaskManager:
    # Manage a list of tasks, including adding, removing, marking complete, and saving/loading tasks

    def __init__(self):
        # Initialize empty list
        self.tasks = []

    def add_task(self, title, category, priority, due_date):
        # Add a new task to the task list
        self.tasks.append(Task(title, category, priority, due_date))

    def remove_task(self, title):
        # Remove a task by title (case-insensitive)
        self.tasks = [task for task in self.tasks if task._title.lower() != title.lower()]
        print(f"Task '{title}' deleted!")

    def mark_task_completed(self, title):
        # Mark a task as completed (case-insensitive)
        for task in self.tasks:
            if task._title.lower() == title.lower():
                task.mark_completed()
                print(f"Task '{title}' marked as completed! ✔")
                return
        print(f"Task '{title}' not found.")

    def list_tasks(self, category=None, show_completed=True):
        # Display tasks, with an option to filter by category and hide completed tasks
        filtered_tasks = self.tasks if category is None else [task for task in self.tasks if task._category.lower() == category.lower()]
        if not show_completed:
            filtered_tasks = [task for task in filtered_tasks if not task._completed]

        if not filtered_tasks:
            print(f"No tasks found in category: {category.capitalize()}" if category else "No tasks found.")
            return

        print("\nTask List:")
        for task in sorted(filtered_tasks, key=lambda x: x._due_date):
            print(task)

    def save_tasks(self, filename="tasks.txt"):
        # Save tasks to text file
        try:
            with open(filename, "w") as file:
                for task in self.tasks:
                    file.write(f"{task._title},{task._category},{task._priority},{task._due_date.strftime('%Y-%m-%d')},{task._completed}\n")
            print("Tasks saved successfully!")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self, filename="tasks.txt"):
        # Load tasks from text file
        try:
            with open(filename, "r") as file:
                self.tasks = []
                for line in file:
                    title, category, priority, due_date, completed = line.strip().split(",")
                    task = Task(title, category, priority, due_date)
                    if completed == "True":
                        task.mark_completed()
                    self.tasks.append(task)
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("No saved tasks found. Starting fresh.")
        except Exception as e:
            print(f"Error reading tasks file: {e}")
