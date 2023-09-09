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

options_values = {
    'pelt_color': ["<None>"] + pelt_colours,
    'tortie_pattern': ["<None>"] + tortiepatterns,
    'tortie_base': ["<None>"] + tortiebases,
    'pelt_length': ["<None>"] + pelt_length,
    'eye_colour': ["<None>"] + eye_colours,
    'eye_colour2': ["<None>"] + eye_colours,  # If eye_colour2 uses the same options as eye_colour
    'points': ["<None>"] + point_markings,
    'vitiligo': ["<None>"] + vit
}