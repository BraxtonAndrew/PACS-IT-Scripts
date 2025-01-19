import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
import json

domain = 'https://pacs.freshservice.com'
api_key = 'REPLACEME'  #################### CHANGE TO YOUR API KEY (Instructions in README) #####################
password = 'x'



def create_time_entry():
    

    def on_click(event):
        ticket_number = ticket_number_entry.get()
        time_spent = time_spent_entry.get()
        # Get mouse click coordinates
        x = event.x_root
        y = event.y_root

        # Create temporary window for note
        note_window = tk.Tk()
        note_window.title("Enter Note")
        # Adjust window size as needed
        note_window.geometry('400x150')

        # Position the window at click coordinates
        note_window.geometry(f"+{x}+{y}")

        note_label = tk.Label(note_window, text="Note")
        note_label.pack()

        note_text = tk.Text(note_window, height=5)
        note_text.pack()

        def submit_and_close_note():
            note = note_text.get('1.0', tk.END)
            # Replace with your API URL
            url = f"{domain}/api/v2/tickets/{ticket_number}/time_entries"
            headers = {'Content-Type': 'application/json'}
            data = json.dumps({
                'time_entry': {
                    'time_spent': time_spent,
                    'agent_id': REPLACEME,  ################ Change to your responder ID (Ask Logan or Parker) ####################
                    'billable': True,
                    'note': note,
                }
            })

            # Send API request (replace with your logic)
            try:
                response = requests.post(url, auth=(api_key, password), headers=headers, data=data)
                response.raise_for_status()  # Raise exception for error responses
                messagebox.showinfo("Success", "Time entry created successfully!")
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"Error creating time entry: {str(e)}")

            note_window.destroy()  # Destroy temporary window after submit
            root.deiconify()


        submit_button = tk.Button(note_window, text="Submit Note", command=submit_and_close_note)
        submit_button.pack()

        note_window.mainloop()


    create_entry_button.bind("<Button-1>", on_click)



def start_timer():
    

    def on_click(event):
        ticket_number = ticket_number_entry.get()
        # Get mouse click coordinates
        x = event.x_root
        y = event.y_root

        # Create temporary window for note
        note_window = tk.Tk()
        note_window.title("Enter Note")
        # Adjust window size as needed
        note_window.geometry('400x150')

        # Position the window at click coordinates
        note_window.geometry(f"+{x}+{y}")

        note_label = tk.Label(note_window, text="Note")
        note_label.pack()

        note_text = tk.Text(note_window, height=5)
        note_text.pack()

        def submit_and_close_note():
            note = note_text.get('1.0', tk.END)


            # API URL for retrieving time entries
            url = f"{domain}/api/v2/tickets/{ticket_number}/time_entries"
            headers = {'Content-Type': 'application/json'}
            data = json.dumps({
                'time_entry': {
                    'timer_running': 'true',
                    'agent_id': REPLACEME,  ################ Change to your responder ID (Ask Logan or Parker) ####################
                    'billable': True,
                    'note': note,
                }
            })

            # Send API request (replace with your logic)
            try:
                response = requests.post(url, auth=(api_key, password), headers=headers, data=data)
                response.raise_for_status()  # Raise exception for error responses
                messagebox.showinfo("Success", "Time entry created successfully!")
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"Error creating time entry: {str(e)}")

            note_window.destroy()  # Destroy temporary window after submit

        submit_button = tk.Button(note_window, text="Submit Note", command=submit_and_close_note)
        submit_button.pack()

        note_window.mainloop()


    start_timer_button.bind("<Button-1>", on_click)

def stop_timer():
    root.unbind("<Button-1>")
    try:
        ticket_number = ticket_number_entry.get()

        # API URL for retrieving time entries
        url = f"{domain}/api/v2/tickets/{ticket_number}/time_entries"
        headers = {'Content-Type': 'application/json'}

        try:
            # Fetch time entries for the ticket
            response = requests.get(url, auth=(api_key, password), headers=headers)
            response.raise_for_status()

            # Extract time entry data
            time_entry_data = response.json()

            # Check if any timers are running
            if time_entry_data and 'time_entries' in time_entry_data:
                time_entries = time_entry_data['time_entries']

                # Loop through each time entry and stop running timers
                for entry in time_entries:
                    if entry['timer_running']:  # Check if timer is running
                        time_entry_id = entry['id']
                        stop_url = f"{domain}/api/v2/tickets/{ticket_number}/time_entries/{time_entry_id}"
                        data = {'timer_running': False}

                        # Send PUT request to stop the timer
                        response = requests.put(stop_url, auth=(api_key, password), headers=headers, json=data)
                        response.raise_for_status()

                # Display success message
                messagebox.showinfo("Stop Timer", f"Stopped all running timers")
            else:
                messagebox.showinfo("Stop Timer", "No running timers found for this ticket.")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to stop timer: {e}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f'Error occurred while trying to stop stimer: {e}')


#clear ticket number box
def clear_ticket_number():
    ticket_number_entry.delete(0, 100)


# Unbind the click


# Create the main window
root = Tk()
root.title("Ticket Time Tool 3.0")
root.geometry("300x210")

# Ticket Number Label
ticket_number_label = tk.Label(root, text="Ticket Number")
ticket_number_label.pack()

# Ticket Number Entry
ticket_number_entry = tk.Entry(root)
ticket_number_entry.pack()

# Clear Button
clear_button = tk.Button(
    root, text="Clear", command=clear_ticket_number,
    width="4", height="1", padx=1, pady=1, bg="#000000",
    fg="#ffffff"
)
clear_button.pack()

# Time Spent Label
time_spent_label = tk.Label(root, text="Time Spent (HH:MM):")
time_spent_label.pack()

# Time Spent Entry
time_spent_entry = tk.Entry(root)
time_spent_entry.pack()

# Create Entry Button
create_entry_button = tk.Button(
    root, text="Create Time Entry", command=create_time_entry, activebackground="purple", activeforeground="white"
)
create_entry_button.pack()

# Start Timer Button
start_timer_button = tk.Button(
    root, text="Start Timer", command=start_timer, activebackground="green", activeforeground="yellow"
)
start_timer_button.pack()

# Stop Timer Button
stop_timer_button = tk.Button(
    root, text="Stop All Timers", command=stop_timer, activebackground="red", activeforeground="black"
)
stop_timer_button.pack()

root.mainloop()
 
