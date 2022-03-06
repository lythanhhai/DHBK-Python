################### Scope ####################

from turtle import position


enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

def drink_potion():
    position_strength = 2
    print(position_strength)

drink_potion()
# print(position_strength) # error local scope

play_healthy = 2

def drink_potion1():
    print(play_healthy)

drink_potion()

# block scope
if 3 > 2:
  a = 1
  print(a)

game_level = 3 
def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
      new_enemy = enemies[0]
  print(new_enemy)


# global to using global varieble in function

enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")