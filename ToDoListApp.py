# Simple To-Do List Application

todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("\nYour To-Do List is empty!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("\nEnter the new task: ")
    todo_list.append(task)
    print("Task added successfully!")

def update_task():
    view_tasks()
    if not todo_list:
        return
    try:
        task_no = int(input("\nEnter the task number to update: "))
        if 1 <= task_no <= len(todo_list):
            new_task = input("Enter the updated task: ")
            todo_list[task_no - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_tasks()
    if not todo_list:
        return
    try:
        task_no = int(input("\nEnter the task number to delete: "))
        if 1 <= task_no <= len(todo_list):
            deleted_task = todo_list.pop(task_no - 1)
            print(f"Deleted task: {deleted_task}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main Loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1-5.")




          