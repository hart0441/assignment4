def menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f'Task "{task}" added!')

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f'Task "{removed_task}" removed!')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        menu()
        choice = input("Select an option (1-4): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()
