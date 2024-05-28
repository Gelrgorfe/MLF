# enemy can't have negative hp
# contunue action after defeating the enemy

init python:
    import random

    class Enemy:
        def __init__(self, name, hp, strength, accuracy, pic):
            self.name = name
            self.hp = hp
            self.strength = strength
            self.accuracy = accuracy
            self.pic = pic

    opponents = [
        Enemy("Enemy1", 50, 4, 90, "Enemy_1.png"),
        Enemy("Enemy2", 70, 6, 90, "Enemy_2.png"),
        Enemy("Enemy3", 100, 8, 90, "Enemy_3.png"),
        Enemy("Enemy4", 120, 10, 90, "Enemy_4.png"),
        Enemy("Enemy5", 60, 10, 90, "Enemy_5.png")
    ]

label forest_event:
    if random.randint(1, 100) <= 15:
        call encounter_enemy
    else:
        "The forest is quiet, maybe even too quiet."
        return

label encounter_enemy:
    $ current_opponent = random.choice(opponents)
    "You encounter a [current_opponent.name]!"
    call start_battle
    return

label start_battle:
    $ player_defense_bonus = 0
    $ potion_heal_amount = 30
    $ max_defense_bonus = 50
    $ strength = stats["strength"]
    $ dexterity = stats["dexterity"]
    $ constitution = stats["constitution"]
    $ max_health = stats["constitution"]

    $ enemy_hp = current_opponent.hp
    $ enemy_strength = current_opponent.strength
    $ enemy_accuracy = current_opponent.accuracy
    $ enemy_picture = current_opponent.pic
    
    jump combat


label combat:
    show expression enemy_picture
    while constitution > 0 and enemy_hp > 0:
        menu:
            "Light attack":
                jump light_attack
            "Hard attack":
                jump hard_attack
            "Dodge (decrease chance of getting hit, can stack)":
                jump dodge
            "Drink a potion":
                jump drink_potion
    jump start_battle

label light_attack:
    if random.randint(1, 100) <= dexterity * 2:
        $ damage = int(strength * 0.5)
        $ enemy_hp -= damage
        "You dealt [damage] damage! The enemy now has [enemy_hp] hp left."
    else:
        "You missed."
    jump enemy_turn

label hard_attack:
    if random.randint(1, 100) <= dexterity:
        $ damage = strength
        $ enemy_hp -= damage
        "You dealt [damage] damage! The enemy now has [enemy_hp] hp left."
    else:
        "You missed."
    jump enemy_turn

label dodge:
    $ player_defense_bonus = min(player_defense_bonus + 5, max_defense_bonus)
    "Dodge increased. Chance to dodge increased by 5 percent."
    jump enemy_turn

label drink_potion:
    $ constitution = min(constitution + potion_heal_amount, max_health)
    "Well you gained some health. You now have [constitution] hp."
    jump enemy_turn

label enemy_turn:
    if enemy_hp > 0:
        if random.randint(1, 100) <= enemy_accuracy - player_defense_bonus:
            $ damage = int(enemy_strength * 1.2)
            $ constitution -= damage
            "[current_opponent.name] dealt [damage] damage to you!... how preposterous. You have [constitution] hp left."
        else:
            "[current_opponent.name] missed. As it should be"
    
    if constitution <= 0:
        hide enemy_picture
        "You lost... gg"
    elif enemy_hp <= 0:
        "Not much of a challenge, innit?"
        hide enemy_picture
        player_name "The forest seems darker than before..."
    else:
        jump combat
    return
