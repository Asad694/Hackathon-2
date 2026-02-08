"""
Todo CLI Application - Phase I
An in-memory command-line todo application
"""

from __future__ import annotations
from typing import List, Optional


class Task:
    """Represents a single todo task"""

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"Task({self.id}, '{self.title}', '{self.description}', {status})"


class TodoApp:
    """Main todo application with in-memory storage"""

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task to the todo list"""
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        task = Task(id=self.next_id, title=title.strip(), description=description.strip())
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks in the todo list"""
        return self.tasks.copy()

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        """Update an existing task's title and/or description"""
        task = self._find_task(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip()

        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task from the todo list"""
        task = self._find_task(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        self.tasks.remove(task)
        return True

    def toggle_completion(self, task_id: int) -> Task:
        """Toggle the completion status of a task"""
        task = self._find_task(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        task.completed = not task.completed
        return task

    def _find_task(self, task_id: int) -> Optional[Task]:
        """Find a task by ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None


def display_menu() -> None:
    """Display the main menu options"""
    print("\n=== Todo CLI Application ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Toggle Task Completion")
    print("6. Exit")
    print("==========================")


def get_user_choice() -> str:
    """Get user input for menu choice"""
    return input("Enter your choice (1-6): ").strip()


def get_task_title() -> str:
    """Prompt user for task title"""
    while True:
        title = input("Enter task title: ").strip()
        if title:
            return title
        print("Error: Task title cannot be empty!")


def get_task_description() -> str:
    """Prompt user for optional task description"""
    description = input("Enter task description (optional): ").strip()
    return description


def get_task_id(prompt: str = "Enter task ID: ") -> int:
    """Prompt user for task ID with validation"""
    while True:
        try:
            task_id = int(input(prompt).strip())
            return task_id
        except ValueError:
            print("Error: Please enter a valid number!")


def display_tasks(tasks: List[Task]) -> None:
    """Display tasks in a formatted table"""
    if not tasks:
        print("No tasks found!")
        return

    print("\nID  |   Status  |     Title     |    Description ")
    print("-" * 50)
    for task in tasks:
        status = " Done  " if task.completed else "Not Yet"
        print(f"{task.id:2}  |  {status}  |   {task.title}   |  {task.description}")


def main() -> None:
    """Main application entry point"""
    app = TodoApp()

    print("Welcome to Todo CLI Application!")

    while True:
        display_menu()
        choice = get_user_choice()

        try:
            if choice == "1":
                title = get_task_title()
                description = get_task_description()
                task = app.add_task(title, description)
                print(f"Task added: {task}")

            elif choice == "2":
                tasks = app.get_all_tasks()
                display_tasks(tasks)

            elif choice == "3":
                task_id = get_task_id()
                new_title = input("Enter new title (press Enter to keep current): ").strip()
                new_description = input("Enter new description (press Enter to keep current): ").strip()

                title = new_title if new_title else None
                description = new_description if new_description else None

                if title is None and description is None:
                    print("No changes made!")
                    continue

                task = app.update_task(task_id, title, description)
                print(f"Task updated: {task}")

            elif choice == "4":
                task_id = get_task_id()
                app.delete_task(task_id)
                print(f"Task {task_id} deleted!")

            elif choice == "5":
                task_id = get_task_id()
                task = app.toggle_completion(task_id)
                status = "completed" if task.completed else "incomplete"
                print(f"Task {task_id} marked as {status}")

            elif choice.lower() == "exit" or choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please enter 1-6 or 'exit'.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()