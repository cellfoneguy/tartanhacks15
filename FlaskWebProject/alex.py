import time

class Item(object):
	
	def __init__(self,name,wantedBy=[],boughtBy=None):
		self.name = name
		self.price = None
		self.wantedBy = wantedBy
		self.boughtBy = boughtBy
		
	def getPrice(self):
		return "$%0.2f" % self.price

	def getBoughtBy(self):
		return self.boughtBy.name

	def getWantedBy(self):
		return self.wantedBy

class User(object):
	def __init__(self,name,friends=[],cart=[]):
		self.name = name
		self.friends = friends
		self.cart = cart
		self.debts = {}

	def __str__(self):
		return self.name

	def updateDebts(self): #add a new friend to debt lists
		for friend in self.friends:
			if friend not in self.debts:
				self.debts[friend] = 0

	def befriend(self,other): #made a friend!
		if self in other.friends or other in self.friends:
			print "You are already friends with %s!" % other.name
		else:
			self.friends.append(other)
			other.friends.append(self)
			self.updateDebts()
			other.updateDebts()

	def getName(self): #user's name
		return self.name

	def getFriends(self): #returns list of friends
		return self.friends

	def getCart(self):
		items = []
		for item in self.cart:
			items.append(item)
		return items

	def addItem(self,item): #add
		self.cart.append(item)
		self.updateWantedBy()
		return "Added %s to cart!" % item.name

	def updateWantedBy(self): #update group cart
		for item in self.cart:
			if self not in item.wantedBy:
				item.wantedBy.append(self)
		
	def removeItem(self,item):
		self.cart.remove(item)
		item.wantedBy.remove(self)
		return "Removed %s from cart!" % item
		
	def buyForSelf(self,item,price):
		self.cart.remove(item)
		item.boughtBy = self
		item.price = price
		item.wantedBy.remove(self)

	def buyForOther(self,item,friend,price): #buying for other
		if item in friend.cart:
			friend.cart.remove(item)
			item.boughtBy = self
			item.price = price
			friend.debts[self] += item.price
		else:
			print "%s did not want this item!!!" % friend.name

	def whoYouOwe(self): #returns debts you owe on a line
		result = ""
		for friend in self.debts:
			owed = self.debts[friend]
			result += "You owe %s $%0.2f" % (friend,owed)
			result += "\n"
		return result

	def doYouOwe(self): #returns boolean: if you owe any money
		for friend in self.debts:
			owed = self.debts[friend]
			if owed != 0:
				return False
		return True

	def whoOwesYou(self): #returns who owes you rn
		result = ""
		for friend in self.friends:
			if self in friend.debts:
				owed = friend.debts[self]
				result += "%s owes you $%0.2f" % (friend.name,owed)
				result += "\n"
		return result

class Group(object):
	
	def __init__(self):
		self.number = 0 #member count
		self.members = []
		self.groupCart = {} #{name:[items]}
		
	def addMember(self,user): #add member to fleet pls
		self.number += 1
		self.members.append(user)
		self.groupCart[user]=user.cart
		return user.name + "was added!"
	
	def removeMember(self,user): #possible overlap?
		self.number -= 1
		self.members.remove(user)
		for item in user.cart:
			groupCart.remove(item)
		return user + "was removed!"
	
	def getNames(self): #gets names of members
		names = []
		for member in self.members:
			names.append(member)
		return names
	
	def getNumber(self): #returns #
		return self.number

	def get_groupCart(self):
		return self.groupCart

	def group_simplify(self): #simplification code
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

print paul.getFriends()
print kishan.getFriends()
print doowon.getFriends()
print alex.getFriends()

family = Group()
family.addMember(paul)
family.addMember(kishan)
family.addMember(doowon)
family.addMember(alex)
print family.getNames()
print family.getNumber()
print


#adding items to wishlist
print 'adding items to wishlist'
eggs = Item('eggs',[])
meat = Item('meat',[])
coke = Item('coke',[])

paul.addItem(eggs)
paul.addItem(meat)
paul.addItem(coke)
doowon.addItem(coke)
kishan.addItem(meat)
alex.addItem(eggs)

print paul.getCart()
print doowon.getCart()
print kishan.getCart()
print alex.getCart()

print eggs.getWantedBy()
print meat.getWantedBy()
print coke.getWantedBy()
print

#changing items
print 'changing items'

paul.removeItem(coke)
kishan.addItem(coke)
alex.addItem(coke)

print paul.getCart()
print doowon.getCart()
print kishan.getCart()
print alex.getCart()

print eggs.getWantedBy()
print meat.getWantedBy()
print coke.getWantedBy()
print

#checking the dictionary
print 'checking the dictionary'

print paul.debts
print doowon.debts
print kishan.debts
print alex.debts
print


#buying items
today = '7 Feb 2015'
print 'buying items'

print paul.getCart()
print doowon.getCart()
print kishan.getCart()
print alex.getCart()
print

paul.buyForSelf(eggs,2)

print paul.getCart()
print paul.debts
print doowon.debts
print eggs.getWantedBy()

paul.buyForOther(coke,doowon,1.5)
paul.buyForOther(coke,doowon,1.5)
paul.buyForOther(eggs,alex,2)
paul.buyForOther(eggs,kishan,2)
paul.buyForOther(coke,alex,1.5)

print paul.getCart()
print doowon.getCart()
print kishan.getCart()
print alex.getCart()
print
print paul.debts
print doowon.debts
print kishan.debts
print alex.debts

alex.buyForOther(meat,kishan,5)
alex.buyForOther(coke,kishan,1.5)
alex.buyForOther(meat,paul,5)

print paul.getCart()
print doowon.getCart()
print kishan.getCart()
print alex.getCart()
print
print paul.debts
print doowon.debts
print kishan.debts
print alex.debts
print

print coke.getBoughtBy()
print

#checking money
print 'checking money'

print 'paul'
print paul.whoYouOwe()
print paul.whoOwesYou()
print 'doowon'
print doowon.whoYouOwe()
print doowon.whoOwesYou()
print 'kishan'
print kishan.whoYouOwe()
print kishan.whoOwesYou()
print 'alex'
print alex.whoYouOwe()
print alex.whoOwesYou()

print eggs.getPrice()
print coke.getPrice()
print meat.getPrice()



	
