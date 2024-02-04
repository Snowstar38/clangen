import ujson

# Read the JSON data from the file
filename = "clan_cats.json"
with open(filename, "r") as file:
    cats = ujson.load(file)

# Create a list of cats with their IDs
cat_list = []
for cat in cats:
    cat_id = cat["ID"]
    cat_name = cat["name_prefix"] + cat["name_suffix"]
    cat_list.append((cat_id, cat_name))

# Save the list of cats with their IDs to a text file
output_filename = "ID masterlist.txt"
with open(output_filename, "w") as file:
    for cat_id, cat_name in cat_list:
        file.write(f"ID: {cat_id} | Name: {cat_name}\n")
