import pygame
from datetime import datetime
class MickeyClock:
    def __init__(self, face, right_hand, left_hand):
        self.face = pygame.image.load(face).convert()
        self.face = pygame.transform.scale(self.face, (650, 650))

        self.right_hand = pygame.image.load(right_hand).convert_alpha()
        self.left_hand = pygame.image.load(left_hand).convert_alpha()
        self.right_hand = pygame.transform.smoothscale(
            self.right_hand, (240, 120)
        )
        self.left_hand = pygame.transform.smoothscale(
            self.left_hand, (180, 90)
        )
        self.left_hand = pygame.transform.flip(
            self.left_hand, False, True
        )
        self.center = pygame.Vector2(325, 325)
    def rotate_hand(self, screen, image, angle, pivot):
        rotation = 90 - angle
        rotated = pygame.transform.rotate(image, rotation)
        offset = pygame.Vector2(image.get_rect().center) - pivot
        rotated_offset = offset.rotate(-rotation)
        rect = rotated.get_rect(
            center=self.center + rotated_offset
        )
        screen.blit(rotated, rect)
    def draw(self, screen):
        screen.blit(self.face, (0, 0))
        now = datetime.now()
        minute_angle = now.minute * 6 + now.second * 0.1
        second_angle = now.second * 6
        self.rotate_hand(
            screen, self.right_hand,
            minute_angle, pygame.Vector2(25, 20)
        )
        self.rotate_hand(
            screen, self.left_hand,
            second_angle, pygame.Vector2(18, 75)
        )
        pygame.draw.circle(screen, (0, 0, 0), (325, 325), 6)



