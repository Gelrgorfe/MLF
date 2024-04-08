screen Map():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "map.png" 
        # for q in Places:
        #     if q.Active:
        #         imagebutton:
        #             auto "map_"+q.name+"_%s.png"
        #             xpos q.x
        #             ypos q.y
        #             action SetVariable("LocationID", q.ID), Return(q.name)
        #             focus_mask True
        #             hovered [Play("sound", "audio/click.wav")]
        # imagebutton auto "map_home_%s.png" xpos 207 ypos 205 focus_mask True action Jump("Home") hovered [Play("sound", "audio/click.wav")]
        # imagebutton auto "map_mall_%s.png" xpos 379 ypos 592 focus_mask True action Jump("Mall") hovered [Play("sound", "audio/click.wav")]
        # imagebutton auto "map_park_%s.png" xpos 903 ypos 613 focus_mask True action Jump("Park") hovered [Play("sound", "audio/click.wav")]
        # imagebutton auto "map_school_%s.png" xpos 1328 ypos 633 focus_mask True action Jump("School") hovered [Play("sound", "audio/click.wav")]
        # |  xpos 217 ypos 209 Home    |  xpos 207 ypos 205   |
        # |  xpos 386 ypos 594 Mall    |  xpos 379 ypos 592   |
        # |  xpos 912 ypos 620 Park    |  xpos 903 ypos 613   |
        # |  xpos 1337 ypos 640 School |  xpos 1328 ypos 633  |
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "return_%s.png"
        hovered [Play("sound", "audio/click.wav")]
        action Return()

screen statsbutton:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "statsbutton_%s.png"
        hovered [Play("sound", "audio/click.wav")]
        action ShowMenu("currentstats")


screen currentstats:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "return_%s.png"
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
                text "Twilight Sparkle affection" size 40
                text "Pinkie Pie affection" size 40
                text "Fluttershy affection" size 40
                text "Rainbow Dash affection" size 40
                text "Rarity affection" size 40
                text "Applejack affection" size 40
            vbox:
                spacing 10
                text "[pony_affection[twilight]]" size 40
                text "[pony_affection[pinkie]]" size 40
                text "[pony_affection[fluttershy]]" size 40
                text "[pony_affection[rainbow]]" size 40
                text "[pony_affection[rarity]]" size 40
                text "[pony_affection[applejack]]" size 40

screen mapbutton:
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        auto "mapbutton_%s.png"
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
