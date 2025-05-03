class ToDoList:
    def __init__(self):
        """Initialize an empty to-do list."""
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        print(f"✅ Added: {task}")

    def update_task(self, task_index, new_task):
        """Update an existing task."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["task"] = new_task
            print(f"✏️ Updated task {task_index+1}: {new_task}")
        else:
            print("❌ Invalid task number.")

    def mark_completed(self, task_index):
        """Mark a task as completed."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"✔️ Task {task_index+1} marked as completed!")
        else:
            print("❌ Invalid task number.")

    def show_tasks(self):
        """Display the current tasks."""
        if not self.tasks:
            print("📭 No tasks found! Start adding some.")
        else:
            print("\n📋 Your To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                status = "✅ Completed" if task["completed"] else "❌ Pending"
                print(f"{i}. {task['task']} - {status}")

def main():
    todo = ToDoList()

    while True:
        print("\n🌟 To-Do List Menu 🌟")
        print("1️⃣ Show Tasks")
        print("2️⃣ Add Task")
        print("3️⃣ Update Task")
        print("4️⃣ Mark Task as Completed")
        print("5️⃣ Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo.show_tasks()
        elif choice == "2":
            task = input("📝 Enter new task: ")
            todo.add_task(task)
        elif choice == "3":
            todo.show_tasks()
            task_index = int(input("🔄 Enter task number to update: ")) - 1
            new_task = input("📝 Enter updated task description: ")
            todo.update_task(task_index, new_task)
        elif choice == "4":
            todo.show_tasks()
            task_index = int(input("✅ Enter task number to mark as completed: ")) - 1
            todo.mark_completed(task_index)
        elif choice == "5":
            print("👋 Goodbye! Stay productive!")
            break
        else:
            print("⚠️ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
