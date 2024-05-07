define lorelei = Character("Lorelei")
define forg = Character("Forg")
define knight = Character("Artaanel")
default location = "Home"
default subplace = "Classroom"
default LocationID = 3

label start:
    call variables 
    $ Running = True
    while Running:
        $ clock
        $ location_img = location.lower()
        $ subplace_img = subplace.lower()
        if renpy.has_image(location_img, exact=True):
            scene expression location_img
            show screen statsbutton
            show screen mapbutton
            show screen timebutton
        jump startgry
    return
label startgry:
    
    "Where the fuck am I"


    $ player_name = renpy.input("What was my name? (default name is maksik)")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="maksik"
  
    player_name "Right, my name is %(player_name)s!"
    $ clock.advance()
    jump test2
    return


label test2:
    
    scene classroom
    show twilight happy
    
    # twilight "*sneezes*"
    # menu:
    #     "*give her handkerchief*":
    #         jump normal_route
    #     "O mało ci ryja nie urwało":
    #         call twilight_affection_decreased
    #         jump retard_route

    

    "Once you add a story, pictures, and music, you can release it to the world!"
    pause

    return

label variables:
    $ Places = [Place(i, x, y, name, True) for i, (x, y, name) in enumerate([(207, 205, "Home"), (379, 592, "Mall"), (903, 613, "Park"), (1328, 633, "School")])]
    $ Locations = [SubPlace(i, LocationID, name, True) for i, name in enumerate(["Hall", "Classroom", "Toilet", "Roof"])]
    return
