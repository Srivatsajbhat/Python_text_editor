import tkinter as tk
from tkinter import filedialog, messagebox, Menu

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")

        self.setup_gui()

        self.current_file = None

    def setup_gui(self):
        self.text_widget = tk.Text(self.root, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill=tk.BOTH)

        self.setup_menu()
        self.setup_toolbar()

    def setup_menu(self):
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)

        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)

    def setup_toolbar(self):
        self.toolbar = tk.Frame(self.root)
        self.toolbar.pack(fill=tk.X)

        self.cut_button = tk.Button(self.toolbar, text="Cut", command=self.cut_text)
        self.cut_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.copy_button = tk.Button(self.toolbar, text="Copy", command=self.copy_text)
        self.copy_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.paste_button = tk.Button(self.toolbar, text="Paste", command=self.paste_text)
        self.paste_button.pack(side=tk.LEFT, padx=5, pady=5)

    def new_file(self):
        self.text_widget.delete("1.0", tk.END)
        self.current_file = None

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.current_file = file_path
            with open(file_path, "r") as file:
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert(tk.END, file.read())

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_widget.get("1.0", tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.current_file = file_path
            with open(file_path, "w") as file:
                file.write(self.text_widget.get("1.0", tk.END))

    def cut_text(self):
        self.text_widget.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_widget.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_widget.event_generate("<<Paste>>")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
