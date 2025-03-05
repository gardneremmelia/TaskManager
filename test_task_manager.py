"""
Emmelia Gardner
Class: CS 521 - Spring 1
Date: 3/1/2025
Final Project: Task Manager and Productivity Tracker
Unit tests for Task Manager
"""
import unittest
import os
from task_manager import TaskManager
from task import Task

class TestTaskManager(unittest.TestCase):
    # Unit tests for TaskManager class

    def setUp(self):
        # Set up new instance before each test
        self.manager = TaskManager()
        self.test_file = "test_tasks.txt" 
        self.manager.save_tasks(self.test_file) 

    def tearDown(self):
        # Remove test file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        # Test adding a new task
        self.manager.add_task("Test Task", "Work", "High", "2025-02-10")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0]._title, "Test Task")

    def test_mark_task_completed(self):
        # Test marking a task as completed
        self.manager.add_task("Test Task", "Work", "High", "2025-02-10")
        self.manager.mark_task_completed("Test Task")
        self.assertTrue(self.manager.tasks[0]._completed)

    def test_remove_task(self):
        # Test removing a task by title
        self.manager.add_task("Test Task", "Work", "High", "2025-02-10")
        self.manager.remove_task("Test Task")
        self.assertEqual(len(self.manager.tasks), 0)

    def test_save_and_load_tasks(self):
        # Test saving and loading tasks from text file
        self.manager.add_task("Test Task", "Work", "High", "2025-02-10")
        self.manager.save_tasks(self.test_file)

        # Create a new TaskManager instance and load from file
        new_manager = TaskManager()
        new_manager.load_tasks(self.test_file)

        self.assertEqual(len(new_manager.tasks), 1)
        self.assertEqual(new_manager.tasks[0]._title, "Test Task")

    def test_list_tasks(self):
        # Test listing tasks with/without filtering
        self.manager.add_task("Task 1", "Work", "High", "2025-02-10")
        self.manager.add_task("Task 2", "Personal", "Medium", "2025-02-12")

        # Check total tasks
        self.assertEqual(len(self.manager.tasks), 2)

        # Check filtering by category
        work_tasks = [task for task in self.manager.tasks if task._category.lower() == "work"]
        self.assertEqual(len(work_tasks), 1)

if __name__ == "__main__":
    unittest.main()
