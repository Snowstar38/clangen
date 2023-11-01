import sys
import re
import ujson
import tkinter as tk
from cat_dictionary import *
from tkinter import ttk, messagebox, filedialog
import os
import tempfile
import shutil

# Define field classes
name_fields = ['ID', 'name_prefix', 'name_suffix', 'specsuffix_hidden']
appearance_fields = ['pelt_name', 'pelt_color', 'pelt_length', 'eye_colour', 'eye_colour2', 'skin', 'tortie_base', 'pattern', 'tortie_color', 'tortie_pattern',
    'white_patches', 'points', 'vitiligo', 'scars', 'accessory', 'tint', 'white_patches_tint', 'reverse', 'opacity']
relationship_fields = ['parent1', 'parent2', 'adoptive_parents', 'mentor', 'former_mentor', 'patrol_with_mentor', 'mate', 'previous_mates', 'current_apprentice', 'former_apprentices', 'faded_offspring']
stats_fields = ['status', 'dead', 'df', 'exiled', 'outside', 'backstory', 'moons', 'dead_moons', 'skill_dict', 'trait', 'facets', 'experience']

categories = {
    "Name": name_fields,
    "Appearance": appearance_fields,
    "Relationships": relationship_fields,
    "Stats": stats_fields
}

skill_dict_widgets = []

def validate_value(key, value):
    val_type = desired_types.get(key)

    if value == '':
        if key == "name_suffix":  # Add a specific check for name suffix
            return ""
        else:
            if val_type == list:
                return []
            elif val_type == str:
                return None
            else:
                return None

    if isinstance(value, str):
        if value == "None":
            return None
        elif val_type == int:
            return int(value) if value.isdigit() else None

    if val_type == list and isinstance(value, str):
        return ujson.loads(value)  # Convert string lists to list objects

    return value

# Save cat appearance to a file
def save_appearance():
    cat_id = cat_to_edit.get('ID')
    cat_appearance_data = {field:cat_to_edit.get(field) for field in appearance_fields if field != 'pelt_length'}
    
    filename = filedialog.asksaveasfilename(defaultextension=".json", title="Save cat appearance")
    if filename:
        with open(filename, "w") as file:
            ujson.dump(cat_appearance_data, file, indent=4)

# Load the cat appearance from a file
def load_appearance():
    global temp_file_path

    filename = filedialog.askopenfilename(filetypes=[("Json files", "*.json")], title="Load cat appearance")
    if filename:
        with open(filename, "r") as file:
            cat_appearance_data = ujson.load(file)

        # Update the cat_to_edit data with the loaded appearance
        for field, value in cat_appearance_data.items():
            cat_to_edit[field] = value

        # Save the updated cat data back to the temporary file
        for cat in cats:
            if cat['ID'] == cat_to_edit.get('ID'):
                cat.update(cat_to_edit)

        # Create a temporary file
        temp_fd, temp_file_path = tempfile.mkstemp()
        with open(temp_file_path, 'w') as file:
            ujson.dump(cats, file, indent=4)
        
        # Refresh the form with temp file
        update_cat_form(cat_to_edit.get('ID'))

# A global variable that references the temporary file throughout:
temp_file_path = None

def save_changes():
    global temp_file_path
    for widget in window.grid_slaves():
        if isinstance(widget, ttk.Entry) or isinstance(widget, ttk.Checkbutton) or isinstance(widget, tk.Text):
            for subkey, combobox, entry, checkbox in skill_dict_widgets:
                skill_type = combobox.get()
                skill_level = entry.get()
                skill_hidden = checkbox.var.get()
    
                if not skill_type and not skill_level and not skill_hidden:
                    if cat_to_edit['skill_dict'] and cat_to_edit['skill_dict'].get(subkey):
                        cat_to_edit['skill_dict'][subkey] = None
                else:
                    cat_to_edit['skill_dict'][subkey] = f"{skill_type},{skill_level},{skill_hidden}"
                    
            number_string_fields = ["ID", "parent1", "parent2", "mentor"]
  
            if isinstance(widget, ttk.Entry):
                example_str = '\n'.join(examples[widget.key]) 
                if widget.key == 'pronouns':  
                    continue
                value = widget.get()
                if value.lower() == "true":
                    value = True
                elif value.lower() == "false":
                    value = False

                if widget.key in number_string_fields:  
                    if value not in ["None", ""]:
                        if not value.isdigit():
                            tk.messagebox.showerror("Validation Error", f"Invalid value for field: {widget.key}. \nExpected a number, got: \n{value} \nExample(s): \n{example_str}")
                            return
                    else:
                        value = None
                desired_type = desired_types.get(widget.key)

                if value is not None:
                    # Additional checks for string fields
                    if desired_type == str:
                        if any(unwanted_char in value for unwanted_char in ["[", "]", "{", "}", "\"", "\'"]):  # Define any unwanted characters here
                            tk.messagebox.showerror("Validation Error", f"Invalid value for field: {widget.key}.\nString fields can't contain brackets or quotes.\nYou entered:\n{value}")
                            return
                    if desired_type == list:
                        temp_value = value
                        dq_value = re.sub(r"'([^']*)'", r'"\1"', temp_value)
                        try:
                            ujson.loads(dq_value)
                        except ujson.JSONDecodeError:  
                            tk.messagebox.showerror("Validation Error", f"Invalid value for field: {widget.key}. \nExpected a list, got: {type(value)}. \nYou entered: \n{value} \nExample(s): \n{example_str}")
                            return
                        import ast

                        value = ast.literal_eval(value)

                    try:
                        if isinstance(value, desired_type):
                            pass 
                        elif desired_type == bool:
                            value = bool(value)
                        elif desired_type == int:
                            value = int(value)
                        elif desired_type == float:
                            value = float(value)
                        elif desired_type == list:
                            value = ujson.loads(value)
                        elif desired_type == dict:
                            value = ujson.loads(value)
                        elif desired_type == str:
                            if widget.key in number_string_fields: 
                                if value == "" or value.isdigit():
                                    pass
                                else:
                                    raise ValueError

                        cat_to_edit[widget.key] = value
                    except ValueError:
                        tk.messagebox.showerror("Validation Error", f"Invalid value for field: {widget.key}. \nExpected {desired_type}, got {type(value)}. \nYou entered: \n{value} \nExample(s): \n{example_str}")
                        return
                else:
                    cat_to_edit[widget.key] = value

            if isinstance(widget, ttk.Checkbutton):
                cat_to_edit[widget.key] = widget.var.get()
            elif isinstance(widget, ttk.Combobox):
                value = widget.get()
                if value == "<None>":
                    value = None
                else:
                    value = validate_value(widget.key, value)
                cat_to_edit[widget.key] = value
            elif isinstance(widget, tk.Text):
                try:
                    value = ujson.loads(widget.get('1.0', 'end'))
                except ujson.JSONDecodeError as ex:
                    tkinter.messagebox.showerror("JSON decode error", f"Please check the value of the {widget.key} field.\n\n{ex}")
                    return
                cat_to_edit[widget.key] = value

    # We create and open the temporary file within a 'with' block
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        ujson.dump(cats, temp_file, indent=4)
        temp_file_path = temp_file.name

    # Now you can freely move the temporary file to the required path
    shutil.move(temp_file_path, filename)

def update_cat_form(cat_id_to_edit):
    global cat_to_edit, options_values
    global skill_dict_widgets  # Added new global variable
    skill_dict_widgets = []    # Clear list
    for widget in window.grid_slaves():
        if widget.grid_info()['row'] > 0:  # Excluding dropdown row
            widget.destroy()

    cat_to_edit = next((cat for cat in cats if cat['ID'] == str(cat_id_to_edit)), {})
    # Splits cat information into columns
    cat_items = sorted([(key, val) for key, val in cat_to_edit.items() if key not in sum([fields for category, fields in categories.items()], [])], key=lambda x: x[0].lower())

    for column, (category, fields) in enumerate(categories.items()):
        for row, field in enumerate(fields):
            draw_form(row+2, field, cat_to_edit.get(field), column)
            cat_items = [(key, val) for key, val in cat_items if key != field]  # Keep items that are not in the category

    for j, remaining_item in enumerate(cat_items):
        draw_form(j + 2, remaining_item[0], remaining_item[1], column + 1)

    # Manually select the right options in the dropdowns
    for widget in window.grid_slaves():
        if isinstance(widget, ttk.Combobox) and widget.key in cat_to_edit:
            if widget.key == "pelt_color":
                options = pelt_colours
            elif widget.key == "pelt_name":
                options = pelt_names
            elif widget.key == "pattern":
                options = tortiepatterns
            elif widget.key == "tortie_pattern":
                options = tortiebases
            elif widget.key == "tortie_base":
                options = tortiebases
            elif widget.key == "tortie_color":
                options = pelt_colours
            elif widget.key == "pelt_length":
                options = pelt_length
            elif widget.key == "eye_colour":
                options = eye_colours    
            elif widget.key == "eye_colour2":
                options = eye_colours
            elif widget.key == "points":
                options = point_markings
            elif widget.key == "vitiligo":
                options = vit
            elif widget.key == "white_patches":
                options = white_patches
            elif widget.key == 'accessory':
                options = accessories
            elif widget.key == 'skin':
                options = skin_sprites
            elif widget.key == 'backstory':
                options = backstories
            elif widget.key == 'tint':
                options = tint
            elif widget.key == 'white_patches_tint':
                options = white_patches_tint
            else:
                options = None
            if options is not None:
                options = options + ["<None>"]
                cat_value = str(cat_to_edit[widget.key])
                value = widget.get()
                # If the value of the cat is None, select "<None>"
                if cat_value in options:
                    try:
                        # Safeguard against index error and attempt to find the index of the cat's value
                        index = options.index(cat_value) + 1
                        widget.current(index)
                    except ValueError:
                        widget.set('')
                elif cat_value in ["None", "null", "", None]:
                    cat_value = "<None>"
                    index = options.index(cat_value)
                    widget.current(0)


# An empty dictionary to store all widget references.
widget_references = {}

def draw_form(i, key, value, column):
    label = ttk.Label(window, text=key+":")
    label.grid(row=i, column=2*column, sticky="w")

    if key == 'skill_dict':
        subkeys = ['primary', 'secondary']

        # Create a new frame for the skill_dict data ONCE
        skill_dict_frame = tk.Frame(window) 
        skill_dict_frame.grid(row=i, column=2*column+1, sticky="ew")

        for j, subkey in enumerate(subkeys):
            subvalue = value.get(subkey)
            if subvalue:
                skill_type, skill_level, skill_hidden = subvalue.split(',')
            else: # If skill is null
                skill_type, skill_level, skill_hidden = None, "", False

            # Dropdown for skill type, set 'row=j' so that each dropdown appears in a new row
            combobox = ttk.Combobox(skill_dict_frame, width=10)
            combobox['values'] = [''] + skills
            combobox.set(skill_type if skill_type else "")
            combobox.grid(row=j, column=0, sticky="w")

            # Entry for skill level, set 'row=j'
            entry = ttk.Entry(skill_dict_frame)
            entry.insert(0, skill_level if skill_level else "")
            entry.grid(row=j, column=1, sticky="w")

            # Checkbox for skill_hidden, set 'row=j'
            var = tk.BooleanVar()
            var.set(skill_hidden)
            checkbox = ttk.Checkbutton(skill_dict_frame, variable=var)
            checkbox.grid(row=j, column=2, sticky="w")
            checkbox.var = var

            combobox.key = entry.key = checkbox.key = f'skill_dict.{subkey}'
            # Append(widget_tuple) on these to the skill_dict_widgets list
            skill_dict_widgets.append((subkey, combobox, entry, checkbox))

        return
    
    if key == "pelt_color":
        options = pelt_colours
    elif key == "pelt_name":
        options = pelt_names
    elif key == "pattern":
        options = tortiepatterns
    elif key == "tortie_pattern":
        options = tortiebases
    elif key == "tortie_base":
        options = tortiebases
    elif key == "tortie_color":
        options = pelt_colours
    elif key == "pelt_length":
        options = pelt_length
    elif key == "eye_colour":
        options = eye_colours    
    elif key == "eye_colour2":
        options = eye_colours
    elif key == "points":
        options = point_markings
    elif key == "vitiligo":
        options = vit
    elif key == "white_patches":
        options = white_patches
    elif key == 'accessory':
        options = accessories
    elif key == 'skin':
        options = skin_sprites
    elif key == 'backstory':
        options = backstories
    elif key == 'tint':
        options = tint
    elif key == 'white_patches_tint':
        options = white_patches_tint

    else:
        options = None

    if isinstance(value, bool):
        var = tk.BooleanVar()
        var.set(value)
        entry = ttk.Checkbutton(window, variable=var)
        entry.var = var  
    elif isinstance(value, dict) or (isinstance(value, list) and key == 'pronouns'):
        entry = tk.Text(window, height=5, width=30)
        entry.insert('end', ujson.dumps(value, indent=4))
    elif options: 
        options = [''] + options
        variable = tk.StringVar(window)
        variable.set(str(value))
        entry = ttk.Combobox(window, values=options, textvariable=variable)
    else:
        entry = ttk.Entry(window)
        entry.insert(0, str(value))
    entry.grid(row=i, column=2*column+1, sticky="ew")
    entry.key = key
    # For every widget created, save its reference in the dictionary.
    if key in appearance_fields and key != 'pelt_length':
        widget_references[key] = entry

def edit_cats():
    global window, cats, cat_to_edit, filename, temp_file_path, temp_fd
    window = tk.Tk()
    window.title("Edit Cats")

    filename = f"../saves/{clan_name}/clan_cats.json"

    # Before starting, copy the source file to a new temporary file.
    temp_fd, temp_file_path = tempfile.mkstemp()

    shutil.copy2(filename, temp_file_path)

    with open(filename,"r") as file:
        cats = ujson.load(file)

    top_frame = tk.Frame(window)
    top_frame.grid(row=0, column=0, columnspan=10)
    ttk.Button(top_frame, text="Save", command=save_changes).grid(column=1, row=0)
    ttk.Button(top_frame, text="Save Appearance", command=save_appearance).grid(column=2, row=0)  # The Save Appearance button
    ttk.Button(top_frame, text="Load Appearance", command=load_appearance).grid(column=3, row=0)  # The Load Appearance button
    variable = tk.StringVar(window)
    cat_select_dropdown = ttk.Combobox(top_frame, width=27, textvariable=variable)
    cat_select_dropdown['values'] = [cat['ID']+": "+cat['name_prefix']+(cat['name_suffix'] and cat['name_suffix'] or '') for cat in cats]
    cat_select_dropdown.current(0)  # Select first cat by default
    cat_select_dropdown.grid(column=0, row=0)
    cat_select_dropdown.bind('<<ComboboxSelected>>', lambda _: update_cat_form(variable.get().split(':')[0]))


    # Initially update the form to show the first cat's details.
    update_cat_form(cat_select_dropdown.get().split(':')[0])

    window.mainloop()

clan_name = sys.argv[1]
filename = f"../saves/{clan_name}/clan_cats.json"
edit_cats()
