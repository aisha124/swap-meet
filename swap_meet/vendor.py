from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory

        if self.inventory is None:
            self.inventory = []
    
    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return self.item

    def remove(self, item):
        self.item = item
        if self.item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return self.item

    
    def get_by_category(self, category):
        # return [item for item in self.inventory if item.category == category]
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, friend, my_item, their_item):
        self.friend = friend
        self.my_item = my_item
        self.their_item = their_item
        
        if self.their_item not in friend.inventory or self.my_item not in self.inventory:
            return False

        if self.my_item:
            friend.inventory.append(my_item)
            self.inventory.remove(my_item)
        
        if self.their_item:
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            return True
        
    def swap_first_item(self, friend):
        self.friend = friend
        
        if len(friend.inventory)==0 or len(self.inventory)==0 :
            return False
        
        self_item = self.inventory.pop(0)
        friend.inventory.append(self_item)

        friend_item= friend.inventory.pop(0)
        self.inventory.append(friend_item)

        return True






# in Wave 4 we will write one method, `swap_first_item`.

# - Instances of `Vendor` have an instance method named `swap_first_item`
#   - It takes one argument: an instance of another `Vendor`, representing the friend that the vendor is swapping with
#   - This method considers the first item in the instance's `inventory`, and the first item in the friend's `inventory`
#   - It removes the first item from its `inventory`, and adds the friend's first item
#   - It removes the first item from the friend's `inventory`, and adds the instances first item
#   - It returns `True`
#   - If either itself or the friend have an empty `inventory`, the method returns `False`