define lorelei = Character("Lorelei")
define forg = Character("Forg")
define knight = Character("Artaanel")

label start:
    call variables from _call_variables 
    $ Running = True
    while Running:
        play music 'audio/muzyka.mp3'
        show screen statsbutton
        show screen mapbutton
        show screen timebutton
        $ clock
        jump startgry
    return

label startgry:
    scene beginning
    $ player_name = renpy.input("What was my name? (default name is maksik)")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="maksik"
  
    player_name "Right, my name is %(player_name)s!"
    player_name "Well I guess I should go and see why they wanted such a great adventurer as me in this disgusting little town"
    # call screen Map
    $ clock.advance()
    jump test2
    return


label test2:
    
    scene tavern
    show mc at left
    show lorelei at right
    lorelei "Lorem ipsum"
    player_name "-------------"
    show mc_golden at left
    player_name "----------------"
    hide mc_golden
    player_name "----------------"
    hide lorelei
    show forg at right
    forg "Lorem ipsum"
    hide forg
    show knight at right
    knight "Lorem ipsum"
    hide knight

    "Once you add a story, pictures, and music, you can release it to the world!"
    $ clock.advance()
    jump day1

    return

label variables:
    # $ Places = [Place(i, x, y, name, True) for i, (x, y, name) in enumerate([(207, 205, "Home"), (379, 592, "Mall"), (903, 613, "Park"), (1328, 633, "School")])]
    # $ Locations = [SubPlace(i, LocationID, name, True) for i, name in enumerate(["Armourer", "Monastery", "Potionmaker", "Tavern", "Weaponsmith", "Forest"])]
    return
