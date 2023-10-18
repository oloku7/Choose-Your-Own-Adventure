# Lab 2 - Choose your own adventure.
# Write the names of the members of your breakout group here:
#   1. (myself)
#   2.
#   3.
#   4.

print("Welcome to choose your own adventure game!")
name = input("What is your name? ")

print(f"Alright {name}, choose your character!")


print("Thor")
print("Hulk")
print("Spider-man")
print("Iron-man")

character_name = input("").lower()

if character_name == 'thor':
 print("Bring on the Lightening and the Thunder!")

if character_name == 'hulk':
 print("Your Strong and Mighty!")

if character_name == 'spider-man':
  print("Your sneaky and stealthy!")

if character_name == 'iron-man':
  print("Your Strong and Meatalic!")




print ("Who will you choose to fight first? ")

print("Thanos")
print("Joker")
print("Loki")

name_1 = input("")

if name_1 == 'thanos':
 print("You WON, Thanos forgot to get the last stone to regain full power! Nice Job!")

if name_1 == 'joker':
 print("You win! Joker couldn't with stand the Heat!")

if name_1 == 'loki':
  print("Aww you Lost! Loki's strong and mightly powers striked you, your dead.")

print("The End!")
