import random

class Killer:
    def __init__(self, killer_name, killer_perks):
        self.killer_name = killer_name
        self.killer_perks = killer_perks
    
    def display_killer_perks(self):
        print(f'Killer {self.killer_name} has the following perks: ')
        print(self.killer_perks)


trapper = Killer("Trapper", ["Unnerving Presence", "Brutal Strength", "Agitation"])
wraith = Killer("Wraith", ["Predator", "Bloodhound", "Shadowborn"])
hillbilly = Killer("Hillbilly", ["Enduring", "Lightborn", "Tinkerer"])
nurse = Killer("Nurse", ["Stridor", "Thanatophobia", "A Nurse's Calling"])
shape = Killer("Shape (Michael Myers)", ["Save the Best for Last", "Play with Your Food", "Dying Light"])
hag = Killer("Hag", ["Hex: The Third Seal", "Hex: Ruin", "Hex: Devour Hope"])
doctor = Killer("Doctor", ["Overcharge", "Monitor & Abuse", "Overwhelming Presence"])
huntress = Killer("Huntress", ["Beast of Prey", "Territorial Imperative", "Hex: Huntress Lullaby"])
cannibal = Killer("Cannibal", ["Knock Out", "Barbecue & Chilli", "Franklin's Demise"])
nightmare = Killer("Nightmare (Freddy Krueger)", ["Fire Up", "Remember Me", "Blood Warden"])
pig = Killer("Pig", ["Hangman's Trick", "Surveillance", "Make Your Choice"])
clown = Killer("Clown", ["Bamboozle", "Coulrophobia", "Pop Goes the Weasel"])
spirit = Killer("Spirit", ["Spirit Fury", "Hex: Haunted Ground", "Rancor"])
legion = Killer("Legion", ["Discordance", "Mad Grit", "Iron Maiden"])
plague = Killer("Plague", ["Corrupt Intervention", "Infectious Fright", "Dark Devotion"])
ghost_face = Killer("Ghost Face", ["I'm All Ears", "Thrilling Tremors", "Furtive Chase"])
demogorgon = Killer("Demogorgon", ["Surge", "Cruel Limits", "Mindbreaker"])
oni = Killer("Oni", ["Zanshin Tactics", "Blood Echo", "Nemesis"])
deathslinger = Killer("Deathslinger", ["Gearhead", "Dead Man's Switch", "Hex: Retribution"])
executioner = Killer("Executioner (Pyramid Head)", ["Forced Penance", "Trail of Torment", "Deathbound"])
blight = Killer("Blight", ["Dragon's Grip", "Hex: Blood Favour", "Hex: Undying"])
twins = Killer("Twins", ["Hoarder", "Oppression", "Coup de Grâce"])
trickster = Killer("Trickster", ["Starstruck", "Hex: Crowd Control", "No Way Out"])
nemesis = Killer("Nemesis", ["Lethal Pursuer", "Hysteria", "Eruption"])
cenobite = Killer("Cenobite (Pinhead)", ["Deadlock", "Hex: Plaything", "Scourge Hook: Gift of Pain"])
artist = Killer("Artist", ["Grim Embrace", "Scourge Hook: Pain Resonance", "Hex: Pentimento"])
onryo = Killer("Onryō", ["Scourge Hook: Floods of Rage", "Call of Brine", "Merciless Storm"])
dredge = Killer("Dredge", ["Septic Touch", "Dissolution", "Darkness Revealed"])
mastermind = Killer("Mastermind (Albert Wesker)", ["Superior Anatomy", "Awakened Awareness", "Terminus"])
knight = Killer("Knight", ["Nowhere to Hide", "Hubris", "Face the Darkness"])
skull_merchant = Killer("Skull Merchant", ["Game Afoot", "THWACK!", "Leverage"])
singularity = Killer("Singularity", ["Genetic Limits", "Forced Hesitation", "Quantum Instability"])
xenomorph = Killer("Xenomorph", ["Ultimate Weapon", "Rapid Brutality", "Alien Instinct"])



def choose_killer():
    
    global all_selected_perks
    
    all_killers = [
        trapper, wraith, hillbilly, nurse, shape, hag, doctor, huntress,
        cannibal, nightmare, pig, clown, spirit, legion, plague, ghost_face,
        demogorgon, oni, deathslinger, executioner, blight, twins, trickster,
        nemesis, cenobite, artist, onryo, dredge, mastermind, knight, skull_merchant,
        singularity, xenomorph
    ]
    
    print('Available killers: ')
    for i, killer in enumerate(all_killers, 1):
        print(f'{i}. {killer.killer_name}')
    
    your_killers_input = input('Select the killers by number (comma-separated): ')
    your_killers_str = your_killers_input.split(',')
    your_killers = [int(killer.strip()) for killer in your_killers_str]
    
    try:
        selected_killers = [all_killers[killer - 1] for killer in your_killers]
        print(f'Selected killers: {", ".join(k.killer_name for k in selected_killers)}')
        
        all_selected_perks = ['Bitter Murmur', 'Deerstalker', 'Distressing', 'Hex: No One Escapes Death', 'Hex: Thrill of the Hunt', 'Insidious', 'Iron Grasp', 
        'Scourge Hook: Monstrous Shrine', 'Shattered Hope', 'Sloppy Butcher', 'Spies from the Shadows', 'Unrelenting', 'Whispers']
        for killer in selected_killers:
            all_selected_perks.extend(killer.killer_perks)
        
        print("\nYou have the following perks: ")
        for perk in all_selected_perks:
            print(f'- {perk}')
            
    except IndexError:
        print("One or more selected killers are out of range. Please try again.")


def randomize_killer_perks():
    if len(all_selected_perks) > 4:
        randomized_perks = random.sample(all_selected_perks, 4)
    else:
        randomized_perks = all_selected_perks
    print(f'\nRandomized perks: {randomized_perks}')
