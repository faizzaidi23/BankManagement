import tkinter as tk
from tkinter import ttk, messagebox

def display_all_books_ui():
    books_list.delete(0, tk.END)
    if not books:
        books_list.insert(tk.END, "No books available in the library.")
    else:
        for book_id, book_info in books.items():
            status = "Available" if book_info[2] else "Checked Out"
            books_list.insert(tk.END, f"ID: {book_id}, Title: {book_info[0]}, Author: {book_info[1]}, Status: {status}")

def add_book_ui():
    book_id = book_id_entry.get()
    title = title_entry.get()
    author = author_entry.get()

    if book_id and title and author:
        if book_id not in books:
            books[book_id] = [title, author, True]
            messagebox.showinfo("Success", f"Book '{title}' added successfully.")
            display_all_books_ui()
            clear_input_fields()
        else:
            messagebox.showerror("Error", "Book ID already exists.")
    else:
        messagebox.showerror("Error", "All fields are required.")

def remove_book_ui():
    book_id = book_id_entry.get()

    if book_id in books:
        removed_book = books.pop(book_id)
        messagebox.showinfo("Success", f"Book '{removed_book[0]}' removed successfully.")
        display_all_books_ui()
        clear_input_fields()
    else:
        messagebox.showerror("Error", "Book ID not found.")

def check_out_book_ui():
    book_id = book_id_entry.get()

    if book_id in books:
        if books[book_id][2]:
            books[book_id][2] = False
            messagebox.showinfo("Success", f"Book '{books[book_id][0]}' checked out successfully.")
            display_all_books_ui()
        else:
            messagebox.showerror("Error", f"Book '{books[book_id][0]}' is already checked out.")
    else:
        messagebox.showerror("Error", "Book ID not found.")

def return_book_ui():
    book_id = book_id_entry.get()

    if book_id in books:
        if not books[book_id][2]:
            books[book_id][2] = True
            messagebox.showinfo("Success", f"Book '{books[book_id][0]}' returned successfully.")
            display_all_books_ui()
        else:
            messagebox.showerror("Error", f"Book '{books[book_id][0]}' was not checked out.")
    else:
        messagebox.showerror("Error", "Book ID not found.")

def clear_input_fields():
    """Clears the Book ID, Title, and Author input fields."""
    book_id_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("700x500")
root.configure(bg="#f2f2f2")

# Add a theme
style = ttk.Style()
style.theme_use("clam")  # Alternative: 'alt', 'default', 'classic'

# Styling
style.configure("TFrame", background="#f2f2f2")
style.configure("TLabel", background="#f2f2f2", font=("Arial", 12))
style.configure("TButton", font=("Arial", 10, "bold"), padding=5)
style.configure("TEntry", padding=5)
style.map("TButton", background=[("active", "#008cba")])

books = {}

# Input fields
input_frame = ttk.Frame(root)
input_frame.pack(pady=10, padx=10)

ttk.Label(input_frame, text="Book ID:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
book_id_entry = ttk.Entry(input_frame, width=30)
book_id_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Title:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
title_entry = ttk.Entry(input_frame, width=30)
title_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Author:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
author_entry = ttk.Entry(input_frame, width=30)
author_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Add Book", command=add_book_ui).grid(row=0, column=0, padx=10, pady=10)
ttk.Button(button_frame, text="Remove Book", command=remove_book_ui).grid(row=0, column=1, padx=10, pady=10)
ttk.Button(button_frame, text="Check Out", command=check_out_book_ui).grid(row=0, column=2, padx=10, pady=10)
ttk.Button(button_frame, text="Return Book", command=return_book_ui).grid(row=0, column=3, padx=10, pady=10)

# Display books list
books_list_frame = ttk.Frame(root)
books_list_frame.pack(pady=10, fill="both", expand=True)

books_list_label = ttk.Label(books_list_frame, text="Books List", font=("Arial", 14, "bold"))
books_list_label.pack(anchor="w", padx=10, pady=5)

books_list = tk.Listbox(books_list_frame, width=80, height=15, font=("Courier", 10), bg="#ffffff", fg="#333333", bd=2, relief="groove")
books_list.pack(pady=10, padx=10, fill="both", expand=True)

# Initialize the display
display_all_books_ui()

# Run the application
root.mainloop()
