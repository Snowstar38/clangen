import sys
import ujson

# Get the clan name from command line arguments
clan_name = sys.argv[1]
save_dir = sys.argv[2]

# Now generate the file paths
filename = f"{save_dir}/{clan_name}/clan_cats.json"
secondary_filename = f"{save_dir}/{clan_name}Clan.json"

# Open and load clan cats file
with open(filename, "r") as file:
    cats = ujson.load(file)

# Find the instructor (i.e., the dead cat with the highest "dead_moons" value)
dead_cats = [cat for cat in cats if cat["dead"]]
if dead_cats:
    instructor = max(dead_cats, key=lambda x: x["dead_moons"] if x["dead_moons"] is not None else 0)["ID"]
else:
    print("Warning: No dead cats found for instructor.")
    instructor = None

# Prepare updated clan_cats IDs
updated_clan_cats = ",".join([str(cat["ID"]) for cat in cats])

# Open and load secondary clan file
with open(secondary_filename, "r") as file:
    secondary_data = ujson.load(file)

# Update fields
secondary_data["instructor"] = instructor
secondary_data["leader"] = next((cat["ID"] for cat in cats if cat["status"] == "leader" and not cat["dead"]), None)
secondary_data["deputy"] = next((cat["ID"] for cat in cats if cat["status"] == "deputy" and not cat["dead"]), None)
secondary_data["med_cat"] = next((cat["ID"] for cat in cats if cat["status"] == "medicine cat" and not cat["dead"]), None)
secondary_data["clan_cats"] = updated_clan_cats

# Write the updated JSON data back to the file
with open(secondary_filename, "w") as file:
    ujson.dump(secondary_data, file, indent=4)

print("Successfully updated secondary clan file!")