init python:
    class Place(object):
        def __init__(self, ID, x, y, name, Active):
            self.ID = ID
            self.x = x
            self.y = y
            self.name = name
            self.Active = Active
    
    @property 
    def rooms(self):
        outlist = []
        for q in Locations:
            if q.parent == self.ID:
                outlist.append(q.ID)
        return outlist
    
    class SubPlace(object):
        def __init__(self, ID, parent, name, Active):
            self.ID = ID
            self.parent = parent
            self.name = name
            self.Active = Active

        
    Places = []
    Locations = []

    t = 0
    while t < 69:
        Places.append(Place(t, 0, 0, "", False))
        Locations.append(SubPlace(t, -1, "", False))
        t += 1