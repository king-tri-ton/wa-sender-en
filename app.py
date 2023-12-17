import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from alright import WhatsApp
import threading
import time
import datetime

class WhatsAppSender:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Newsletter")
        self.root.geometry("800x550")

        # Main frame
        self.main_frame = tk.Frame(root, bg='#25d366')
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Fields for selecting the contact file and entering the message
        self.contact_file_label = tk.Label(self.main_frame, text="Select the contact file:", bg='#25d366', fg='white', font=('Arial', 12, 'bold'))
        self.contact_file_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.contact_file_entry = tk.Entry(self.main_frame, width=40, state='disabled', font=('Arial', 12))
        self.contact_file_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_button = tk.Button(self.main_frame, text="Browse", command=self.browse_contacts, bg='#007BFF', fg='white', font=('Arial', 12, 'bold'))
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        self.message_label = tk.Label(self.main_frame, text="Enter the message:", bg='#25d366', fg='white', font=('Arial', 12, 'bold'))
        self.message_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.message_entry = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, width=40, height=5, font=('Arial', 12))
        self.message_entry.grid(row=1, column=1, padx=10, pady=10)

        # Field for displaying logs
        self.log_label = tk.Label(self.main_frame, text="Logs:", bg='#25d366', fg='white', font=('Arial', 12, 'bold'))
        self.log_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.log_display = tk.Text(self.main_frame, wrap=tk.WORD, width=40, height=10, state='disabled', font=('Arial', 12))
        self.log_display.grid(row=2, column=1, padx=10, pady=10)

        # Button to start the newsletter
        self.start_button = tk.Button(self.main_frame, text="Start Newsletter", command=self.start_send, bg='#007BFF', fg='white', font=('Arial', 12, 'bold'))
        self.start_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Add two labels with instructions
        instruction_text1 = "Clicking the 'Start Newsletter' button will begin sending messages."
        instruction_text2 = "Do not close the program until the newsletter is complete."

        self.instruction_label1 = tk.Label(self.main_frame, text=instruction_text1, font=('Arial', 8), fg='#4c4c4c', bg='#25d366')
        self.instruction_label1.grid(row=4, column=0, columnspan=3, pady=2)

        self.instruction_label2 = tk.Label(self.main_frame, text=instruction_text2, font=('Arial', 8), fg='#4c4c4c', bg='#25d366')
        self.instruction_label2.grid(row=5, column=0, columnspan=3, pady=8)

        # Copyright
        self.copyright_label = tk.Label(root, text="© 2023 King Triton", bg='#25d366', fg='white', font=('Arial', 10))
        self.copyright_label.pack(side=tk.BOTTOM, pady=10)

        # Initialize variable to track the newsletter status
        self.sending_in_progress = False

    def browse_contacts(self):
        file_path = filedialog.askopenfilename(title="Select the contact file", filetypes=[("Text files", "*.txt")])
        self.contact_file_entry.config(state='normal')
        self.contact_file_entry.delete(0, tk.END)
        self.contact_file_entry.insert(tk.END, file_path)
        self.contact_file_entry.config(state='disabled')

    def start_send(self):
        # Check if a newsletter is already in progress
        if self.sending_in_progress:
            return

        contacts_file = self.contact_file_entry.get()
        message = self.message_entry.get("1.0", tk.END).strip()

        self.log_display.config(state='normal')
        self.log_display.delete(1.0, tk.END)

        if not contacts_file or not message:
            self.log_display.insert(tk.END, "Error: Fill in all fields\n")
            return

        # Update window title
        self.root.title("WhatsApp Newsletter (Sending messages...)")

        # Log the start of the newsletter
        start_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        start_log_message = f"Newsletter started [{start_time}]\n"
        self.log_display.insert(tk.END, start_log_message)

        # Disable "Browse" and "Start Newsletter" buttons
        self.browse_button.config(state='disabled')
        self.start_button.config(state='disabled')

        # Disable the message entry field
        self.message_entry.config(state='disabled')

        # Set the flag that the newsletter has started
        self.sending_in_progress = True

        # Launch the task in a separate thread
        threading.Thread(target=self.run_send, args=(contacts_file, message, start_time)).start()

    def run_send(self, contacts_file, message, start_time):
        try:
            # Initialize the alright instance
            messenger = WhatsApp()

            # Send the message to each contact in the file
            with open(contacts_file, 'r') as file:
                contacts = file.readlines()
                for contact in contacts:
                    contact = contact.strip()
                    if contact:
                        # Find the user
                        messenger.find_user(contact)

                        # Send the message
                        messenger.send_message(message)
                        self.log_display.insert(tk.END, f"Message sent to contact {contact}\n")

                        # Optionally, introduce a delay between messages
                        time.sleep(1)

        except Exception as e:
            self.log_display.insert(tk.END, f"Error: {str(e)}\n")

        finally:
            # Log the end of the newsletter
            end_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
            end_log_message = f"Newsletter completed [{end_time}]\n"
            self.log_display.insert(tk.END, end_log_message)

            # Quit alright to free up resources
            messenger.quit()

            # Update the interface in the main thread
            self.root.after(0, lambda: self.update_interface(start_time, end_time))

    def update_interface(self, start_time, end_time):
        # Enable "Browse" and "Start Newsletter" buttons
        self.browse_button.config(state='normal')
        self.start_button.config(state='normal')

        # Enable the message entry field
        self.message_entry.config(state='normal')

        # Set the flag that the newsletter has ended
        self.sending_in_progress = False

        # Update the window title
        self.root.title("WhatsApp Newsletter")

        # Update the interface after the newsletter is complete
        self.log_display.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppSender(root)
    root.mainloop()
