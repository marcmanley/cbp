# this is a test doc

sampleList = [1, 2, 3, 4, 5]
print("Here's our initial list:")
print(sampleList)

# using type to print a data type's type

print(type(sampleList))

# using sum

theTotalSum = sum(sampleList)
print("Here's the sum of that list:")
print(theTotalSum)
print("That's the way you do it!")

# how to .append

sampleList.append(6)
print("Here's our updated list:")
print(sampleList)
theTotalSum = sum(sampleList)
print("Here's our new total:")
print(theTotalSum)
print(sampleList)
sampleList.append(7)
print("We've APPENDED #7 into our list:")
print(sampleList)

# how to .insert

sampleList.insert(7,8)
print("We've also INSERTED 7 and 8 into our list:")
print(sampleList)
theTotalSum = sum(sampleList)
print("The new list:")
print(sampleList)
print("The new sum:")
print(theTotalSum)

# how to .remove

sampleList.remove(8)
print("We've now REMOVED #8 from the list. Our new total is now:")
theTotalSum = sum(sampleList)
print(theTotalSum)

# how to .reverse

sampleList.reverse() #gonna switch things up
print("So now we're gonna switch things up with REVERSE:")
print(sampleList)
print("Here's a list of fruits in our basket:")
fruitBasket2 = ['apples', 'mangos', 'pears', 'peaches', 'bananas']
print(fruitBasket2)
print("What kind of data type is fruitBasket2?")
print(type(fruitBasket2))
print("It's a LIST.")
print("Can we reverse this list?")
fruitBasket2.reverse()
print(fruitBasket2)
print("Sure looks like it.")
print("Can we reverse back?")
fruitBasket2.reverse()
print(fruitBasket2)
print("Sure looks like it.")

# how to print a variable's name and not not its value

theData = { 'thePlace' : 'right here',
'theTime' : 'right now' }
for item in theData.items():
    print('%s = %s' %item)
print(type(theData))
fruitDict1 = { 'redFruit' : 'apples', 'yellowFruit' : 'bananas',
'greenFruit' : 'pears', 'pinkFruit' : 'peaches'}
for item in fruitDict1.items():
    print('%s = %s' %item)
print(type(fruitDict1))

# [ dictionaries ]

calories = { 'apples' : 52, 'bananas' : 89, 'pears' : 75 }
c = calories
print("Here we have some fruits and their calories:")
print(c)
print("Apples have less calories than pears: t/f?", c['apples'] < c['pears'])
print("I wonder if bananas have fewer calories than pears ... t/f?", c['bananas'] < c['pears'])
print("Of course it's",c['bananas'] < c['pears'],". That's because bananas have", c['bananas'], "calories.")

# Classes

class Dog:
    """ Blueprint of a dog """

    # class variable
    # for all instances
    species = ["canis lupus"]

    def __init__(self, n, c):
        self.name = n
        self.state = "sleeping"
        self.color = c

    def command(self, x):
        if x == self.name:
            self.bark(2)
        elif x == "sit":
            self.state = "wag tail"

    def bark(self, freq):
        for i in range(freq):
            print(self.name + ": Woof!")

bello = Dog("bello", "black")
alice = Dog("alice", "white")

print(bello.color) # black
print(alice.color) # white

bello.bark(1) # bello: Woof!

alice.command("sit")
print("alice: " + alice.state)
# alice: switch
bello.command("no")
print("bello: " + bello.state)
# bello: wag tail

alice.command("alice")
# alice: Woof!
# alice: Woof!

bello.species += ["wulf"]
print(len(bello.species)
    == len(alice.species))
# True (!)
