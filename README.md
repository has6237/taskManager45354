# taskManager45354
Mini Task Manager System with Python File Handling

# 📝 Task Manager (Python CLI)

A simple command-line Task Manager built with Python. This program allows users to add tasks, view all tasks, and mark tasks as completed. All tasks are stored in a CSV file for persistence.

---

## 🚀 Features

* Add new tasks
* View all existing tasks
* Mark tasks as done (removes them from the list)
* Persistent storage using CSV file
* Simple and easy-to-use command-line interface

---

## 🛠️ Technologies Used

* Python
* Built-in modules:

  * `csv` (for file handling)
  * `os` (for file checking)

---

## 📂 Project Structure

```
task-manager/
│
├── tasks.csv        # Stores all tasks
├── main.py          # Main program file
└── README.md        # Project documentation
```


## 💡 How It Works

* When the program starts, it loads tasks from `tasks.csv`.
* Users can choose from a menu:

  * Add a task
  * View all tasks
  * Mark a task as done
* Every change is automatically saved to the CSV file.

---

## 📸 Sample Output

```
Task manager
1. Add a task
2. View all task
3. Mark as done
Enter tour choise: 1
Add Task
Enter your task: I have to send a note at 7pm 

Task manager
1. Add a task
2. View all task
3. Mark as done
Enter tour choise: 1
Add Task
Enter your task: I have to update the system at 10pm

Task manager
1. Add a task
2. View all task
3. Mark as done
Enter tour choise: 2
View All Task
Serial number: 1
Task name: I have to send a note at 7pm
_______________________________
Serial number: 2
Task name: I have to update the system at 10pm
_______________________________

Task manager
1. Add a task
2. View all task
3. Mark as done
Enter tour choise: 1
Add Task
Enter your task: I have to buy ice-cream

Task manager
1. Add a task
2. View all task
3. Mark as done
Enter tour choise: 2
View All Task
Serial number: 1
Task name: I have to send a note at 7pm
_______________________________
Serial number: 2
Task name: I have to update the system at 10pm
_______________________________
Serial number: 3
Task name: I have to buy ice-cream
_______________________________

Task manager
1. Add a task
2. View all task
3. Mark as done
Enter tour choise: 3
Mark Task As Done
Enter the serial number: 1
Done!

Task manager
1. Add a task
2. View all task
3. Mark as done
Enter tour choise: 2
View All Task
Serial number: 1
Task name: I have to update the system at 10pm
_______________________________
Serial number: 2
Task name: I have to buy ice-cream
_______________________________


## 📄 License

This project is open-source and free to use.
