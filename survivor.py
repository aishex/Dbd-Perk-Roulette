import random

class Survivor:
    def __init__(self, survivor_name, survivor_perks):
        self.survivor_name = survivor_name
        self.survivor_perks = survivor_perks
    
    def display_survivor_perks(self):
        print(f'Survivor {self.survivor_name} has the following perks: ')
        print(self.survivor_perks)

dwight = Survivor("Dwight Fairfield", ["Bond", "Prove Thyself", "Leader"])
meg = Survivor("Meg Thomas", ["Adrenaline", "Sprint Burst", "Quick and Quiet"])
claudette = Survivor("Claudette Morel", ["Self-Care", "Empathy", "Botany Knowledge"])
jake = Survivor("Jake Park", ["Iron Will", "Calm Spirit", "Saboteur"])
nea = Survivor("Nea Karlsson", ["Balanced Landing", "Urban Evasion", "Streetwise"])
laurie = Survivor("Laurie Strode", ["Decisive Strike", "Sole Survivor", "Object of Obsession"])
ace = Survivor("Ace Visconti", ["Open Handed", "Up the Ante", "Ace in the Hole"])
bill = Survivor("Bill Overbeck", ["Borrowed Time", "Unbreakable", "Left Behind"])
feng = Survivor("Feng Min", ["Technician", "Lithe", "Alert"])
davidking = Survivor("David King", ["We're Gonna Live Forever", "Dead Hard", "No Mither"])
quentin = Survivor("Quentin Smith", ["Wake Up!", "Pharmacy", "Vigil"])
davidtapp = Survivor("David Tapp", ["Tenacity", "Detective's Hunch", "Stake Out"])
kate = Survivor("Kate Denson", ["Dance With Me", "Windows of Opportunity", "Boil Over"])
adam = Survivor("Adam Francis", ["Diversion", "Deliverance", "Autodidact"])
jeff = Survivor("Jeff Johansen", ["Breakdown", "Distortion", "Aftercare"])
jane = Survivor("Jane Romero", ["Solidarity", "Poised", "Head On"])
ash = Survivor("Ash Williams", ["Flip-Flop", "Buckle Up", "Mettle of Man"])
nancy = Survivor("Nancy Wheeler", ["Better Together", "Fixated", "Inner Strength"])
steve = Survivor("Steve Harrington", ["Babysitter", "Camaraderie", "Second Wind"])
yui = Survivor("Yui Kimura", ["Lucky Break", "Any Means Necessary", "Breakout"])
zarina = Survivor("Zarina Kassir", ["For the People", "Off the Record", "Red Herring"])
cheryl = Survivor("Cheryl Mason", ["Soul Guard", "Blood Pact", "Repressed Alliance"])
felix = Survivor("Felix Richter", ["Visionary", "Desperate Measures", "Built to Last"])
elodie = Survivor("Élodie Rakoto", ["Appraisal", "Deception", "Power Struggle"])
yun = Survivor("Yun-Jin Lee", ["Fast Track", "Smash Hit", "Self-Preservation"])
jill = Survivor("Jill Valentine", ["Counterforce", "Resurgence", "Blast Mine"])
leon = Survivor("Leon Scott Kennedy", ["Bite the Bullet", "Flashbang", "Rookie Spirit"])
mikaela = Survivor("Mikaela Reed", ["Clairvoyance", "Boon: Circle of Healing", "Boon: Shadow Step"])
jonah = Survivor("Jonah Vasquez", ["Overcome", "Corrective Action", "Boon: Exponential"])
yoichi = Survivor("Yoichi Asakawa", ["Parental Guidance", "Empathic Connection", "Boon: Dark Theory"])
haddie = Survivor("Haddie Kaur", ["Inner Focus", "Residual Manifest", "Overzealous"])
ada = Survivor("Ada Wong", ["Wiretap", "Reactive Healing", "Low Profile"])
rebecca = Survivor("Rebecca Chambers", ["Better Than New", "Reassurance", "Hyperfocus"])
vittorio = Survivor("Vittorio Toscano", ["Potential Energy", "Fogwise", "Quick Gambit"])
thalita = Survivor("Thalita Lyra", ["Cut Loose", "Friendly Competition", "Teamwork: Power of Two"])
renato = Survivor("Renato Lyra", ["Blood Rush", "Background Player", "Teamwork: Collective Stealth"])
gabriel = Survivor("Gabriel Soma", ["Troubleshooter", "Scavenger", "Made for This"])
nicolas = Survivor("Nicolas Cage", ["Dramaturgy", "Scene Partner", "Plot Twist"])
ellen = Survivor("Ellen Ripley", ["Lucky Star", "Chemical Trap", "Light Footed"])
alan = Survivor("Alan Wake", ["Heavy Rain", "Overdrive", "Low Visibility"])
sable = Survivor("Sable Ward", ["Nimble Steps", "Antique Charm", "Herbal Remedy"])
troupe = Survivor("The Troupe", ["Collaborative Spirits", "Inspiring Encore", "Nomadic Unity"])
lara = Survivor("Lara Croft", ["Tomb Raider", "Survival Instinct", "Artifact Mastery"])
trevor = Survivor("Trevor Belmont", ["Vampire Slayer", "Whip Master", "Family Legacy"])

def choose_survivor():
    
    global all_selected_perks
    
    all_survivors = [
        dwight, meg, claudette, jake, nea, laurie, ace, bill, feng, davidking, quentin, davidtapp, kate, adam, jeff, jane, ash, nancy, 
        steve, yui, zarina, cheryl, felix, elodie, yun, jill, leon, mikaela, jonah, yoichi, haddie, ada, rebecca, vittorio, thalita, 
        renato, gabriel, nicolas, ellen, alan, sable, troupe, lara, trevor
    ]
    
    print('Available survivors: ')
    for i, survivor in enumerate(all_survivors, 1):
        print(f'{i}. {survivor.survivor_name}')
    
    your_survivors_input = input('Select the survivors by number (comma-separated): ')
    your_survivors_str = your_survivors_input.split(',')
    your_survivors = [int(survivor.strip()) for survivor in your_survivors_str]
    
    try:
        selected_survivors = [all_survivors[survivor - 1] for survivor in your_survivors]
        print(f'Selected survivors: {", ".join(s.survivor_name for s in selected_survivors)}')
        
        all_selected_perks = ['Dark sense', 'Déjà Vu', 'Hope', 'Kindred', 'Lightweight', 'No One Left Behind',
        "Plunderer's Instinct", 'Premonition', 'Resilience', 'Slippery Meat', 'Small Game', 'Spine Chill',
        'This Is Not Happening', "We'll Make It"]
        
        for survivor in selected_survivors:
            all_selected_perks.extend(survivor.survivor_perks)
        
        print("\nYou have the following perks: ")
        for perk in all_selected_perks:
            print(f'- {perk}')
            
    except IndexError:
        print("One or more selected killers are out of range. Please try again.")


def randomize_survivor_perks():
    if len(all_selected_perks) > 4:
        randomized_perks = random.sample(all_selected_perks, 4)
    else:
        randomized_perks = all_selected_perks
    print(f'\nRandomized perks: {randomized_perks}')

