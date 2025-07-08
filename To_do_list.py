import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.tasks = []

        # Entry for adding tasks
        self.task_entry = tk.Entry(root, width=30, font=('Arial', 14))
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, width=20, bg="lightblue")
        self.add_button.pack()

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE, font=('Arial', 12))
        self.task_listbox.pack(pady=10)

        # Buttons for Mark Done and Delete
        self.done_button = tk.Button(root, text="Mark as Done", command=self.mark_done, width=20, bg="lightgreen")
        self.done_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, width=20, bg="tomato")
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({'task': task, 'done': False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]['done'] = True
            self.update_listbox()
        else:
            messagebox.showinfo("Selection Error", "No task selected.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showinfo("Selection Error", "No task selected.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✔️" if task['done'] else "❌"
            self.task_listbox.insert(tk.END, f"{status} {task['task']}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
