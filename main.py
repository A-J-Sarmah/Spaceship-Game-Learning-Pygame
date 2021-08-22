# imports pygame
import pygame
import os

WIDTH, HEIGHT = 900, 500
FPS = 60
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))  # loads yellow  spaceship
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (55, 40)),
                                           90)  # rotates and resizes the spaceship images
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))  # loads red  spaceship
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (55, 40)),
                                        270)  # resizes the spaceship images
VEL = 5
BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)
# creates a pygame window pygame.display.set_mode() takes a tuple as argument and makes a new app window .
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship game")  # set name of the window .


def draw_window(red, yellow):
    WINDOW.fill((255, 255, 255))  # set the color of screen it takes rgb value as tuple .
    pygame.draw.rect(WINDOW, (0, 0, 0), BORDER)  # draws the border rectangle .
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))  # draws the spaceship .
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))  # draws the spaceship.
    pygame.display.update()  # updates the display after each render.


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # checks if we pressed left key
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # checks if we pressed right key
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # checks if we pressed left key
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT:  # checks if we pressed right key
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # checks if we pressed left key
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # checks if we pressed right key
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # checks if we pressed left key
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT:  # checks if we pressed right key
        red.y += VEL


# game loop in pygame
def main():
    red = pygame.Rect(700, 300, 55, 40)  # defines position for red player
    yellow = pygame.Rect(100, 300, 55, 40)  # defines position for red player
    clock = pygame.time.Clock()  # defines clock object that controls FPS
    run = True
    while run:
        clock.tick(FPS)  # controls FPS
        # check pygame event and determine the logic based on it  here pygame.event.get() returns a list of event
        for event in pygame.event.get():
            # checks if user quit the game and accordingly toggles the game loop.
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()  # keep track of key press
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)
    # exit pygame window at end of loop
    pygame.quit()


if __name__ == "__main__":
    main()
