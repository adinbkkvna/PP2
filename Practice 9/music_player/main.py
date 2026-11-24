import pygame
import os
from player import MusicPlayer
pygame.init()
WIDTH = 700
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lovely music player")
BLACK = (18, 18, 18)
DARK = (35, 35, 35)
GREEN = (30, 215, 96)
WHITE = (255, 255, 255)
GRAY = (170, 170, 170)

title_font = pygame.font.SysFont("Arial", 34, bold=True)
font = pygame.font.SysFont("Arial", 23)
small_font = pygame.font.SysFont("Arial", 17)

playlist = [
    "music/track1.mp3",
    "music/track2.mp3"
]

player = MusicPlayer(playlist)
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    title = title_font.render("Music Player", True, GREEN)
    screen.blit(title, (40, 35))
    subtitle = small_font.render("YOUR PERSONAL MUSIC SPACE", True, GRAY)
    screen.blit(subtitle, (43, 80))
    pygame.draw.rect(screen, DARK, (40, 130, 620, 210), border_radius=18)
    track_name = os.path.basename(
        playlist[player.current_track]
    )

    track_name = os.path.splitext(track_name)[0]
    track_text = font.render(track_name, True, WHITE)
    screen.blit(track_text, (70, 170))
    status = "NOW PLAYING" if player.is_playing else "PAUSED / STOPPED"
    status_text = small_font.render(status, True, GREEN)
    screen.blit(status_text, (70, 215))

    pygame.draw.circle(screen, GREEN, (350, 295), 28)
    play_symbol = "||" if player.is_playing else "▶"
    symbol = font.render(play_symbol, True, BLACK)
    screen.blit(symbol, symbol.get_rect(center=(350, 295)))

    controls = [
        ("B", "Previous"),
        ("P", "Play / Pause*"),
        ("S", "Stop"),
        ("N", "Next")
    ]

    for i, (key, action) in enumerate(controls):
        x = 65 + i * 155
        pygame.draw.rect(
            screen, DARK, (x, 380, 135, 55), border_radius=12
        )
        key_text = font.render(key, True, GREEN)
        action_text = small_font.render(action, True, WHITE)
        screen.blit(key_text, (x + 12, 388))
        screen.blit(action_text, (x + 42, 397))

    footer = small_font.render(
        "Press Q to quit | *P starts the current track",
        True, GRAY
    )
    screen.blit(footer, (40, 465))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.previous_track()
            elif event.key == pygame.K_q:
                running = False
                
    clock.tick(30)
pygame.quit()
