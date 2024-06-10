import tkinter as tk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        master.title("Lista de Tarefas")

        self.task_label = tk.Label(master, text="Tarefa:")
        self.task_label.grid(row=0, column=0, padx=7, pady=15)

        self.task_entry = tk.Entry(master)
        self.task_entry.grid(row=0, column=1, padx=7, pady=15,)

        self.add_button = tk.Button(master, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=7, pady=15 )

        self.tasks_listbox = tk.Listbox(master,)
        self.tasks_listbox.grid(row=1, column=0, columnspan=3, padx=7, pady=15)

        self.delete_button = tk.Button(master, text="Remover Tarefa", command=self.remove_task)
        self.delete_button.grid(row=2, column=1, padx=7, pady=15)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_index)
        except IndexError:
            pass

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
