print("hello") #single line comment
print("Good morning")
age = 23
name = "Zac"
print (age,name)
word="Lecture"
letter=word[2] #INdesxing starts at 0 so 2 refers to c
print(letter)

word="charmander evovles to charizard"
sub_word= word[8:10] #sliciing from index 8 to 10
print(sub_word)

message = "Hello, %s. Your are %d years old." %(name, age)
print(message) #Output: Heelo, Zac. You are 23 years old.

#Practice_roll dice
import random #Import other's code
def roll_dice():
    return random.randrange(1,7) #It does not generate the number of 7
#or we could use random.randint(1,6), which include the number of 6

print(roll_dice())
print(roll_dice())
print(roll_dice())
print(roll_dice())
print(roll_dice())

