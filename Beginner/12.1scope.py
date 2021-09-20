# LOCAL SCOPE AND GLOBAL SCOPE
enemies = 1

def increase_enemies():
    enemies = 2
    # local scope
    print(f"enemies inside function: {enemies}")


increase_enemies()
# global scope
print(f"enemies outside function: {enemies}")



# NO BLOCK SCOPE 
game_level=3
def create_enemy():
    enemies=["Skeleton","Zombie","Alien"]
    if game_level<5:
        # new_enemy - not block scope, instead function scope
        new_enemy=enemies[0]
    print(new_enemy)
# print(new_enemy) Error: outside function and not block scope.

create_enemy()


# Modifying Global Scope

enemy = "Skeleton"


def increase_enemy():
    # Explicitly specify you are using global variable- SHOULD AVOID MODIFYING,instead use "return" like return enemy+1
    global enemy

    enemy = "Zombie"
    print(f"enemies inside function: {enemy}")


increase_enemy()
print(f"enemies outside function: {enemy}")



# Global Constants

# use UPPERCASE - not going to change in the code
PI =3.14
URL="www.google.com"