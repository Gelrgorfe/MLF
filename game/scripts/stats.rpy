default stats = {
    "strength": 30,
    "dexterity": 20,
    "constitution": 80,
    "intelligence": 100,
    "wisdom": 100,
    "charisma": 7
}

label increase_stat(stat):
    $ stats[stat] += 1

label decrease_stat(stat):
    $ stats[stat] -= 1

# $ renpy.call("increase_stat", "strength")
# $ renpy.call("decrease_stat", "intelligence")
    
