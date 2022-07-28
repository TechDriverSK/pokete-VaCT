attacks = {
    # normal attacks
    "tackle": {
        "name": "Tackle",
        "factor": 3 / 2,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Tackles the enemy very hard.",
        "types": ["normal"],
        "effect": None,
        "is_generic": True,
        "ap": 30,
    },
    "cry": {
        "name": "Cry",
        "factor": 0,
        "action": "cry",
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "So loud that it confuses the enemy.",
        "types": ["normal"],
        "effect": None,
        "is_generic": False,
        "ap": 10,
    },
    "bite": {
        "name": "Bite",
        "factor": 1.75,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "A hard bite with sharp teeth.",
        "types": ["normal"],
        "effect": None,
        "is_generic": False,
        "ap": 30,
    },
    "power_bite": {
        "name": "Power Bite",
        "factor": 8,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 30,
        "desc": "The hardest bite you can think of.",
        "types": ["normal"],
        "effect": None,
        "is_generic": False,
        "ap": 5,
    },
    "chocer": {
        "name": "Choker",
        "factor": 1,
        "action": "chocer",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Chokes the enemy and makes it weaker.",
        "types": ["normal", "snake"],
        "effect": "paralyzation",
        "is_generic": True,
        "ap": 15,
    },
    "tail_wipe": {
        "name": "Tail Swipe",
        "factor": 2.5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.5,
        "min_lvl": 10,
        "desc": "Swipes through the enemy's face.",
        "types": ["normal"],
        "effect": None,
        "is_generic": False,
        "ap": 10,
    },
    "meat_skewer": {
        "name": "Meat Skewer",
        "factor": 3.5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.7,
        "min_lvl": 0,
        "desc": "Drills a horn deep in the enemy's flesh.",
        "types": ["normal"],
        "effect": None,
        "is_generic": False,
        "ap": 10,
    },
    "snooze": {
        "name": "Snooze",
        "factor": 0,
        "action": "snooze",
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 15,
        "desc": "Makes the enemy sleepy.",
        "types": ["normal"],
        "effect": "sleep",
        "is_generic": False,
        "ap": 15,
    },
    "supercow_power": {
        "name": "Supercow Power",
        "factor": 0,
        "action": "self.atc += 1",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 10,
        "desc": "Makes the Pokete angry and strong.",
        "types": ["normal"],
        "effect": None,
        "is_generic": False,
        "ap": 10,
    },
    # poison attacks
    "poison_bite": {
        "name": "Poison Bite",
        "factor": 1,
        "action": None,
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.3,
        "min_lvl": 0,
        "desc": "Makes the enemy weaker.",
        "types": ["poison", "snake"],
        "effect": "poison",
        "is_generic": True,
        "ap": 10,
    },
    "poison_thorn": {
        "name": "Poison Thorn",
        "factor": 2.75,
        "action": None,
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.1,
        "min_lvl": 15,
        "desc": "Stabs a venomous thorn into the enemy's flesh.",
        "types": ["poison"],
        "effect": "poison",
        "is_generic": False,
        "ap": 20,
    },
    # stone attacks
    "pepple_fire": {
        "name": "Pebble Fire",
        "factor": 1,
        "action": "cry",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Fires pebbles at the enemy and makes it blind.",
        "types": ["stone"],
        "effect": None,
        "is_generic": True,
        "ap": 5,
    },
    "sand_throw": {
        "name": "Sand Throw",
        "factor": 1,
        "action": "cry",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Throws sand at the enemy and makes it blind.",
        "types": ["stone"],
        "effect": None,
        "is_generic": False,
        "ap": 5,
    },
    "politure": {
        "name": "Polish",
        "factor": 0,
        "action": "politure",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Upgrades defense and attack points.",
        "types": ["stone"],
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "brick_throw": {
        "name": "Brick Throw",
        "factor": 2.5,
        "action": None,
        "world_action": "",
        "move": ["throw"],
        "miss_chance": 0.3,
        "min_lvl": 15,
        "desc": "Throws an Euler brick at the enemy.",
        "types": ["stone"],
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "stone_crush": {
        "name": "Stone crush",
        "factor": 2,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.3,
        "min_lvl": 0,
        "desc": "Crushes the enemy between two heavy stones.",
        "types": ["stone"],
        "effect": None,
        "is_generic": True,
        "ap": 20,
    },
    "rock_smash": {
        "name": "Rock Smash",
        "factor": 5,
        "action": None,
        "world_action": "",
        "move": ["pound"],
        "miss_chance": 0.1,
        "min_lvl": 15,
        "desc": "Pounds the enemy with the Pokete's full weight.",
        "types": ["stone"],
        "effect": None,
        "is_generic": True,
        "ap": 5,
    },
    "dia_stab": {
        "name": "Dia Stab",
        "factor": 5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 15,
        "desc": "Stabs the enemy with a giant diamond spike.",
        "types": ["stone"],
        "effect": None,
        "is_generic": False,
        "ap": 5,
    },
    "dazzle": {
        "name": "Dazzle",
        "factor": 1.5,
        "action": None,
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 10,
        "desc": "Shines a bright light at the enemy and dazzles them.",
        "types": ["stone"],
        "effect": "paralyzation",
        "is_generic": False,
        "ap": 20,
    },
    "dia_spikes": {
        "name": "Dia spikes",
        "factor": 2,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 20,
        "desc": "Throws a heck of a lot of diamond spikes at the enemy.",
        "types": ["stone"],
        "effect": None,
        "is_generic": False,
        "ap": 20,
    },
    # ground attacks
    "earch_quake": {
        "name": "Earthquake",
        "factor": 4,
        "action": None,
        "world_action": "",
        "move": ["pound"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Moves the ground with tremendous force.",
        "types": ["ground"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "power_roll": {
        "name": "Power Roll",
        "factor": 2.5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Rolls over the enemy.",
        "types": ["ground"],
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "toe_breaker": {
        "name": "Toe Breaker",
        "factor": 2.5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.3,
        "min_lvl": 0,
        "desc": "Breaks the enemy's toes.",
        "types": ["ground"],
        "effect": None,
        "is_generic": True,
        "ap": 20,
    },
    "ground_hit": {
        "name": "Ground Hit",
        "factor": 3,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "Damages the enemy with an unpredictable hit out of the ground.",
        "types": ["ground"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "dick_energy": {
        "name": "Dick Energy",
        "factor": 0,
        "action": "dick_energy",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Collects a great amount of energy in the Pokete's tip.",
        "types": ["ground"],
        "effect": None,
        "is_generic": False,
        "ap": 15,
    },
    "hiding": {
        "name": "Hiding",
        "factor": 0,
        "action": "hiding",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 20,
        "desc": "Makes the Pokete hide under the ground to minimize damage.",
        "types": ["ground"],
        "effect": None,
        "is_generic": False,
        "ap": 15,
    },

    # Fire attacks
    "fire_bite": {
        "name": "Fire Bite",
        "factor": 2,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Burns and bites the enemy at the same time.",
        "types": ["fire"],
        "effect": "burning",
        "is_generic": True,
        "ap": 15,
    },
    "ash_throw": {
        "name": "Ash Throw",
        "factor": 0.5,
        "action": "cry",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 15,
        "desc": "Throws ashes in the enemy's eyes.",
        "types": ["fire"],
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "flame_throw": {
        "name": "Flame Throw",
        "factor": 2.5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.3,
        "min_lvl": 15,
        "desc": "Hans! Get ze Flammenwerfer!",
        "types": ["fire"],
        "effect": "burning",
        "is_generic": True,
        "ap": 10,
    },

    "fire_ball": {
        "name": "Fire Ball",
        "factor": 4,
        "action": None,
        "world_action": "",
        "move": ["fireball"],
        "miss_chance": 0,
        "min_lvl": 25,
        "desc": "Casts a fireball at the enemy.",
        "types": ["fire"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    # flying attacks
    "flying": {
        "name": "Flying",
        "factor": 1.5,
        "action": None,
        "world_action": "teleport",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "Gives the Pokete the ability to fly you around.",
        "types": ["flying"],
        "effect": None,
        "is_generic": False,
        "ap": 30,
    },
    "pick": {
        "name": "Peck",
        "factor": 1.7,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "A peck at the enemy's weakest spot.",
        "types": ["flying", "bird"],
        "effect": None,
        "is_generic": True,
        "ap": 30,
    },
    "wind_blow": {
        "name": "Wind Blow",
        "factor": 2,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Casts a gust of wind at the enemy.",
        "types": ["flying"],
        "effect": None,
        "is_generic": True,
        "ap": 20,
    },
    "storm_gust": {
        "name": "Storm Gale",
        "factor": 6,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Casts a vicious and violent storm full of rain and hail, hitting the enemy in its weakest spots "
                "and makes it want to die.",
        "types": ["flying"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "schmetter": {
        "name": "Schmetter",
        "factor": 1.7,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "Schmetters the enemy away.",
        "types": ["flying"],
        "effect": None,
        "is_generic": False,
        "ap": 30,
    },
    "eye_pick": {
        "name": "Eye Peck",
        "factor": 2.5,
        "action": "eye_pick",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.6,
        "min_lvl": 0,
        "desc": "Pecks at one of the enemy's eyes.",
        "types": ["flying", "bird"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "wing_hit": {
        "name": "Wing Hit",
        "factor": 2.5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.5,
        "min_lvl": 0,
        "desc": "Hits the enemy with a wing.",
        "types": ["flying"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "brooding": {
        "name": "Brooding",
        "factor": 0,
        "action": "brooding",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 15,
        "desc": "Regenerates 2 HP.",
        "types": ["flying", "bird"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "power_pick": {
        "name": "Power Peck",
        "factor": 2,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.4,
        "min_lvl": 0,
        "desc": "A harsh pecking on the enemy's head.",
        "types": ["flying", "bird"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    # water attacks
    "bubble_gun": {
        "name": "Bubble Gun",
        "factor": 2,
        "action": None,
        "world_action": "",
        "move": ["gun"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Fires some bubbles at the enemy.",
        "types": ["water"],
        "effect": None,
        "is_generic": True,
        "ap": 20,
    },
    "bubble_bomb": {
        "name": "Bubble Bomb",
        "factor": 6,
        "action": "cry",
        "world_action": "",
        "move": ["bomb", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "A deadly bubble.",
        "types": ["water"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "bubble_shield": {
        "name": "Bubble Shield",
        "factor": 0,
        "action": "hiding",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Creates a giant bubble that protects the Pokete.",
        "types": ["water"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "wet_slap": {
        "name": "Wet Slap",
        "factor": 2.5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 10,
        "desc": "Gives the enemy a cold and wet slap in the face.",
        "types": ["water"],
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "shell_pinch": {
        "name": "Shell Pinch",
        "factor": 2.5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 15,
        "desc": "Pinches the enemy with its strong shell.",
        "types": ["water"],
        "effect": None,
        "is_generic": False,
        "ap": 20,
    },
    # undead attacks
    "heart_touch": {
        "name": "Heart Touch",
        "factor": 4,
        "action": "heart_touch",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 20,
        "desc": "Touches the enemy's heart with cold, ghostly claws.",
        "types": ["undead"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "confusion": {
        "name": "Confusion",
        "factor": 0,
        "action": None,
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Confuses the enemy.",
        "types": ["undead"],
        "effect": "confusion",
        "is_generic": True,
        "ap": 40,
    },
    "mind_blow": {
        "name": "Mind Blow",
        "factor": 0,
        "action": None,
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Causes confusion deep in the enemy's mind.",
        "types": ["undead"],
        "effect": "confusion",
        "is_generic": True,
        "ap": 15,
    },
    # electro attacks
    "shock": {
        "name": "Shock",
        "factor": 3 / 2,
        "action": None,
        "world_action": "",
        "move": ["arch"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Gives the enemy a shock.",
        "types": ["electro"],
        "effect": None,
        "is_generic": True,
        "ap": 30,
    },
    "charging": {
        "name": "Charging",
        "factor": 0,
        "action": "dick_energy",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 10,
        "desc": "Charges up the Pokete.",
        "types": ["electro"],
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "mega_arch": {
        "name": "Mega Arch",
        "factor": 5,
        "action": None,
        "world_action": "",
        "move": ["arch"],
        "miss_chance": 0.2,
        "min_lvl": 15,
        "desc": "Gives the enemy a massive shock.",
        "types": ["electro"],
        "effect": "paralyzation",
        "is_generic": True,
        "ap": 10,
    },
    # plant attacks
    "special_smell": {
        "name": "Special Smell",
        "factor": 0,
        "action": None,
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "Spreads a special smell that will make the enemy confused but very happy.",
        "types": ["plant"],
        "effect": "confusion",
        "is_generic": False,
        "ap": 10,
    },
    "apple_drop": {
        "name": "Apple Drop",
        "factor": 1.7,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.3,
        "min_lvl": 0,
        "desc": "Makes an apple drop on the enemy's head.",
        "types": ["plant"],
        "effect": None,
        "is_generic": False,
        "ap": 30,
    },
    "super_sucker": {
        "name": "Super Sucker",
        "factor": 0,
        "action": "super_sucker",
        "world_action": "",
        "move": ["downgrade", "shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Sucks 2 HP from the enemy and adds to its own.",
        "types": ["plant"],
        "effect": None,
        "is_generic": False,
        "ap": 10,
    },
    "sucker": {
        "name": "Sucker",
        "factor": 0,
        "action": "sucker",
        "world_action": "",
        "move": ["downgrade", "shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Sucks 1 HP from the enemy and adds to its own.",
        "types": ["plant"],
        "effect": None,
        "is_generic": False,
        "ap": 20,
    },
    "root_strangler": {
        "name": "Root Strangler",
        "factor": 1,
        "action": None,
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 20,
        "desc": "Uses old and crusty roots to strangle the enemy.",
        "types": ["plant"],
        "effect": "paralyzation",
        "is_generic": True,
        "ap": 15,
    },
    "root_slap": {
        "name": "Root Slap",
        "factor": 1.5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Uses old and crusty roots to slap the enemy.",
        "types": ["plant"],
        "effect": None,
        "is_generic": True,
        "ap": 30,
    },
    "the_old_roots_hit": {
        "name": "The Old Roots Hit",
        "factor": 50,
        "action": None,
        "world_action": "",
        "move": ["shine", "shine", "attack"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "An ancient attack that summons the deepest and oldest roots from deep in the earth to defeat the enemy.",
        "types": ["plant"],
        "effect": None,
        "is_generic": False,
        "ap": 1,
    },
    "leaf_storm": {
        "name": "Leaf Storm",
        "factor": 5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 20,
        "desc": "Blasts a bunch of spiky leaves at the enemy.",
        "types": ["plant"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "bark_hardening": {
        "name": "Bark Hardening",
        "factor": 0,
        "action": "bark_hardening",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Hardens its outer layers to protect itself.",
        "types": ["plant"],
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "poison_spores": {
        "name": "Poison Spores",
        "factor": 0,
        "action": None,
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Ejects some poisonous spores onto the enemy.",
        "types": ["plant"],
        "effect": "poison",
        "is_generic": False,
        "ap": 15,
    },
    "branch_stab": {
        "name": "Branch Stab",
        "factor": 4,
        "action": "cry",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 15,
        "desc": "Stabs the enemy with a branch, preferably in the enemy's eyes.",
        "types": ["plant"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    # ice attacks
    "freeze": {
        "name": "Freeze",
        "factor": 0,
        "action": None,
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0.1,
        "min_lvl": 10,
        "desc": "Freezes the enemy.",
        "types": ["ice"],
        "effect": "freezing",
        "is_generic": True,
        "ap": 10,
    },
    "snow_storm": {
        "name": "Snow Storm",
        "factor": 2.5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Summons a snow storm full of ice spikes onto the enemy.",
        "types": ["ice"],
        "effect": None,
        "is_generic": True,
        "ap": 20,
    },
    "sword_of_ice": {
        "name": "Sword of Ice",
        "factor": 5,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.3,
        "min_lvl": 20,
        "desc": "Stabs a giant ice spike into the enemy.",
        "types": ["ice"],
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "spikes": {
        "name": "Spikes",
        "factor": 1.75,
        "action": None,
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Stabs the enemy with some small ice spikes.",
        "types": ["ice"],
        "effect": None,
        "is_generic": True,
        "ap": 30,
    },
}

if __name__ == "__main__":
    print("\033[31;1mDo not execute this!\033[0m")
