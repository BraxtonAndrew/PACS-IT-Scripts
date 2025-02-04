import tkinter as tk
import subprocess
import sys

# Function to install the requests module if not already installed
def install_requests():
    try:
        import requests
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
    return requests

# Install and import the requests module
requests = install_requests()

def generate_password():
    # Define the API endpoint
    url = "https://password.ninja/api/password?minPassLength=12&instruments=true&colours=true&shapes=true&food=true&sports=true&transport=true&symbols=true&numOfPasswords=1&maxLength=14&excludeSymbols=sfha"
    
    # Make the GET request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the generated password from the response
        password = response.text.strip('\"')  # Remove quotes
        password = password.capitalize()  # Capitalize the first letter
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    else:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Failed to retrieve password")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()  # Now it stays on the clipboard after the window is closed

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a frame for the password entry
entry_frame = tk.Frame(root)
entry_frame.pack(pady=20)

# Create the password entry
password_entry = tk.Entry(entry_frame, font=("Helvetica", 24), bd=0, bg="lightgrey")
password_entry.pack(padx=10)

# Create a frame for the buttons and place it at the bottom
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create the generate button
generate_button = tk.Button(button_frame, text="Generate", command=generate_password)
generate_button.grid(row=0, column=0, padx=10)

# Create the copy button
copy_button = tk.Button(button_frame, text="Copy", command=copy_password)
copy_button.grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()
