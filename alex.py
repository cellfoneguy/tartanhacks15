import time

class Item(object):
	
	def __init__(self,name,wantedBy,boughtBy=None):
		self.name = name
		self.price = None
		self.wantedBy = wantedBy
		self.boughtBy = boughtBy
		
	def get_price(self):
		return "$%0.2f" % self.price

	def get_boughtBy(self):
		return self.boughtBy.name

	def get_wantedBy(self):
		return self.wantedBy

class User(object):
	def __init__(self,name,friends=[],cart=[]):
		self.name = name
		self.friends = friends
		self.cart = cart
		self.debts = {}

	def update_debts(self):
		for friend in self.friends:
			if friend not in self.debts:
				self.debts[friend] = 0

	def befriend(self,other):
		if self in other.friends or other in self.friends:
			print "You are already friends with %s!" %other.name
			return
		self.friends.append(other)
		other.friends.append(self)
		self.update_debts()
		other.update_debts()

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
		for friend in self.debts:
			printed_dict[friend.name] = self.debts[friend]
		return printed_dict
		
	def add_item(self,item):
		self.wishlist.append(item)
		self.update_wantedBy(self.wishlist)
		return "Added %s to wishlist!" %item.name

	def update_wantedBy(self,wishlist):
		for item in self.wishlist:
			if self.name not in item.wantedBy:
				item.wantedBy.append(self.name)
		
	def remove_item(self,item):
		self.wishlist.remove(item)
		item.wantedBy.remove(self.name)
		return "Removed %s from wishlist!" %item.name
		
	def buy_item_for_self(self,item,price,date):
		self.wishlist.remove(item)
		item.date_purchased = time.time()
		item.boughtBy = self.name
		item.date_purchased = date
		item.price = price
		item.wantedBy.remove(self.name)

	def buy_item_for_other(self,item,friend,price,date):
		if item not in friend.wishlist:
			print "%s did not want this item!!!" %friend.name
			
		try:
			friend.wishlist.remove(item)
		except:
			pass
		item.date_purchased = date
		item.boughtBy = self
		item.price = price
		friend.debts[self] += item.price
		
	def who_you_owe(self):
		result = ""
		for friend in self.debts:
			money_owed = self.debts[friend]
			result += "You owe %s $%0.2f" %(friend.name,money_owed)
			result += "\n"
		return result

	def do_you_owe(self):
		for friend in self.debts:
			money_owed = self.debts[friend]
			if money_owed != 0:
				return False
		return True

	def who_owes_you(self):
		result = ""
		for friend in self.friends:
			their_dict = friend.debts
			if self in friend.debts:
				money_owed = friend.debts[self]
				result += "%s owes you $%0.2f" %(friend.name,money_owed)
			result += "\n"
		return result
			
	def pay_person(self,target,amount):
		return
	
	def pay_all(self):
		return

class Group(object):
	
	def __init__(self):
		self.number = 0 #member count
		self.members = []
		self.groupCart = {} #{name:[items]}
		
	def add_member(self,user):
		self.number += 1
		self.members.append(user)
		self.groupCart[user.name]=user.wishlist
		return user.name + "was added!"
	
	def remove_member(self,user):
		self.number -= 1
		self.members.remove(user)
		for item in user.wishlist:
			groupCart.remove(item)
		return user.name + "was removed!"
	
	def get_names(self):
		names = []
		for member in self.members:
			names.append(member.name)
		return names
	
	def get_number(self):
		return self.number

	def get_groupCart(self):
		return self.groupCart

	def group_simplify(self):
		end = len(self.members)
		for index1 in xrange(end):
			for index2 in xrange(index1+1,end):
				friend1 = self.members[index1]
				friend2 = self.members[index2]
				

	
#users, friends and family
print 'users, friends and family'
paul = User('paul',[],[])
kishan = User('kishan',[],[])
doowon = User('doowon',[],[])
alex = User('alex',[],[])

paul.befriend(kishan)
paul.befriend(doowon)
paul.befriend(alex)
doowon.befriend(alex)
doowon.befriend(kishan)
kishan.befriend(alex)

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
print 'adding items to wishlist'
eggs = Item('eggs','6 eggs',[])
meat = Item('meat','1 large chicken yo',[])
coke = Item('coke','1 liter of coke',[])

print coke.get_description()

paul.add_item(eggs)
paul.add_item(meat)
paul.add_item(coke)
doowon.add_item(coke)
kishan.add_item(meat)
alex.add_item(eggs)

print paul.get_wishlist()
print doowon.get_wishlist()
print kishan.get_wishlist()
print alex.get_wishlist()

print eggs.get_wantedBy()
print meat.get_wantedBy()
print coke.get_wantedBy()
print

#changing items
print 'changing items'

paul.remove_item(coke)
kishan.add_item(coke)
alex.add_item(coke)

print paul.get_wishlist()
print doowon.get_wishlist()
print kishan.get_wishlist()
print alex.get_wishlist()

print eggs.get_wantedBy()
print meat.get_wantedBy()
print coke.get_wantedBy()
print

#checking the dictionary
print 'checking the dictionary'

print paul.print_dict()
print doowon.print_dict()
print kishan.print_dict()
print alex.print_dict()
print


#buying items
today = '7 Feb 2015'
print 'buying items'

print paul.get_wishlist()
print doowon.get_wishlist()
print kishan.get_wishlist()
print alex.get_wishlist()
print

paul.buy_item_for_self(eggs,2,today)

print paul.get_wishlist()
print paul.print_dict()
print doowon.print_dict()
print eggs.get_wantedBy()

paul.buy_item_for_other(coke,doowon,1.5,today)
paul.buy_item_for_other(coke,doowon,1.5,today)
paul.buy_item_for_other(eggs,alex,2,today)
paul.buy_item_for_other(eggs,kishan,2,today)
paul.buy_item_for_other(coke,alex,1.5,today)

print paul.get_wishlist()
print doowon.get_wishlist()
print kishan.get_wishlist()
print alex.get_wishlist()
print
print paul.print_dict()
print doowon.print_dict()
print kishan.print_dict()
print alex.print_dict()

alex.buy_item_for_other(meat,kishan,5,today)
alex.buy_item_for_other(coke,kishan,1.5,today)
alex.buy_item_for_other(meat,paul,5,today)

print paul.get_wishlist()
print doowon.get_wishlist()
print kishan.get_wishlist()
print alex.get_wishlist()
print
print paul.print_dict()
print doowon.print_dict()
print kishan.print_dict()
print alex.print_dict()
print

print coke.get_date()
print coke.get_boughtBy()
print

#checking money
print 'checking money'

print 'paul'
print paul.who_you_owe()
print paul.who_owes_you()
print 'doowon'
print doowon.who_you_owe()
print doowon.who_owes_you()
print 'kishan'
print kishan.who_you_owe()
print kishan.who_owes_you()
print 'alex'
print alex.who_you_owe()
print alex.who_owes_you()

print eggs.get_price()
print coke.get_price()
print meat.get_price()



	
