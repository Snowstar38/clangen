desired_types = {
    'ID': str,
    'name_prefix': str,
    'name_suffix': str,
    'specsuffix_hidden': bool,
    'gender': str,
    'gender_align': str,
    'pronouns': list,
    'birth_cooldown': int,
    'status': str,
    'backstory': str,
    'moons': int,
    'trait': str,
    'facets': str,
    'parent1': str,
    'parent2': str,
    'adoptive_parents': list,
    'mentor': str,
    'former_mentor': list,
    'patrol_with_mentor': int,
    'mate': list,
    'previous_mates': list,
    'dead': bool,
    'paralyzed': bool,
    'no_kits': bool,
    'no_retire': bool,
    'no_mates': bool,
    'exiled': bool,
    'pelt_name': str,
    'pelt_color': str,
    'pelt_length': str,
    'sprite_kitten': int,
    'sprite_adolescent': int,
    'sprite_adult': int,
    'sprite_senior': int,
    'sprite_para_adult': int,
    'eye_colour': str,
    'eye_colour2': str,
    'reverse': bool,
    'white_patches': str,
    'vitiligo': str,
    'points': str,
    'white_patches_tint': str,
    'pattern': str,
    'tortie_base': str,
    'tortie_color': str,
    'tortie_pattern': str,
    'skin': str,
    'tint': str,
    'skill_dict': dict,
    'scars': list,
    'accessory': str,
    'experience': int,
    'dead_moons': int,
    'current_apprentice': list,
    'former_apprentices': list,
    'df': bool,
    'outside': bool,
    'faded_offspring': list,
    'opacity': int,
    'prevent_fading': bool,
    'favourite': bool
}

pelt_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK', 'CREAM', 'PALEGINGER', 'GOLDEN',
    'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN', 'CHOCOLATE'
]
tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR',
                'HALF', 'OREO', 'SWOOP', 'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'ORIOLE', 'CHIMERA',
                'DAUB', 'EMBER', 'BLANKET', 'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI', 'SMUDGED', 'DAPPLENIGHT', 'STREAK',
                'MASK', 'CHEST', 'ARMTAIL', 'SMOKE', 'GRUMPYFACE', 'BRIE', 'BELOVED']
tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel', 'classic', 'sokoke', 'agouti',
            'singlestripe']
pelt_length = ["short", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 
    'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER']
point_markings = ['COLOURPOINT', 'RAGDOLL', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']
vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'KARPATI', 'POWDER', 'BLEACHED']

little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY', 'LUNA',
                'EXTRA', 'MUSTACHE', 'REVERSEHEART', 'SPARKLE', 'RIGHTEAR', 'LEFTEAR', 'ESTRELLA', 'REVERSEEYE', 'BACKSPOT',
                'EYEBAGS']
mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR', 'WINGS',
            'DIVA', 'SAVANNAH', 'FADESPOTS', 'BEARD', 'DAPPLEPAW', 'TOPCOVER', 'WOODPECKER', 'MISS', 'BOWTIE', 'VEST', 'FADEBELLY']
high_white = ['ANY', 'ANYTWO', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO',
            'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
            'CURVED', 'GLASS', 'MASKMANTLE', 'MAO', 'PAINTED', 'SHIBAINU', 'OWL', 'BUB', 'SPARROW', 'TRIXIE',
            'SAMMY', 'FRONT', 'BLOSSOMSTEP', 'BULLSEYE']
mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO','PEBBLESHINE', 'BOOTS', 'COW', 'COWTWO', 'LOVEBUG', 'SHOOTINGSTAR',
                'EYESPOT', 'PEBBLE', 'TAILTWO', 'BUDDY']
                
white_patches =  little_white + mid_white + high_white + mostly_white

plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                    "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                    "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
                    ]
wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
                    ]
tail_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS"]
collars = [
    "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
    "BLACK", "SPIKES", "WHITE", "PINK", "PURPLE", "MULTI", "INDIGO", "CRIMSONBELL", "BLUEBELL",
    "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
    "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL", "PINKBELL", "PURPLEBELL",
    "MULTIBELL", "INDIGOBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
    "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW", "PINKBOW",
    "PURPLEBOW", "MULTIBOW", "INDIGOBOW", "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON",
    "REDNYLON", "LIMENYLON", "GREENNYLON", "RAINBOWNYLON",
    "BLACKNYLON", "SPIKESNYLON", "WHITENYLON", "PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON",
]

accessories = plant_accessories + wild_accessories + tail_accessories + collars

tabbies = ["Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti"]
spotted = ["Speckled", "Rosette"]
plain = ["SingleColour", "TwoColour", "Smoke", "Singlestripe"]
exotic = ["Bengal", "Marbled"]
torties = ["Tortie", "Calico"]
pelt_names = tabbies + spotted + plain + exotic + torties

skin_sprites = ['BLACK',  'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE', 'RED']
                
tint = ['pink', 'gray', 'red', 'black', 'orange', 'yellow', 'purple', 'blue']

white_patches_tint = ["darkcream", "cream", "offwhite", "gray", "pink"]
                
backstories = [
  "clan_founder", "clanborn", "outsider_roots1", "outsider_roots2", "halfclan1", "halfclan2", "loner1", "loner2", "refugee2", "tragedy_survivor4", "guided3",
  "refugee5", "wandering_healer2", "rogue1", "rogue2", "rogue3", "refugee4", "tragedy_survivor2", "guided2", "refugee5", "wandering_healer1", "kittypet1", "kittypet2",
  "kittypet3", "kittypet4", "refugee3", "tragedy_survivor3", "guided1", "otherclan1", "otherclan2", "otherclan3", "ostracized_warrior", "disgraced1", "disgraced2",
  "disgraced3", "retired_leader", "refugee1", "tragedy_survivor1", "medicine_cat", "guided4", "refugee5", "medicine_cat", "wandering_healer1", "wandering_healer2",
  "orphaned1", "orphaned2", "orphaned3", "orphaned4", "orphaned5", "orphaned6", "abandoned1", "abandoned2", "abandoned3", "abandoned4", "outsider1", "outsider2", "outsider3"]
  
skills = ['TEACHER', 'HUNTER', 'FIGHTER', 'RUNNER', 'CLIMBER', 'SWIMMER', 'SPEAKER', 'MEDIATOR', 'CLEVER', 'INSIGHTFUL', 'SENSE', 'KIT', 'STORY', 'LORE', 'CAMP', 'HEALER', 'STAR', 'DARK', 'OMEN', 'DREAM', 'CLAIRVOYANT', 'PROPHET', 'GHOST']

options_values = {
    'pelt_color': pelt_colours,
    'pelt_name': pelt_names,
    'pattern': ["<None>"] + tortiepatterns,  # This is the TORTIE pattern (i.e., where the primary and secondary colors go)
    'tortie_base': ["<None>"] + tortiebases,  # This is the fur pattern for the PRIMARY color
    'tortie_color': ["<None>"] + pelt_colours,  # This is the fur color for the SECONDARY color
    'tortie_pattern': ["<None>"] + tortiebases,  # This is the fur pattern for the SECONDARY color
    'pelt_length': pelt_length,
    'eye_colour': eye_colours,
    'eye_colour2': ["<None>"] + eye_colours,  # If eye_colour2 uses the same options as eye_colour
    'points': ["<None>"] + point_markings,
    'vitiligo': ["<None>"] + vit,
    'white_patches': ["<None>"] + white_patches,
    'accessory': ["<None>"] + accessories,
    'skin': skin_sprites,
    'backstory': backstories,
    'tint': tint,
    'white_patches_tint': white_patches_tint
}