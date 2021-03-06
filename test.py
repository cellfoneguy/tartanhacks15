import time

class Group(object):
    
    def __init__(self):
        self.number = 0
        self.members = []
        self.group_wishlist = []
        
    def add_member(self,user):
        self.number += 1
        self.members.append(user)
        self.group_wishlist.append(user.wishlist)
        return user.name + "was added!"
    
    def remove_member(self,user):
        self.number -= 1
        self.members.remove(user)
        for item in user.wishlist:
            group_wishlist.remove(item)
        return user.name + "was removed!"
    
    def get_names(self):
        names = []
        for member in self.members:
            names.append(member.name)
        return names
    
    def get_number(self):
        return self.number

    def get_group_wishlist(self):
        return self.group_wishlist

class User(object):
    
    def __init__(self,name,friends=[],wishlist=[]):
        self.name = name
        self.friends = friends
        self.wishlist = wishlist
        self.friends_and_money = dict()

    def update_friends_and_money(self):
        for friend in self.friends:
            if friend not in self.friends_and_money:
                self.friends_and_money[friend] = 0

    def befriend(self,other):
        if self in other.friends or other in self.friends:
            print "You are already friends with %s!" %other.name
            return
        self.friends.append(other)
        other.friends.append(self)
        self.update_friends_and_money()
        other.update_friends_and_money()

    def get_name(self):
        return self.name

    def get_friends(self):
        names = []
        for member in self.friends:
            names.append(member.name)
        return names

    def get_wishlist(self):
        items = []
        for item in self.wishlist:
            items.append(item.name)
        return items

    def print_dict(self):
        printed_dict = {}
        for friend in self.friends_and_money:
            printed_dict[friend.name] = self.friends_and_money[friend]
        return printed_dict
        
    def add_item(self,item):
        self.wishlist.append(item)
        self.update_wanted_by(self.wishlist)
        return "Added %s to wishlist!" %item.name

    def update_wanted_by(self,wishlist):
        for item in self.wishlist:
            if self.name not in item.wanted_by:
                item.wanted_by.append(self.name)
        
    def remove_item(self,item):
        self.wishlist.remove(item)
        item.wanted_by.remove(self.name)
        return "Removed %s from wishlist!" %item.name
        
    def buy_item_for_self(self,item):
        self.wishlist.remove(item)
        item.date_purchased = time.time()
        item.purchased_by = self.name

    def buy_item_for_other(self,item,friend):
        if friend.name not in item.wanted_by:
            print "%s did not want this item!!!" %friend.name
            return
        friend.wishlist.remove(item)
        item.date_purchased = time.time()
        item.purchased_by = self
        friend.friends_and_money[self] += item.price
        
    def who_you_owe(self):
        result = ""
        for friend in self.friends_and_money:
            money_owed = self.friends_and_money[friend]
            result += "You owe %s $%0.2f" %(friend, money_owed)
        return result

    def who_owes_you(self):
        result = ""
        for friend in friends:
            their_dict = friend.friends_and_money
            if self.name in friend.friends_and_money:
                money_owed = friend.friends_and_money[self.name]
                result += "%s owes you $%0.2f" %(friend, money_owed)
        return result          
            
    def pay_person(self,target,amount):
        return
    
    def pay_all(self):
        return 

class Item(object):
    
    def __init__(self,name,price,description,wanted_by,
                 date_purchased=None,purchased_by=None):
        self.name = name
        self.price = price
        self.description = description
        self.wanted_by = wanted_by
        self.date_purchased = date_purchased
        self.purchased_by = purchased_by
        
    def get_price(self):
        return "$%0.2f" %self.price
    
    def get_description(self):
        return self.description

    def get_wanted_by(self):
        return self.wanted_by


#users, friends and family
paul = User('paul',[],[])
kishan = User('kishan',[],[])
doowon = User('doowon',[],[])
alex = User('alex',[],[])

paul.befriend(kishan)
paul.befriend(doowon)
doowon.befriend(alex)
alex.befriend(paul)

print paul.get_friends()
print kishan.get_friends()
print doowon.get_friends()
print alex.get_friends()

family = Group()
family.add_member(paul)
family.add_member(kishan)
family.add_member(doowon)
family.add_member(alex)
print family.get_names()
print family.get_number()
print


#adding items to wishlist
eggs = Item('eggs',2,'6 eggs',[])
meat = Item('meat',5,'1 large chicken yo',[])
coke = Item('coke',1.5,'1 liter of coke',[])

print eggs.get_price()
print coke.get_description()

paul.add_item(eggs)
paul.add_item(meat)
paul.add_item(coke)
doowon.add_item(coke)

print paul.get_wishlist()
print doowon.get_wishlist()

print eggs.get_wanted_by()
print meat.get_wanted_by()
print coke.get_wanted_by()

paul.remove_item(coke)
kishan.add_item(coke)

print paul.get_wishlist()
print kishan.get_wishlist()

print eggs.get_wanted_by()
print meat.get_wanted_by()
print coke.get_wanted_by()
print

#checking the dictionary

print paul.print_dict()
print doowon.print_dict()
print kishan.print_dict()
print alex.print_dict()
print


#buying items

paul.buy_item_for_self(eggs)

print paul.get_wishlist()
print paul.print_dict()
print doowon.print_dict()

paul.buy_item_for_other(coke,doowon)

print doowon.get_wishlist()
print paul.print_dict()
print doowon.print_dict()





    


    
