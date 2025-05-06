import pygame

def read_obstacles(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    rows, cols = map(int, lines[0].split())
    obstacles = set()
    for line in lines[1:]:
        x, y = map(int, line.split())
        obstacles.add((x, y))
    
    return rows, cols, obstacles

class Robot:
    DIRECTIONS = ['N', 'E', 'S', 'W']
    MOVES = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    
    def __init__(self, x, y, direction, rows, cols, obstacles, goal_x, goal_y):
        self.x = x
        self.y = y
        self.direction = direction
        self.rows = rows
        self.cols = cols
        self.obstacles = obstacles
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.path = [(x, y)]  # Зберігаємо траєкторію руху
    
    def turn_left(self):
        self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) - 1) % 4]
    
    def turn_right(self):
        self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) + 1) % 4]
    
    def can_move(self):
        dx, dy = self.MOVES[self.direction]
        new_x, new_y = self.x + dx, self.y + dy
        return (0 <= new_x < self.rows and 0 <= new_y < self.cols and (new_x, new_y) not in self.obstacles)
    
    def move_forward(self):
        if self.can_move():
            dx, dy = self.MOVES[self.direction]
            self.x += dx
            self.y += dy
            self.path.append((self.x, self.y))  # Додаємо позицію в шлях
    
    def calc_next_dir(self):
        # Перевірка напрямку за годинниковою стрілкою (правосторонній обхід)
        for _ in range(4):
            if self.can_move():
                return
            self.turn_right()
        # Якщо не можна рухатись у жодному напрямку, зупиняємо робота
        return False
    
    def move_towards_goal(self):
        if (self.x, self.y) == (self.goal_x, self.goal_y):
            return True
        if self.can_move():
            self.move_forward()
        else:
            if not self.calc_next_dir():  # Якщо всі напрямки заблоковані
                return False
        return False

def draw_grid(screen, rows, cols, obstacles, robot):
    cell_size = 40
    screen.fill((255, 255, 255))
    for x in range(rows):
        for y in range(cols):
            rect = pygame.Rect(y * cell_size, x * cell_size, cell_size, cell_size)
            if (x, y) in obstacles:
                pygame.draw.rect(screen, (0, 0, 0), rect)
            else:
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)
    
    goal_rect = pygame.Rect(robot.goal_y * cell_size, robot.goal_x * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, (0, 255, 0), goal_rect)
    
    for px, py in robot.path:
        path_rect = pygame.Rect(py * cell_size + 10, px * cell_size + 10, 20, 20)
        pygame.draw.rect(screen, (0, 0, 255), path_rect)
    
    robot_rect = pygame.Rect(robot.y * cell_size, robot.x * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, (255, 0, 0), robot_rect)
    pygame.display.flip()

def main():
    pygame.init()
    file_path = "obstacles.txt"
    rows, cols, obstacles = read_obstacles(file_path)
    screen = pygame.display.set_mode((cols * 40, rows * 40))
    pygame.display.set_caption("Robot Navigation")
    
    robot = Robot(0, 0, 'E', rows, cols, obstacles, rows - 1, cols - 1)
    running = True
    goal_reached = False
    start_time = pygame.time.get_ticks()

    while running:
        draw_grid(screen, rows, cols, obstacles, robot)
        
        if not goal_reached:
            goal_reached = robot.move_towards_goal()  # Рух до мети
        
        if goal_reached:
            print("Goal reached!")
        
        if pygame.time.get_ticks() - start_time > 200:  # затримка між кроками
            start_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

if __name__ == "__main__":
    main()
