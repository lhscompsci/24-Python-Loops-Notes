

# while loop examples
x = 0
while (x < 5):
    print(x)
    x += 1

# loops don't always have to count by singular values
x = 0
while(x < 15):
    print (x)
    x += 3

# Lopps don't always have to count up
x = 30
while (x > 0):
    print(x)
    x = x - 4

# loops don't have to count at all -- they can be used to discover things and dissect things

# watch this
num = 9154
print(num % 10)
print(num // 10)

# notice anything special?

number = 157342
while (number > 0):
    print(number % 10)
    number = number // 10


# for loops -- counting loops
for g in range(-10,15,3):
     print(g,"Howdy")


# for each
for c in "Hello World":
    print(c,end=" ")

word = "Computer Science"
for w in word:
    if w == "u":
        break
    print(w)

#nested loops
for x in range(3):
    print ("x is",x)
    for y in range(2):
        print ("y is",y)
    print()

for x in range (3):
    for y in range(2):
        print("(",str(x),",",str(y),")")