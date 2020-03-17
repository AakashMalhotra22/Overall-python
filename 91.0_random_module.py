'''
random module functions:

1. random() - gives random value between 0 and 1 where 1 is not inclusive but 0 is inclusive
2. uniform(a,b)- gives random floating point value between a and b.
3. randint(a,b) - gives random whole number between a and b, here a and b are inclusive.
4. choice(list_name) - gives the random value from the list.

5. choices(list_name, k =number_of_values_you_want) - gives the k number of random values from the list in the form of list.
   In the output, same values can also come, means each value may not be unique
   In choices, you can also use some other attributes like weight.

6. shuffle(list_name) - It will shuffle the values in the list, means rearrange it.

7. sample(list_name, k=number_of_random_unique_values)- It will give k number of unique values from the list.

'''

from random import*

#1 random()
y = random()
print(y)

#2 uniform(a,b)

y = uniform(1,10)

print(y)

#3 randint(a,b)

y = randint(1,6)

print(y)

#4 choice(list_name)- When you want random values from list

greet = ["hello", "hi", "hey", "hei"]

y = choice(greet)

print(y + " aakash! ")


#5 choices(list_name) When you want more than 1 random outcomes from the list.

colors = ["red", "black", "Green"]

y = choices(colors, k = 10)

print(y)

#6  When you give the probabilities to the elements of the list

colors = ["red", "black", "Green"]

y = choices(colors, weights = [18,18,2], k = 10)

print(y)


#7 shuffle(list_name)

deck = list(range(1,53))
shuffle(deck) # It will shuffle the list.
print(deck)


#8 sample()

deck = list(range(1,53))
print(sample(deck, k=5)) # sample gives the unique values, it never gives the same values.

