label rollback:
    # Roll back to the previous label
    return
label Home:
    screen home
    menu:
        "Corridor":
            jump corridor
        "Your Room":
            jump mcroom
        "Kitchen":
            jump Kitchen
        "Return":
            return
    pause
    jump test2
    return

label Mall:
    scene mall
    menu:
        "Sweets":
            jump sweets
        "Electronics":
            jump electronics
        "Cafe":
            jump cafe
    pause
    jump test2
    return
label Park:
    scene park
    menu:
        "Bench":
            jump bench
        "Big Tree":
            jump bigtree
        "Ice Cream Stand":
            jump icecream
    pause
    jump test2
    return
label School:
    scene school
    menu:
        "Corridor":
            jump corridor
        "Classroom":
            jump classroom
        "Nurse Office":
            jump nurse
        "Principal Office":
            jump principal
    pause
    jump test2
    return