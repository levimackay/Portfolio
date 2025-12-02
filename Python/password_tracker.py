"""
Password Tracker - Final Project (CSE 111)
Author: Levi Mackay
Date: July 2025

Yo! This is my final project for Programming with Functions (CSE 111).
It's a super simple password tracker that lets you store website login info
like site names, usernames, and passwords using a clean little GUI. No crazy
security or encryption here (although I do want to learn how to do that)

Here's what it does:
- Saves login info to a plain text file (passwords.txt)
- Also saves it to a Word document (passwords.docx) using the `python-docx` module
- Full GUI built with `tkinter` — no terminal input required
- Lets you view all saved passwords in a scrollable popup
- Includes a simple search tool to find logins by site name

This project was a blast to build. LOL hope it’s as clean and functional as I tried
to make it.
"""

from docx import Document
import tkinter as tk
from tkinter import messagebox, scrolledtext

def create_password_file(filename):
    """Creates a new password text file if it doesn't exist."""
    try:
        with open(filename, "x") as file:
            file.write("Password Tracker\n")
            file.write("================\n\n")
    except FileExistsError:
        pass

def add_password_entry(filename, site, username, password):
    """Adds a new password entry to the file."""
    with open(filename, "a") as file:
        file.write(f"Site: {site}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write("--------------------------\n")

def save_gui_password():
    """Gets input from GUI and saves to the .txt file."""
    site = site_entry.get()
    user = user_entry.get()
    pwd = pass_entry.get()
    if site and user and pwd:
        add_password_entry("passwords.txt", site, user, pwd)
        messagebox.showinfo("Saved", "Password saved to passwords.txt.")
        site_entry.delete(0, tk.END)
        user_entry.delete(0, tk.END)
        pass_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Missing info", "Fill out all fields!")

def view_saved_passwords():
    """Opens a window to display all saved passwords."""
    try:
        with open("passwords.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        content = "No password file found."

    view_window = tk.Toplevel()
    view_window.title("Saved Logins")
    view_window.geometry("400x400")

    text_box = scrolledtext.ScrolledText(view_window, wrap=tk.WORD, font=("Arial", 10))
    text_box.pack(expand=True, fill="both")
    text_box.insert(tk.END, content)
    text_box.config(state="disabled")

def search_passwords():
    """Lets the user search for saved logins by site name."""
    def do_search():
        keyword = search_entry.get().lower()
        results = ""

        try:
            with open("passwords.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if keyword in lines[i].lower():
                        results += lines[i]
                        results += lines[i + 1]
                        results += lines[i + 2]
                        results += lines[i + 3]
                        results += "\n"
                        i += 4
                    else:
                        i += 1
        except FileNotFoundError:
            results = "No password file found."

        result_window = tk.Toplevel()
        result_window.title("Search Results")
        result_window.geometry("400x300")

        box = scrolledtext.ScrolledText(result_window, wrap=tk.WORD)
        box.pack(expand=True, fill="both")
        box.insert(tk.END, results if results else "No matches found.")
        box.config(state="disabled")

    search_win = tk.Toplevel()
    search_win.title("Search for Site")
    search_win.geometry("250x100")

    tk.Label(search_win, text="Enter site name:").pack(pady=5)
    search_entry = tk.Entry(search_win)
    search_entry.pack()
    tk.Button(search_win, text="Search", command=do_search).pack(pady=5)

def main():
    """Launches the password GUI window."""
    global site_entry, user_entry, pass_entry
    create_password_file("passwords.txt")

    window = tk.Tk()
    window.title("Password Tracker")
    window.geometry("300x340")

    tk.Label(window, text="Site:").pack(pady=5)
    site_entry = tk.Entry(window)
    site_entry.pack()

    tk.Label(window, text="Username:").pack(pady=5)
    user_entry = tk.Entry(window)
    user_entry.pack()

    tk.Label(window, text="Password:").pack(pady=5)
    pass_entry = tk.Entry(window, show="*")
    pass_entry.pack()

    tk.Button(window, text="Save Password", command=save_gui_password).pack(pady=10)
    tk.Button(window, text="View All Passwords", command=view_saved_passwords).pack(pady=5)
    tk.Button(window, text="Search for a Site", command=search_passwords).pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    main()
