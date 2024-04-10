default stats = {
    "strength": 0,
    "dexterity": 0,
    "constitution": 0,
    "intelligence": 0,
    "wisdom": 0,
    "charisma": 0
}

label increase_stat(stat):
    $ stats[stat] += 1

label decrease_stat(stat):
    $ stats[stat] -= 1

# $ renpy.call("increase_stat", "strength")
# $ renpy.call("decrease_stat", "intelligence")
    
