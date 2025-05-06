import pygame
import random

# ініціалізація Pygame
pygame.init()

# налаштування екрану
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Базова гра на Pygame")

# кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# параметри гравця
player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# перешкоди
obstacle_width = 50
obstacle_height = 50
obstacles = []

# бонуси
bonus_width = 30
bonus_height = 30
bonuses = []

# ціль
goal_width = 100
goal_height = 100
goal_x = random.randint(0, screen_width - goal_width)
goal_y = random.randint(0, screen_height - goal_height)

# годинник для контролю кадрів
clock = pygame.time.Clock()

# основна функція гри
def game():
    global player_x, player_y, goal_x, goal_y, obstacles, bonuses
    running = True
    score = 0

    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # керування гравцем
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < screen_height - player_height:
            player_y += player_speed

        # додавання перешкод
        if random.randint(1, 100) < 2:
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            obstacle_y = 0
            obstacles.append([obstacle_x, obstacle_y])

        # рух перешкод
        for obstacle in obstacles:
            obstacle[1] += 5
            if obstacle[1] > screen_height:
                obstacles.remove(obstacle)

        # додавання бонусів
        if random.randint(1, 100) < 2:
            bonus_x = random.randint(0, screen_width - bonus_width)
            bonus_y = 0
            bonuses.append([bonus_x, bonus_y])

        # рух бонусів
        for bonus in bonuses:
            bonus[1] += 5
            if bonus[1] > screen_height:
                bonuses.remove(bonus)

        # перевірка на зіткнення з перешкодами
        for obstacle in obstacles:
            if (player_x < obstacle[0] + obstacle_width and player_x + player_width > obstacle[0] and
                player_y < obstacle[1] + obstacle_height and player_y + player_height > obstacle[1]):
                running = False  # гра закінчується при зіткненні з перешкодою

        # перевірка на зібрання бонусів
        for bonus in bonuses:
            if (player_x < bonus[0] + bonus_width and player_x + player_width > bonus[0] and
                player_y < bonus[1] + bonus_height and player_y + player_height > bonus[1]):
                bonuses.remove(bonus)
                score += 1

        # перевірка на досягнення цілі
        if (player_x < goal_x + goal_width and player_x + player_width > goal_x and
            player_y < goal_y + goal_height and player_y + player_height > goal_y):
            running = False  # гра закінчується при досягненні цілі

        # малюємо гравця
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

        # малюємо перешкоди
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

        # малюємо бонуси
        for bonus in bonuses:
            pygame.draw.rect(screen, GREEN, (bonus[0], bonus[1], bonus_width, bonus_height))

        # малюємо ціль
        pygame.draw.rect(screen, BLACK, (goal_x, goal_y, goal_width, goal_height))

        # показуємо рахунок
        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.update()

        clock.tick(60)  # обмеження кадрів на секунду

    pygame.quit()

# запуск гри
game()
