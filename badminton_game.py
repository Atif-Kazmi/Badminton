import pygame
import random

# Initialize Pygame
pygame.init()

# Constants for the game
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Badminton Game")

# Game objects
player1 = pygame.Rect(50, HEIGHT//2 - 60, 10, 120)
player2 = pygame.Rect(WIDTH - 60, HEIGHT//2 - 60, 10, 120)
shuttlecock = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
shuttlecock_speed = [random.choice((5, -5)), random.choice((5, -5))]

player1_speed = 0
player2_speed = 0
player_speed = 7

# Game loop
def main_game():
    clock = pygame.time.Clock()
    running = True
    player1_score = 0
    player2_score = 0

    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Player 1 controls (W and S)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_speed = -player_speed
                if event.key == pygame.K_s:
                    player1_speed = player_speed
                if event.key == pygame.K_UP:
                    player2_speed = -player_speed
                if event.key == pygame.K_DOWN:
                    player2_speed = player_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2_speed = 0
        
        # Move players
        player1.y += player1_speed
        player2.y += player2_speed

        # Prevent paddles from moving off the screen
        if player1.top <= 0:
            player1.top = 0
        if player1.bottom >= HEIGHT:
            player1.bottom = HEIGHT
        if player2.top <= 0:
            player2.top = 0
        if player2.bottom >= HEIGHT:
            player2.bottom = HEIGHT

        # Move the shuttlecock
        shuttlecock.x += shuttlecock_speed[0]
        shuttlecock.y += shuttlecock_speed[1]

        # Shuttlecock collision with top and bottom
        if shuttlecock.top <= 0 or shuttlecock.bottom >= HEIGHT:
            shuttlecock_speed[1] = -shuttlecock_speed[1]

        # Shuttlecock collision with paddles
        if shuttlecock.colliderect(player1) or shuttlecock.colliderect(player2):
            shuttlecock_speed[0] = -shuttlecock_speed[0]

        # Shuttlecock out of bounds
        if shuttlecock.left <= 0:
            player2_score += 1
            shuttlecock.x, shuttlecock.y = WIDTH//2 - 15, HEIGHT//2 - 15
            shuttlecock_speed = [random.choice((5, -5)), random.choice((5, -5))]

        if shuttlecock.right >= WIDTH:
            player1_score += 1
            shuttlecock.x, shuttlecock.y = WIDTH//2 - 15, HEIGHT//2 - 15
            shuttlecock_speed = [random.choice((5, -5)), random.choice((5, -5))]

        # Draw the game objects
        pygame.draw.rect(screen, RED, player1)
        pygame.draw.rect(screen, BLUE, player2)
        pygame.draw.ellipse(screen, BLACK, shuttlecock)
        pygame.draw.aaline(screen, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        # Display scores
        font = pygame.font.Font(None, 74)
        text = font.render(str(player1_score), True, RED)
        screen.blit(text, (250, 10))
        text = font.render(str(player2_score), True, BLUE)
        screen.blit(text, (510, 10))

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main_game()
