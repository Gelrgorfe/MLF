label rollback:
    # Roll back to the previous label
    return
label Beginning:
    screen beginning
    pause
    return
screen armourer:
    add "armourer.png"

screen monastery:
    add "monastery.png"

screen potionmaker:
    add "potionmaker.png"

screen tavern:
    add "tavern.png"

screen weaponsmith:
    add "weaponsmith.png"

screen forest:
    add "forest.png"


label Armourer:
    call screen armourer
    menu:
        "Talk":
            jump talk_armourer
        "Return":
            return
    pause
    return

label Monastery:
    call screen monastery
    menu:
        "Talk":
            jump talk_monastery
        "Return":
            return
    pause
    return

label Potionmaker:
    call screen potionmaker
    menu:
        "Talk":
            jump talk_apotionmaker
        "Return":
            return
    pause
    return

label Tavern:
    call screen tavern
    menu:
        "Talk":
            jump talk_tavern
        "Spend some time":
            $ clock.advance()
        "Return":
            return
    pause
    return

label Weaponsmith:
    call screen weaponsmith
    menu:
        "Talk":
            jump talk_weaponsmith
        "Return":
            return
    pause
    return

label Forest:
    call screen forest
    menu:
        "Explore":
            jump explore_forest
        "Return":
            return
    pause
    return


# label Home:
#     screen home
#     menu:
#         "Corridor":
#             jump corridor
#         "Your Room":
#             jump mcroom
#         "Kitchen":
#             jump Kitchen
#         "Return":
#             return
#     pause
#     jump test2
#     return

# label Mall:
#     scene mall
#     menu:
#         "Sweets":
#             jump sweets
#         "Electronics":
#             jump electronics
#         "Cafe":
#             jump cafe
#     pause
#     jump test2
#     return
# label Park:
#     scene park
#     menu:
#         "Bench":
#             jump bench
#         "Big Tree":
#             jump bigtree
#         "Ice Cream Stand":
#             jump icecream
#     pause
#     jump test2
#     return
# label School:
#     scene school
#     menu:
#         "Corridor":
#             jump corridor
#         "Classroom":
#             jump classroom
#         "Nurse Office":
#             jump nurse
#         "Principal Office":
#             jump principal
#     pause
#     jump test2
#     return