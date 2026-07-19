tasks = []

def add(tasks_list, task_name, priority, done):
    tasks_list.append({"task": task_name, "Priority": priority, "done": done})
    print(f"{task_name} added successfully")

def complete(tasks_list, task_name):
    for task in tasks_list:
        if task["task"] == task_name:
            task["done"] = True
            print(f"{task_name} completed successfully")
            return
    print(f"{task_name} not found")

def delete(tasks_list, task_name):
    for index, task in enumerate(tasks_list):
        if task["task"] == task_name:
            tasks_list.pop(index)
            print(f"{task_name} deleted")
            return
    print(f"{task_name} not found")

def display(tasks_list):
    sorted_tasks = sorted(tasks_list, key=lambda item: item["Priority"])
    print("Tasks sorted by priority")
    for item in sorted_tasks:
        print(f"{item['task']}: {item['Priority']} priority - done: {item['done']}")

while True:
    print("1. Add task")
    print("2. Complete task")
    print("3. Delete task")
    print("4. Display all tasks")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Enter a task: ")
        priority = input("Priority (High/Low): ")
        done = input("Is task done or not yet: ")
        add(tasks, task, priority, done)
    elif choice == 2:
        task = input("Enter the task you completed: ")
        complete(tasks, task)
    elif choice == 3:
        task = input("Enter task to be deleted: ")
        delete(tasks, task)
    elif choice == 4:
        display(tasks)
    elif choice == 5:
        print("EXIT.")
        break
    else:
        print("Invalid input")