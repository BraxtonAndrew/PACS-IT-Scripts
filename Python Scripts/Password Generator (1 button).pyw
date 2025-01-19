import tkinter as tk
import pyperclip
import requests
import random

# Function to fetch password from API
def get_password_from_api():
    response = requests.get("https://www.dinopass.com/password/simple")
    if response.ok:
        return response.text.strip()  # Strip any extra whitespace or newlines
    else:
        return None

# Function to capitalize the first letter
def capitalize_first_letter(password):
    return password[0].upper() + password[1:]

# Function to add an easy symbol
def add_easy_symbol(password):
    symbols = ['!', '@', '$']
    return password + random.choice(symbols)

# Function to handle button click
def generate_password():
    min_length = 12
    password = None
    
    # Keep fetching passwords until one meets the minimum length
    while password is None or len(password) < min_length:
        password = get_password_from_api()
        if password:
            password = capitalize_first_letter(password)
            password = add_easy_symbol(password)

    # Update the entry and clipboard with the valid password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a frame for the password entry
entry_frame = tk.Frame(root)
entry_frame.pack(pady=20)

# Create the password entry
password_entry = tk.Entry(entry_frame, font=("Helvetica", 24), bd=0, bg="lightgrey")
password_entry.pack(padx=10)

# Create a frame for the button and place it at the bottom
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create the generate button
generate_button = tk.Button(button_frame, text="Generate and Copy", command=generate_password)
generate_button.pack()

# Run the application
root.mainloop()
