import sys
import ujson

# Get the clan name from command line arguments
clan_name = sys.argv[1]

# Now generate the file paths
filename = f"../saves/{clan_name}/clan_cats.json"

# Now use these paths in the rest of your script
with open(filename, "r") as file:
    cats = ujson.load(file)

# Separate cats based on their status (living, dead, Clan, outsider)
living_clan_cats = [cat for cat in cats if not cat['dead'] and not cat['outside']]
living_outsiders = [cat for cat in cats if not cat['dead'] and cat['outside']]
dead_outsiders = [cat for cat in cats if cat['dead'] and cat['outside']]
dead_clan_cats = [cat for cat in cats if cat['dead'] and not cat['outside']]

# Sort each category by age (measured in moons)
sorted_living_clan_cats = sorted(living_clan_cats, key=lambda x: x['moons'], reverse=True)
sorted_living_outsiders = sorted(living_outsiders, key=lambda x: x['moons'], reverse=True)

# Sort the dead cats by the sum of their "moons" and "dead_moons" values
sorted_dead_outsiders = sorted(dead_outsiders, key=lambda x: x['moons'] + x['dead_moons'], reverse=True)
sorted_dead_clan_cats = sorted(dead_clan_cats, key=lambda x: x['moons'] + x['dead_moons'], reverse=True)

# Combine the sorted lists in the desired order
sorted_cats = sorted_living_clan_cats + sorted_living_outsiders + sorted_dead_outsiders + sorted_dead_clan_cats

# Write the sorted JSON data back to the file
with open(filename, "w") as file:
    ujson.dump(sorted_cats, file, indent=4)