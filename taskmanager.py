
"""created the dummy email for testing purpose"""

dummy_email = "testcli@gmail.com"
dummy_password = "Mnk@assgn"

"""create a class name Task"""
class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed
        
    """convert the task object to json object"""
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

    """class method to create task instance """
    @classmethod
    def from_dict(cls, data):
        return cls(id=data["id"], title=data["title"], completed=data["completed"])

"""create task management function"""

import json
import os

tasks = []
next_id = 1

"""check the credentials"""

def login():
    print("Log in to access the Task Manager by providing credentials")
    print("email:testcli@gmail.com")
    print("password:Mnk@assgn")
    
    email = input("Email: ")
    password = input("Password: ")
    
    if email == dummy_email and password == dummy_password :
        print("Login succesfull.\n")
        return True
    else:
        print("Invalid email or password. Please try again.\n")
        return False

"""add the created task into tasks list"""

def add_task(title):
    global next_id
    task = Task(id=next_id, title=title)
    tasks.append(task)
    next_id += 1
    print(f"Task '{title}' added with ID {task.id}.")

"""display the created tasks along with its status"""

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "Completed" if task.completed else "Not Completed"
        print(f"ID: {task.id}, Title: {task.title}, Status: {status}")
        
"""delete the task using its id number"""

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    print(f"Task with ID {task_id} deleted.")

"""change the status of completed task"""

def mark_task_completed(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Task with ID {task_id} marked as completed.")
            return
    print(f"Task with ID {task_id} not found.")

"""create JSON file handling functions"""

"""add the tsak into JSON file"""

def save_tasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump([task.to_dict() for task in tasks], file)
    print("Tasks saved to file.")


"""retireve the tak information from JSON file"""

def load_tasks(filename="tasks.json"):
    global tasks, next_id
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks_data = json.load(file)
            tasks = [Task.from_dict(task) for task in tasks_data]
            next_id = max([task.id for task in tasks], default=0) + 1
    print("Tasks loaded from file.")

"""create command line interface"""

"""create the loop to take input and provide appropriate response"""

def main():
    if not login():
        return
    load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. Add_Task")
        print("2. View_Task")
        print("3. Delete_Task")
        print("4. Mark_as Complete")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == "5":
            save_tasks()
            print("See you again!!!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


