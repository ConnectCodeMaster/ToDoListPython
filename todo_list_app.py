import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # Frame for title
        title_frame = tk.Frame(self.root, bg="#f0f0f0")
        title_frame.pack(pady=10)

        self.title_label = tk.Label(title_frame, text="To-Do List", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack()

        # Frame for Listbox and Scrollbar
        listbox_frame = tk.Frame(self.root, bg="#f0f0f0")
        listbox_frame.pack(pady=10)

        self.listbox = tk.Listbox(listbox_frame, width=40, height=15, font=("Arial", 14), bd=0, selectbackground="#a6a6a6")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(listbox_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Frame for Entry and Buttons
        entry_frame = tk.Frame(self.root, bg="#f0f0f0")
        entry_frame.pack(pady=20)

        self.entry = tk.Entry(entry_frame, width=34, font=("Arial", 14), bd=0)
        self.entry.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(entry_frame, text="Add Task", width=10, font=("Arial", 14), bg="#20bebe", fg="#fff", bd=0, command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        self.remove_button = tk.Button(self.button_frame, text="Remove Task", width=15, font=("Arial", 14), bg="#ff6347", fg="#fff", bd=0, command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.mark_button = tk.Button(self.button_frame, text="Mark Completed", width=15, font=("Arial", 14), bg="#32cd32", fg="#fff", bd=0, command=self.mark_completed)
        self.mark_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task = self.listbox.get(selected_task_index)
            if messagebox.askyesno("Confirm Delete", f"Do you want to delete '{task}'?"):
                del self.tasks[selected_task_index[0]]
                self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_completed(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task = self.listbox.get(selected_task_index)
            self.tasks[selected_task_index[0]] = f"{task} (completed)"
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
