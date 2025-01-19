import requests
import json
import datetime
import tkinter as tk
from tkinter import messagebox

# credentials
domain = 'https://pacs.freshservice.com'
api_key = 'REPLACE-ME'  #################### CHANGE TO YOUR API KEY #####################
password = 'x'

responder_ID = REPLACEME #################### CHANGE TO YOUR RESPONDER ID (Ask Logan or Parker) #####################
group_ID = REPLACEME #################### CHANGE TO YOUR GROUP ID (Listed in the README) #####################

# Create ticket
def create_ticket():
    ticket_number_entry = ticket_number_text.get()

    # Construct URL and data
    ticket_url = f"{domain}/api/v2/tickets"
    ticket_headers = {'Content-Type': 'application/json'}
    ticket_data = json.dumps({
        'category': "Other",
        'email': "Phone_call@email.com",
        'status': 2,
        'priority': 1,
        'source': 3,
        'subject': (f'| Phone Call, {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M")}'),
        'description': (f"User called in, see notes for info. Agent, change requester email to proper email address"),
        'workspace_id': 11,
        'group_id': group_ID,  
        'responder_id': responder_ID,  
        'custom_fields': {
            'issuetype': 'Other'
        }
    })

    # Send request to create ticket
    try:
        ticket_response = requests.post(ticket_url, auth=(api_key, password), headers=ticket_headers, data=ticket_data)
        ticket_response.raise_for_status()  # Raise exception for error responses

        # Extract ticket number
        ticket_number = ticket_response.json()['ticket']['id']
        ticket_number_text.delete(0, tk.END)
        ticket_number_text.insert(0, ticket_number)

        # Copy ticket number to clipboard
        copy_text()

        # Start timer on the ticket
        start_timer(ticket_number)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error creating ticket: {str(e)}")

def start_timer(ticket_number):
    url = f"{domain}/api/v2/tickets/{ticket_number}/time_entries"
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({
        'time_entry': {
            'timer_running': 'true',
            'agent_id': responder_ID,  
            'billable': True,
        }
    })

    # Send request to start timer
    try:
        response = requests.post(url, auth=(api_key, password), headers=headers, data=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error starting timer: {str(e)}")

# Copy button function
def copy_text():
    text_to_copy = ticket_number_text.get()
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(text_to_copy)  # Append the text to the clipboard
    root.update()  # Update the clipboard

# Create the main window
root = tk.Tk()
root.title("Ticket Creation Tool")
root.geometry("200x100")

# Label for ticket number entry
ticket_number_label = tk.Label(root, text="New Ticket Number:")
ticket_number_label.pack()

# Text entry field for ticket number (initially empty)
ticket_number_text = tk.Entry(root)
ticket_number_text.pack()

# Button to create ticket
start_button = tk.Button(root, text="Create Ticket & Copy", command=create_ticket)
start_button.pack()

# Copy button
#copy_button = tk.Button(root, text="Copy", command=copy_text)
#copy_button.pack()

root.mainloop()
