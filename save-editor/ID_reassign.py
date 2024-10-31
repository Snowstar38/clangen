import sys
import ujson

# Get the clan name from command line arguments
clan_name = sys.argv[1]
save_dir = sys.argv[2]

# Now generate the file paths
filename = f"{save_dir}/{clan_name}/clan_cats.json"

# Load the file
with open(filename, "r") as file:
    cats = ujson.load(file)

id_count = 1 # Start ID count from 1
id_mates_apprentices_mult = {"mate", "previous_mates", "current_apprentice", "former_apprentices", "former_mentor"}
id_mates_apprentices_sing = {"mentor"}

normal_cats = []  # A list to store the remaining cats 

ordered_status = ["leader", "deputy", "medicine cat"] # Order of statuses

# First handle the special positions
for status in ordered_status:
    for cat in cats:
        cat['mentor'] = None
        if cat['status'] == status and cat['dead'] == False:
            cat['ID'] = str(id_count)
            id_count += 1  # Increment ID for next cat
            print(id_count, "special")
            # Clear out related cats
            for key in id_mates_apprentices_mult:
                if key in cat:
                    cat[key] = []
            for key in id_mates_apprentices_sing:
                if key in cat:
                    cat[key] = None
                if cat['mentor'] == []:
                    cat['mentor'] = None
        elif cat['status'] not in ordered_status and cat not in normal_cats: # If not a special cat and we're on the last iteration, add to normal_cats for later processing
            normal_cats.append(cat)
        elif cat['dead'] == True and cat not in normal_cats: # If not a special cat and we're on the last iteration, add to normal_cats for later processing
            normal_cats.append(cat)
# Now handle the normal cats
for cat in normal_cats:
    cat['ID'] = str(id_count)
    id_count += 1
    print(id_count, "normal")
    # Clear out related cats
    for key in id_mates_apprentices_mult:
        if key in cat:
            cat[key] = []

# Write the sorted JSON data back to the file
with open(filename, "w") as file:
    ujson.dump(cats, file, indent=4)

print("Finished reassigning ids!")