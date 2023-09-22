import age_sort, cat_dictionary, clanfile_ID_update, edit_cats, ID_reassign
import os
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

# Get current working directory
current_working_directory = os.getcwd()
messagebox.showwarning("Backup your data", "Please remember to make backup copies of your save files before making changes with this tool!")
# Defining functions to call scripts
def run_script(script_name):
    clan = clan_var.get()
    # Handle case in which no Clan is selected
    if not clan:
        messagebox.showwarning("No Clan Selected", "Please select a Clan from the dropdown menu before proceeding.")
        return
    response = os.system('python {}/{}.py {}'.format(current_working_directory, script_name, clan))
    # Check whether the script ran successfully
    if response != 0:
        messagebox.showerror("Error", f"An error occurred while trying to run the {script_name} script. Please check that the necessary files exist.")

def run_age_sort():
    run_script('age_sort')

def run_ID_reassign():
    run_script('ID_reassign')

def run_clanfile_ID_update():
    run_script('clanfile_ID_update')

def run_edit_cats():
    run_script('edit_cats')

# Get list of subdirectories in the 'saves' directory
def get_clan_names(dir='../saves'):  
    return next(os.walk(dir))[1]

# Initialize the tkinter window
root = tk.Tk()

# New! Add a reminder for players to backup their saves
reminder = tk.Label(root, text="Please remember to back up your saves!", fg="red")  # fg="red" makes the text red
reminder.grid(column=1, row=1, columnspan=2)  # Place it above the clan dropdown

# Add a label
ttk.Label(root, text="Select a Clan:").grid(column=0, row=1)  # 'row' is now '1'

# Add a label
ttk.Label(root, text="Select a Clan:").grid(column=0, row=0) 

# Create a dropdown menu
clan_var = tk.StringVar()
clan_dropdown = ttk.Combobox(root, width=27, textvariable=clan_var)

# Set the choices in the dropdown to be the clan names
clan_dropdown['values'] = get_clan_names() 
clan_dropdown.grid(column=1, row=0)

class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)
        
    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 35
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{int(x)}+{int(y)}")
        label = tk.Label(self.tooltip, text=self.text, background="white")
        label.pack()
    
    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

# Add script execution buttons
sort_cats_button = ttk.Button(root, text="Sort Cats by Age", command=run_age_sort)
sort_cats_button.grid(column=0, row=2)
ToolTip(sort_cats_button, "Sort all cats in the clan in clan_cats.json by their ages")

reassign_ID_button = ttk.Button(root, text="Reassign Cat IDs", command=run_ID_reassign)
reassign_ID_button.grid(column=0, row=3)
ToolTip(reassign_ID_button, "Assign new unique IDs to each cat, starting at 1 - BUGGY, WILL REMOVE RELATIONSHIPS")

update_ID_list_button = ttk.Button(root, text="Update Clan ID Lists", command=run_clanfile_ID_update)
update_ID_list_button.grid(column=0, row=4)
ToolTip(update_ID_list_button, "Update the saved list of cat IDs for the clan in clan.json - BUGGY, WILL REMOVE RELATIONSHIPS")

edit_cats_button = ttk.Button(root, text="Edit Cats", command=run_edit_cats)
edit_cats_button.grid(column=0, row=5)
ToolTip(edit_cats_button, "Open the cat editor")

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.grid(column=1, row=6)
ToolTip(quit_button, "Close the application")

# Add a button to close the application
ttk.Button(root, text="Quit", command=root.destroy).grid(column=1, row=6)

root.mainloop()