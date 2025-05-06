import random

def read_map(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    width, height = map(int, lines[0].split())
    obstacles = set()
    
    for line in lines[1:]:
        for coord in line.split():
            x, y = map(int, coord.split(','))
            obstacles.add((x, y))
    
    return width, height, obstacles

def generate_goal(width, height, obstacles, start):
    free_cells = [(x, y) for x in range(width) for y in range(height)
                  if (x, y) not in obstacles and (x, y) != start]
    return random.choice(free_cells)

def generate_bonuses(width, height, obstacles, goal, start, num_bonuses=3):
    free_cells = [(x, y) for x in range(width) for y in range(height)
                  if (x, y) not in obstacles and (x, y) != goal and (x, y) != start]
    return set(random.sample(free_cells, min(num_bonuses, len(free_cells))))

def print_grid(width, height, obstacles, position, goal, bonuses):
    for y in range(height):
        row = ''
        for x in range(width):
            if (x, y) == position:
                row += 'O '
            elif (x, y) == goal:
                row += 'G '
            elif (x, y) in bonuses:
                row += 'B '
            elif (x, y) in obstacles:
                row += 'X '
            else:
                row += '. '
        print(row)

def move(position, direction, width, height, obstacles):
    x, y = position
    if direction == 'w' and y > 0 and (x, y - 1) not in obstacles:
        y -= 1
    elif direction == 's' and y < height - 1 and (x, y + 1) not in obstacles:
        y += 1
    elif direction == 'a' and x > 0 and (x - 1, y) not in obstacles:
        x -= 1
    elif direction == 'd' and x < width - 1 and (x + 1, y) not in obstacles:
        x += 1
    return x, y

# Зчитуємо та виводимо карту
filename = "map.txt"  # Твій файл із перешкодами
width, height, obstacles = read_map(filename)
position = (0, 0)  # Початкова позиція
goal = generate_goal(width, height, obstacles, position)  # Випадкова ціль
bonuses = generate_bonuses(width, height, obstacles, goal, position)  # Випадкові бонуси

collected_bonuses = 0

while True:
    print_grid(width, height, obstacles, position, goal, bonuses)
    print(f"Зібрано бонусів: {collected_bonuses}")
    if position == goal:
        print("Вітаємо! Ви дісталися до цілі!")
        break
    move_direction = input("Рух (w - вгору, s - вниз, a - вліво, d - вправо, q - вихід): ")
    if move_direction == 'q':
        break
    position = move(position, move_direction, width, height, obstacles)
    if position in bonuses:
        bonuses.remove(position)
        collected_bonuses += 1