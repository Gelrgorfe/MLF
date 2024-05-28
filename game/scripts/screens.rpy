screen Map():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "map.png" 
        for q in Places:    # affected by script.rpy (label variables: ... )
            if q.Active:
                imagebutton:
                    auto "map_"+q.name+"_%s.png"
                    xpos q.x
                    ypos q.y
                    action SetVariable("LocationID", q.ID), Return(q.name)
                    focus_mask True
                    hovered [Play("sound", "audio/click.wav")]
                    # label variables in script.rpy also affects this
        imagebutton auto "armourer_%s.png" xpos 660 ypos 170 focus_mask True action Jump("Armourer") hovered [Play("sound", "audio/click.wav")]
        imagebutton auto "monastery_%s.png" xpos 1020 ypos 590 focus_mask True action Jump("Monastery") hovered [Play("sound", "audio/click.wav")]
        imagebutton auto "potionmaker_%s.png" xpos 680 ypos 650 focus_mask True action Jump("Potionmaker") hovered [Play("sound", "audio/click.wav")]
        imagebutton auto "tavern_%s.png" xpos 750 ypos 380 focus_mask True action Jump("Tavern") hovered [Play("sound", "audio/click.wav")]
        imagebutton auto "weaponsmith_%s.png" xpos 1080 ypos 310 focus_mask True action Jump("Weaponsmith") hovered [Play("sound", "audio/click.wav")]
        imagebutton auto "forest_%s.png" xpos 120 ypos 70 focus_mask True action Jump("Forest") hovered [Play("sound", "audio/click.wav")]
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "returnicon_%s.png"
        hovered [Play("sound", "audio/click.wav")]
        action Return()

screen statsbutton:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "statsicon_%s.png"
        hovered [Play("sound", "audio/click.wav")]
        action ShowMenu("currentstats")


screen currentstats:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "returnicon_%s.png"
        hovered [Play("sound", "audio/click.wav")]
        action Return()
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 30

            vbox:
                spacing 10
                text "Strength" size 40
                text "Dexterity" size 40
                text "Constitution" size 40
                text "Intelligence" size 40
                text "Wisdom" size 40
                text "Charisma" size 40
            vbox:
                spacing 10
                text "[stats['strength']]" size 40
                text "[stats['dexterity']]" size 40
                text "[stats['constitution']]" size 40
                text "[stats['intelligence']]" size 40
                text "[stats['wisdom']]" size 40
                text "[stats['charisma']]" size 40
screen mapbutton:
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        auto "mapicon_%s.png"
        hovered [Play("sound", "audio/click.wav")]
        action ShowMenu("Map")

screen timebutton():
    text "Day:[clock.day], [clock.weekday], [clock.time]" xalign 0.5 yalign 0.0


screen Sublocations():
    frame:
        xalign 0.0
        yalign 0.0
        vbox:
            for q in Locations:
                if q.parent == LocationID:
                    text q.name
