"""Minimal Tkinter GUI starter for SnC."""
import tkinter as tk
from tkinter import ttk, messagebox


class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=12)
        self.pack(fill="both", expand=True)

        ttk.Label(self, text="Enter text:").grid(row=0, column=0, sticky="w")
        self.entry = ttk.Entry(self, width=40)
        self.entry.grid(row=1, column=0, sticky="ew", pady=4)
        self.entry.bind("<Return>", lambda e: self.add_item())
        ttk.Button(self, text="Add", command=self.add_item).grid(row=1, column=1, padx=(6, 0))

        self.listbox = tk.Listbox(self, height=10)
        self.listbox.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=4)
        ttk.Button(self, text="Remove selected", command=self.remove_item).grid(
            row=3, column=0, columnspan=2, sticky="e")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

    def add_item(self):
        text = self.entry.get().strip()
        if text:
            self.listbox.insert("end", text)
            self.entry.delete(0, "end")

    def remove_item(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("SnC", "Select an item first.")
            return
        self.listbox.delete(sel[0])


def main():
    root = tk.Tk()
    root.title("SnC")
    root.geometry("420x320")
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
