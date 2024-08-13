import json
import os
from collections import defaultdict
import sys

BACKSTORY_DISPLAY = {
    "clan_founder_backstories": "Clan founder",
    "clanborn_backstories": "Clanborn",
    "outsider_roots_backstories": "outsider roots",
    "half_clan_backstories": "half-Clan",
    "loner_backstories": "formerly a loner",
    "rogue_backstories": "formerly a rogue",
    "kittypet_backstories": "formerly a kittypet",
    "outsider_backstories": "formerly an outsider",
    "former_clancat_backstories": "originally from another Clan",
    "orphaned_backstories": "orphaned",
    "abandoned_backstories": "abandoned"
}

BACKSTORY_CATEGORIES = {
    "clan_founder_backstories": ["clan_founder"],
    "clanborn_backstories": ["clanborn"],
    "outsider_roots_backstories": ["outsider_roots1", "outsider_roots2"],
    "half_clan_backstories": ["halfclan1", "halfclan2"],
    "loner_backstories": ["loner1", "loner2", "loner3", "loner4", "refugee2", "tragedy_survivor4", "guided3", "refugee5", "wandering_healer2"],
    "rogue_backstories": ["rogue1", "rogue2", "rogue3", "refugee4", "tragedy_survivor2", "guided2", "refugee5", "wandering_healer1"],
    "kittypet_backstories": ["kittypet1", "kittypet2", "kittypet3", "kittypet4", "refugee3", "tragedy_survivor3", "guided1", "refugee6"],
    "former_clancat_backstories": ["otherclan1", "otherclan2", "otherclan3", "ostracized_warrior", "disgraced1", "disgraced2", "disgraced3", "retired_leader", "refugee1", "tragedy_survivor1", "medicine_cat", "guided4", "refugee5"],
    "healer_backstories": ["medicine_cat", "wandering_healer1", "wandering_healer2"],
    "orphaned_backstories": ["orphaned1", "orphaned2", "orphaned3", "orphaned4", "orphaned5", "orphaned6"],
    "abandoned_backstories": ["abandoned1", "abandoned2", "abandoned3", "abandoned4"],
    "outsider_backstories": ["outsider1", "outsider2", "outsider3"]
}

def get_name(cat):
    prefix = cat['name_prefix']
    suffix = cat['name_suffix']
    status = cat['status']
    
    if status == 'leader':
        suffix = 'star'
    elif 'apprentice' in status:
        suffix = 'paw'
    elif status == 'kitten' or status == 'newborn':
        suffix = 'kit'
    
    return f"{prefix}{suffix}"

def get_age_string(moons):
    if moons < 12:
        return f"{moons} moon{'s' if moons != 1 else ''} old"
    years = moons // 12
    return f"{years} year{'s' if years != 1 else ''} old"

SKILL_DESCRIPTIONS = {
    "TEACHER": ("quick to help", "good teacher", "great teacher", "excellent teacher"),
    "HUNTER": ("moss-ball hunter", "good hunter", "great hunter", "renowned hunter"),
    "FIGHTER": ("avid play-fighter", "good fighter", "formidable fighter", "unusually strong fighter"),
    "RUNNER": ("never sits still", "fast runner", "incredible runner", "fast as the wind"),
    "CLIMBER": ("constantly climbing", "good climber", "great climber", "impressive climber"),
    "SWIMMER": ("splashes in puddles", "good swimmer", "talented swimmer", "fish-like swimmer"),
    "SPEAKER": ("confident with words", "good speaker", "great speaker", "eloquent speaker"),
    "MEDIATOR": ("quick to make peace", "good mediator", "great mediator", "skilled mediator"),
    "CLEVER": ("quick witted", "clever", "very clever", "incredibly clever"),
    "INSIGHTFUL": ("careful listener", "helpful insight", "valuable insight", "trusted advisor"),
    "SENSE": ("oddly observant", "natural intuition", "keen eye", "unnatural senses"),
    "KIT": ("active imagination", "good kitsitter", "great kitsitter", "beloved kitsitter"),
    "STORY": ("lover of stories", "good storyteller", "great storyteller", "masterful storyteller"),
    "LORE": ("interested in Clan history", "learner of lore", "lore keeper", "lore master"),
    "CAMP": ("picky nest builder", "steady paws", "den builder", "camp keeper"),
    "HEALER": ("interested in herbs", "good healer", "great healer", "fantastic healer"),
    "STAR": ("curious about StarClan", "connection to StarClan", "deep StarClan bond", "unshakable StarClan link"),
    "DARK": ("interested in the Dark Forest", "Dark Forest affinity", "deep Dark Forest bond", "unshakable Dark Forest link"),
    "OMEN": ("interested in oddities", "omen seeker", "omen sense", "omen sight"),
    "DREAM": ("restless sleeper", "strange dreamer", "dream walker", "dream shaper"),
    "CLAIRVOYANT": ("oddly insightful", "somewhat clairvoyant", "fairly clairvoyant", "incredibly clairvoyant"),
    "PROPHET": ("fascinated by prophecies", "prophecy seeker", "prophecy interpreter", "prophet"),
    "GHOST": ("morbid curiosity", "ghost sense", "ghost sight", "ghost speaker")
}

def get_skill_description(skill_name, skill_value):
    skill_name = skill_name.upper()
    if skill_name not in SKILL_DESCRIPTIONS:
        return skill_name.lower().capitalize()
    
    skill_value = int(skill_value)
    if skill_value >= 30:
        return SKILL_DESCRIPTIONS[skill_name][3]
    elif skill_value >= 20:
        return SKILL_DESCRIPTIONS[skill_name][2]
    elif skill_value >= 10:
        return SKILL_DESCRIPTIONS[skill_name][1]
    else:
        return SKILL_DESCRIPTIONS[skill_name][0]

def get_skills_string(skill_dict):
    skills = []
    if skill_dict['primary']:
        primary_skill, primary_value, _ = skill_dict['primary'].split(',')
        primary_desc = get_skill_description(primary_skill, primary_value)
        skills.append(primary_desc)
    if skill_dict['secondary']:
        secondary_skill, secondary_value, _ = skill_dict['secondary'].split(',')
        secondary_desc = get_skill_description(secondary_skill, secondary_value)
        skills.append(secondary_desc)
    
    if len(skills) == 2:
        return f"{skills[0]} and {skills[1]}"
    elif len(skills) == 1:
        return skills[0]
    else:
        return ""

def get_gender_icon(gender):
    if gender == "male":
        gender_icon = "♂"
    elif gender == "trans male":
        gender_icon = "⚧♂"
    elif gender == "female":
        gender_icon = "♀"
    elif gender == "trans female":
        gender_icon = "⚧♀"
    else:
        gender_icon = " "
    return(gender_icon)

def create_name_dict(cats):
    return {cat['ID']: get_name(cat) for cat in cats}

def get_relationships(cat_id, name_dict, clan_dir):
    relationship_dict = {}
    relationship_file = os.path.join(clan_dir, "relationships", f"{cat_id}_relations.json")
    
    if os.path.exists(relationship_file):
        with open(relationship_file, 'r') as f:
            relationships = json.load(f)
        
        for relation in relationships:
            other_cat_id = relation['cat_to_id']
            if other_cat_id in name_dict:
                friendship_score = (relation['platonic_like'] + relation['admiration'] + 
                                    relation['comfortable'] + relation['trust'])
                enmity_score = relation['dislike'] + relation['jealousy']
                romantic_score = relation['romantic_love']
                
                relationship_dict[other_cat_id] = {
                    'name': name_dict[other_cat_id],
                    'friendship_score': friendship_score,
                    'enmity_score': enmity_score,
                    'romantic_score': romantic_score
                }
    
    return relationship_dict

def get_backstory_description(backstory):
    for category, backstories in BACKSTORY_CATEGORIES.items():
        if backstory in backstories:
            return BACKSTORY_DISPLAY[category]
    return "Unknown backstory"

def process_cats(clan_name, save_dir):
    clan_dir = os.path.join(save_dir, clan_name)
    json_file = os.path.join(clan_dir, 'clan_cats.json')
    output_file = os.path.join(os.path.dirname(save_dir), "save-editor", f"{clan_name}Clan list.txt")
    
    with open(json_file, 'r') as f:
        cats = json.load(f)
    
    name_dict = create_name_dict(cats)
    
    valid_statuses = ['leader', 'deputy', 'medicine cat', 'warrior', 'mediator', 'apprentice', 
                      'medicine cat apprentice', 'mediator apprentice', 'kitten', 'newborn', 'elder', 'rogue', 'kittypet', 'loner']
    outsider_statuses = ['rogue', 'kittypet', 'loner']
    
    cat_groups = defaultdict(list)
    missing_cats = []
    outsiders = []
    rogues = []
    loners = []
    kittypets = []
    
    # Create dictionaries to store children and dead status for each cat
    children_dict = defaultdict(list)
    dead_dict = {cat['ID']: cat['dead'] for cat in cats}
    for cat in cats:
        if cat['parent1']:
            children_dict[cat['parent1']].append(cat['ID'])
        if cat['parent2']:
            children_dict[cat['parent2']].append(cat['ID'])
    
    for cat in cats:
        if cat['status'] not in valid_statuses or cat['dead']:
            continue
        
        name = get_name(cat)
        age = get_age_string(cat['moons'])
        gender = cat['gender_align']
        gender_icon = get_gender_icon(gender)
        trait = cat['trait']
        skills = get_skills_string(cat['skill_dict'])
        backstory = get_backstory_description(cat['backstory'])
        
        cat_string = f"{gender_icon} {name}:\n	{age}, {trait}, {backstory}"
        if skills:
            cat_string += f", {skills}"
        
        # Add parents information (including dead parents)
        parents = []
        if cat['parent1'] and cat['parent1'] in name_dict:
            parents.append(name_dict[cat['parent1']])
        if cat['parent2'] and cat['parent2'] in name_dict:
            parents.append(name_dict[cat['parent2']])
        
        if parents:
            cat_string += f"\n	Parents: {' and '.join(parents)}"
        
        # Add mates information (including dead mates)
        mates = [name_dict[mate_id] for mate_id in cat['mate'] if mate_id in name_dict]
        if mates:
            cat_string += f"\n	Mate{'s' if len(mates) > 1 else ''}: {', '.join(mates)}"
        
        # Add children information (excluding dead children)
        children = [name_dict[child_id] for child_id in children_dict[cat['ID']] if child_id in name_dict and not dead_dict[child_id]]
        
        # Add apprentices information (excluding dead apprentices)
        apprentices = [name_dict[app_id] for app_id in cat['current_apprentice'] if app_id in name_dict and not dead_dict[app_id]]
        if apprentices:
            cat_string += f"\n	Apprentice{'s' if len(apprentices) > 1 else ''}: {', '.join(apprentices)}"

        # Add former apprentices information (excluding dead apprentices)
        former_apprentices = [name_dict[app_id] for app_id in cat['former_apprentices'] if app_id in name_dict and not dead_dict[app_id]]
        if former_apprentices:
            cat_string += f"\n	Former Apprentice{'s' if len(former_apprentices) > 1 else ''}: {', '.join(former_apprentices)}"
        
        # Process relationships
        relationships = get_relationships(cat['ID'], name_dict, clan_dir)
        crushes = []
        friends = []
        best_friends = []
        dislikes = []
        enemies = []
        family_ids = set(cat['mate'] + [cat['parent1'], cat['parent2']] + children_dict[cat['ID']])
        
        for related_cat_id, relation in relationships.items():
            # Skip dead cats
            if dead_dict[related_cat_id]:
                continue

            if related_cat_id in family_ids:
                # Higher threshold for family members
                if relation['friendship_score'] > 240:
                    best_friends.append((relation['name'], relation['friendship_score']))
                elif relation['friendship_score'] > 180:
                    friends.append((relation['name'], relation['friendship_score']))
                if relation['enmity_score'] > 60:
                    enemies.append((relation['name'], relation['enmity_score']))
                elif relation['enmity_score'] > 30:
                    dislikes.append((relation['name'], relation['enmity_score']))
            else:
                # Normal threshold for non-family members
                if relation['romantic_score'] > 20:
                    crushes.append((relation['name'], relation['romantic_score']))
                if relation['friendship_score'] > 150:
                    best_friends.append((relation['name'], relation['friendship_score']))
                elif relation['friendship_score'] > 100:
                    friends.append((relation['name'], relation['friendship_score']))
                if relation['enmity_score'] > 50:
                    enemies.append((relation['name'], relation['enmity_score']))
                elif relation['enmity_score'] > 25:
                    dislikes.append((relation['name'], relation['enmity_score']))
        
        # Sort the relationship lists
        crushes.sort(key=lambda x: x[1], reverse=True)
        best_friends.sort(key=lambda x: x[1], reverse=True)
        friends.sort(key=lambda x: x[1], reverse=True)
        enemies.sort(key=lambda x: x[1], reverse=True)
        dislikes.sort(key=lambda x: x[1], reverse=True)
        
        # Create the relationship strings
        if best_friends:
            term = "Best Friend" if len(best_friends) == 1 else "Best Friends"
            cat_string += f"\n	{term}: {', '.join(name for name, _ in best_friends)}"
        if friends:
            term = "Friend" if len(friends) == 1 else "Friends"
            cat_string += f"\n	{term}: {', '.join(name for name, _ in friends)}"
        if enemies:
            term = "Enemy" if len(enemies) == 1 else "Enemies"
            cat_string += f"\n	{term}: {', '.join(name for name, _ in enemies)}"
        if dislikes:
            cat_string += f"\n	Dislikes: {', '.join(name for name, _ in dislikes)}"
        if crushes:
            cat_string += f"\n	Crushes: {', '.join(name for name, _ in crushes)}"
        
        status = 'kits' if cat['status'] in ['kitten', 'newborn'] else cat['status']
        
        if cat['outside']:
            if status in outsider_statuses:
                outsiders.append(cat_string)
                if status == "rogue":
                    rogues.append(cat_string)
                if status == "loner":
                    loners.append(cat_string)
                if status == "kittypet":
                    kittypets.append(cat_string)
            else:
                missing_cats.append(cat_string)
        else:
            cat_groups[status].append(cat_string)
    
    # Write to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        status_order = ['leader', 'deputy', 'medicine cat', 'mediator', 'warrior', 
                        'medicine cat apprentice', 'mediator apprentice', 'apprentice', 'kits', 'elder', 'rogue', 'loner', 'kittypet']
        clantitle = str(clan_name + "Clan")
        f.write(f"{clantitle}\n\n")
        for status in status_order:
            if status in cat_groups:
                cats_in_group = cat_groups[status]
                if len(cats_in_group) > 0:
                    plural = 's' if len(cats_in_group) > 1 else ''
                    title = status.capitalize() + plural
                    if status == 'kits':
                        title = 'Kit' + plural
                    title = title.upper()
                    f.write(f"{title}\n\n")
                    for cat in cats_in_group:
                        f.write(f"{cat}\n\n")  # Added an extra newline for readability
                    f.write("\n")
        
        if missing_cats:
            f.write("Missing cats\n")
            for cat in missing_cats:
                f.write(f"{cat}\n\n")  # Added an extra newline for readability
        
        if outsiders:
            f.write("Outsiders\n")
            if rogues:
                f.write("Rogues\n")
                for cat in rogues:
                    f.write(f"{cat}\n\n")  # Added an extra newline for readability
            if loners:
                f.write("Loners\n")
                for cat in loners:
                    f.write(f"{cat}\n\n")  # Added an extra newline for readability
            if kittypets:
                f.write("Kittypets\n")
                for cat in kittypets:
                    f.write(f"{cat}\n\n")  # Added an extra newline for readability
    
    print(f"Cat list exported to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python cat_export.py <clan_name> <save_dir>")
        sys.exit(1)
    
    clan_name = sys.argv[1]
    save_dir = sys.argv[2]
    process_cats(clan_name, save_dir)