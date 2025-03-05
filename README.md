# Task Manager and Productivity Tracker
## 1.	OVERVIEW
The Task Manager and Productivity Tracker is a Python-based tool designed to help users organize and manage their daily tasks more efficiently. With this program, users can add, update, and delete tasks, set priority levels, categorize them, and track their progress. Its filtering feature makes it easier to sort tasks by category, which is useful for managing responsibilities across work, school, and personal life. To ensure that tasks are saved and accessible across multiple sessions, all task data is stored in a text file (tasks.txt) and automatically reloaded when the program starts.
This project was developed using object-oriented programming, file-handling, loops, conditionals, and unit testing, meeting all CS-521 final project requirements while also functioning as a practical and real-world task management solution. By simplifying task organization and improving productivity, this program provides users with a simply yet highly effective way to stay on top of their commitments.
## 2.	FUNCTIONALITY AND FEATURES
The Task Manager and Productivity Tracker includes several key features to help users stay on top of their tasks. Users can create and organize tasks by assigning a title, category, priority level, and due date. The program also supports task completion and filtering, allowing users to mark tasks as finished and sort them by category.
To ensure data persistence, all task information is stored in tasks.txt and automatically reloaded each time the program starts, preventing data loss. The program features an interactive command-line interface with a menu system that simplifies navigation and task management. Additionally, tasks are sorted and prioritized based on due dates and priority levels, helping users focus on what needs attention first.
## 3.	REQUIREMENTS
This project fully meets the CS-521 final project requirements:
•	Data Structures: It incorporates a list (for task storage), a tuple (for priority levels), a set (for unique categories), and a dictionary (for file storage representation).
•	Iteration and Conditionals: The program uses for-loops (for listing tasks), while-loops (for menu navigation), and if statements for decision-making.
•	Error Handling: A try-except-else block is implemented to handle errors in file operations, preventing crashes due to missing or corrupted files.
•	User-Defined Functions: The function mark_task_completed(title) updates the completion status of a specific task based on user input.
•	File Handling: The program stores and retrieves tasks from tasks.txt, ensuring that tasks persist even after the program is closed.
•	Object-Oriented Programming (OOP): The Task class includes private and public attributes, a __str__() method for readable output, and a magic method (__lt__()) to sort tasks by due date.
•	Unit Testing: The program includes five unit tests (instead of the required two) to validate key functionalities such as task addition, deletion, completion, saving, and loading.
This project is built only using Python’s standard library modules, meaning no additional installations are needed.
## 4.	CONCLUSION
The Task Manager and Productivity Tracker is a fully functional and practical Python application that enhances productivity by providing an efficient way to track and organize daily tasks. This project successfully demonstrates object-oriented programming, iteration, conditions, file-handling, and unit testing, meeting all CS-521 final project requirements. As a real-world applicable tool, it shows my Python programming skills, making it a valuable addition to my portfolio. 
