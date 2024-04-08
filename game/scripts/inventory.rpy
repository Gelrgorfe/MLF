init python:
    class Item(object):
        def __init__(self, name, value, weight, owned, item_id):
            self.name = name
            self.value = value
            self.weight = weight
            self.owned = owned
            self.item_id = item_id
            
        def add_item(self):
            max_weight = 25
            current_weight = sum(item.weight * item.owned for item in Inventory)
            if current_weight + self.weight > max_weight:
                return 
            else:
                self.owned += 1
                
    inventory_data = [
        {"name": "lollipop", "value": 2, "weight": 0},
        {"name": "chocolate", "value": 5, "weight": 1},
        {"name": "book", "value": 25, "weight": 2}
    ]

    Inventory = []
    for i, data in enumerate(inventory_data):
        item = Item(data["name"], data["value"], data["weight"], 0, i)
        Inventory.append(item)
        