class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_first_task(self):
        if self.tasks:
            self.tasks.pop(0)

    def remove_last_task(self):
        if self.tasks:
            self.tasks.pop()

    def remove_task_at_position(self, position):
        if 0 <= position < len(self.tasks):
            self.tasks.pop(position)

    def display_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

task_list = TaskList()

while True:
    print("\n1. Add task\n2. Remove first task\n3. Remove last task\n4. Remove task at position\n5. Display tasks\n6. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        task_list.add_task(task)
    elif choice == "2":
        task_list.remove_first_task()
    elif choice == "3":
        task_list.remove_last_task()
    elif choice == "4":
        position = int(input("Enter position: "))
        task_list.remove_task_at_position(position - 1)
    elif choice == "5":
        task_list.display_tasks()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please choose again.")
