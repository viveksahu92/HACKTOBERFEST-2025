# Simple To-Do List Manager
# Medium level program

import os

todo_file = "todo_list.txt"

def show_todos():
    if os.path.exists(todo_file):
        with open(todo_file, "r") as f:
            todos = f.readlines()
            if todos:
                print("\nYour To-Do List:")
                for i, item in enumerate(todos, start=1):
                    print(f"{i}. {item.strip()}")
            else:
                print("\nYour To-Do list is empty.")
    else:
        print("\nNo To-Do list found.")

def add_todo():
    task = input("Enter a task to add: ")
    with open(todo_file, "a") as f:
        f.write(task + "\n")
    print(f"✅ Task '{task}' added!")

def delete_todo():
    show_todos()
    try:
        number = int(input("Enter the task number to delete: "))
        with open(todo_file, "r") as f:
            todos = f.readlines()
        if 1 <= number <= len(todos):
            removed = todos.pop(number-1)
            with open(todo_file, "w") as f:
                f.writelines(todos)
            print(f"🗑️ Task '{removed.strip()}' deleted!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Show To-Do List")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_todos()
        elif choice == "2":
            add_todo()
        elif choice == "3":
            delete_todo()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
