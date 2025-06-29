import os

# File to store tasks
TODO_FILE = "todo.txt"


# ================== Core File Handling ===================

def load_tasks(file=TODO_FILE):
    """Load tasks from the file."""
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip()]


def save_tasks(tasks, file=TODO_FILE):
    """Save tasks to the file."""
    with open(file, "w") as f:
        for task in tasks:
            f.write(task + "\n")


# ================== Business Logic =======================

def add_task_logic(tasks, task):
    """Add task if it's not empty."""
    task = task.strip()
    if task:
        tasks.append(task)
        return True
    return False


def delete_task_logic(tasks, index):
    """Delete task by index (0-based). Return removed task or None."""
    if 0 <= index < len(tasks):
        return tasks.pop(index)
    return None


def update_task_logic(tasks, index, new_task):
    """Update task at index. Return (old, new) or None."""
    new_task = new_task.strip()
    if 0 <= index < len(tasks) and new_task:
        old = tasks[index]
        tasks[index] = new_task
        return old, new_task
    return None


# ================== CLI Interface ========================

def view_tasks():
    """Display tasks with numbers."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")


def add_task():
    """CLI to add a task."""
    tasks = load_tasks()
    task = input("Enter task to add: ").strip()
    if add_task_logic(tasks, task):
        save_tasks(tasks)
        print(f'Task "{task}" added.')
    else:
        print("Task cannot be empty.")


def delete_task():
    """CLI to delete a task."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks()
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        removed = delete_task_logic(tasks, idx)
        if removed:
            save_tasks(tasks)
            print(f'Task "{removed}" deleted.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def update_task():
    """CLI to update a task."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks to update.")
        return

    view_tasks()
    try:
        idx = int(input("Enter task number to update: ")) - 1
        new_task = input("Enter new task: ").strip()
        result = update_task_logic(tasks, idx, new_task)
        if result:
            old, new = result
            save_tasks(tasks)
            print(f'Task "{old}" updated to "{new}".')
        else:
            print("Invalid task number or empty new task.")
    except ValueError:
        print("Please enter a valid number.")


# ================== Main Loop ============================

def main():
    """Main menu loop."""
    actions = {
        "1": view_tasks,
        "2": add_task,
        "3": delete_task,
        "4": update_task,
        "5": lambda: print("Exiting... Goodbye! 👋")
    }
    menu = (
        "\nTodo List Menu:\n"
        "1. View tasks\n"
        "2. Add task\n"
        "3. Delete task\n"
        "4. Update task\n"
        "5. Exit\n"
    )
    while True:
        print(menu)
        cmd = input("Enter command number: ").strip()
        if cmd == "5":
            actions[cmd]()
            break
        action = actions.get(cmd)
        if action:
            action()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
