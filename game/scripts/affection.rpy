default pony_affection = {
    "twilight": 0,
    "pinkie": 0,
    "fluttershy": 0,
    "rainbow": 0,
    "rarity": 0,
    "applejack": 0
}

label increase_affection(pony):
    $ pony_affection[pony] += 1

label decrease_affection(pony):
    $ pony_affection[pony] -= 1

# $ renpy.call("increase_affection", "twilight")
# $ renpy.call("decrease_affection", "pinkie")
    