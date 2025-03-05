"""
Emmelia Gardner
Class: CS 521 - Spring 1
Date: 3/1/2025
Final Project: Task Manager and Productivity Tracker
Task Class: Represent a task with title, category, priority, due date, and completion status attributes
"""
from datetime import datetime

class Task:
    # Represent a task with title, category, priority, due date, and completion status attributes

    def __init__(self, title, category, priority, due_date):
        # Initialize task attributes
        self._title = title  # Private attribute
        self._category = category
        self._priority = priority
        self._due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self._completed = False  # Default to not completed

    def mark_completed(self):
        # Mark task as completed
        self._completed = True

    def is_overdue(self):
        # Check if task is overdue
        return not self._completed and datetime.now() > self._due_date

    def __str__(self):
        # Return formatted string representation of task
        status = "Completed ✔" if self._completed else "Pending..."
        overdue = "Overdue!" if self.is_overdue() else ""
        return f"{self._title} - {self._category.capitalize()} | Priority: {self._priority.capitalize()} | Due: {self._due_date.date()} | {status}{overdue}"
