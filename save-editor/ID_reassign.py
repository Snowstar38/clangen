import sys
import ujson

# Get the clan name from command line arguments
clan_name = sys.argv[1]

# Now generate the file paths
filename = f"../saves/{clan_name}/clan_cats.json"

# Now use these paths in the rest of your script
with open(filename, "r") as file:
    cats = ujson.load(file)

IDs = {"leader": 1, "deputy": 2, "medicine cat": 3}
id_count = 4
id_mates_apprentices = {"mate", "previous_mates", "current_apprentice", "former_apprentices", "mentor", "former_mentor"}

# First handle the special positions
for cat in cats:
    if cat['status'] in IDs and cat['dead'] == False:
        cat['ID'] = str(IDs[cat['status']])
        if cat['status'] == 'medicine cat':
            IDs[cat['status']] += 1  # Increment ID for next medicine cat
        # Clear out related cats
        for key in id_mates_apprentices:
            if key in cat:
                cat[key] = []
    else:
        cat['ID'] = str(id_count)
        id_count += 1
        # Clear out related cats
        for key in id_mates_apprentices:
            if key in cat:
                cat[key] = []

# Write the sorted JSON data back to the file
with open(filename, "w") as file:
    ujson.dump(cats, file, indent=4)

print("Finished reassigning ids!")