import pygame
from clock import MickeyClock
pygame.init()
screen = pygame.display.set_mode((650, 650))
pygame.display.set_caption("Mickey Mouse Clock")
clock = pygame.time.Clock()
mickey = MickeyClock(
    "images/clock_face_cropped.jpg",
    "images/right_hand.png",
    "images/left_hand.png"
)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mickey.draw(screen)
    pygame.display.flip()
    clock.tick(1)
pygame.quit()
