import csv
import os

tasks = []

FILE_NAME = "tasks.csv"

def load_tasks():
    #Loading the tasks from csv file to the tasks=[]
    global tasks
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append({
                    "task_name": row['task_name']
                })



def save_tasks():
    #Saving any tasks to the csv file
    with open(FILE_NAME, 'w', newline='') as file:
        fieldnames = ['task_name']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)





def menu():
    print("Task manager")
    print("1. Add a task")
    print("2. View all task")
    print("3. Mark as done")

    input_menu = int(input("Enter tour choise: "))

    if input_menu == 1:
        addTask()
    elif input_menu == 2:
        viewAll()
    elif input_menu == 3:
        markDone()
    else:
        print("Invalid choise!")




def addTask():
    print("Add Task")
    task_name = input("Enter your task: ")
    tasks.append({
        "task_name": task_name,
    })
    save_tasks()   #Save after adding any task
    menu()

def viewAll():
    print("View All Task")
    for i, task in enumerate(tasks):
        print(f"Serial number: {i+1}")
        print(f"Task name: {task['task_name']}")
        print("_______________________________")

    menu()


def markDone():
    print("Mark Task As Done")
    serial_number = int(input("Enter the serial number: "))
    found = False
    for i, task in enumerate(tasks):
        if i+1 == serial_number:
            tasks.remove(task)
            save_tasks()   #Save after removing one
            print("Done!")
            found = True
            break
        if not found:
            print("Serial nunmber not found!")

    menu()


load_tasks()
menu()