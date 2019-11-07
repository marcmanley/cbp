# this is a test doc

sampleList = [1, 2, 3, 4, 5]
print("Here's our initial list:")
print(sampleList)
print(type(sampleList))
theTotalSum = sum(sampleList)
print("Here's the sum of that list:")
print(theTotalSum)
print("That's the way you do it!")
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
sampleList.insert(7,8)
print("We've also INSERTED 7 and 8 into our list:")
print(sampleList)
theTotalSum = sum(sampleList)
print("The new list:")
print(sampleList)
print("The new sum:")
print(theTotalSum)
sampleList.remove(8)
print("We've now REMOVED #8 from the list. Our new total is now:")
theTotalSum = sum(sampleList)
print(theTotalSum)
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
