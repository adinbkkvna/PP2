import pygame
from datetime import datetime
from tools import draw_shape, flood_fill
pygame.init()
WIDTH = 1000
HEIGHT = 700
TOOLBAR = 150

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 2 - Paint Application")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (225, 230, 235)
BLUE = (180, 205, 235)

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR))
canvas.fill(WHITE)

font = pygame.font.SysFont("Arial", 16)
text_font = pygame.font.SysFont("Arial", 28)

clock = pygame.time.Clock()

tools = [
    "Pencil", "Line", "Rectangle", "Circle",
    "Square", "Right Triangle", "Equilateral Triangle",
    "Rhombus", "Eraser", "Fill", "Text"
]
colors = [
    BLACK,
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (150, 0, 200),
    (255, 105, 180),
    WHITE
]
tool_buttons = {}
color_buttons = {}
size_buttons = {}

for i, name in enumerate(tools):
    x = 10 + (i % 6) * 164
    y = 10 + (i // 6) * 38

    tool_buttons[name] = pygame.Rect(x, y, 158, 32)
for i, c in enumerate(colors):
    color_buttons[c] = pygame.Rect(
        10 + i * 34, 100, 28, 28
    )
for i, s in enumerate([2, 5, 10]):
    size_buttons[s] = pygame.Rect(
        350 + i * 65, 100, 60, 28
    )
save_button = pygame.Rect(580, 100, 90, 28)
clear_button = pygame.Rect(680, 100, 90, 28)

tool = "Pencil"
color = BLACK
size = 5
drawing = False
start = (0, 0)
previous = (0, 0)
current = (0, 0)
typing = False
text = ""
text_position = (0, 0)
running = True

def save_canvas():
    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S_%f"
    )
    filename = f"painting_{timestamp}.png"
    pygame.image.save(canvas, filename)
    print("Saved:", filename)

def draw_button(rect, label, selected=False):
    background = BLUE if selected else WHITE

    pygame.draw.rect(
        screen, background, rect, border_radius=5
    )
    pygame.draw.rect(
        screen, BLACK, rect, 1, border_radius=5
    )
    label_surface = font.render(label, True, BLACK)
    screen.blit(
        label_surface,
        label_surface.get_rect(center=rect.center)
    )
def canvas_position(position):
    return position[0], position[1] - TOOLBAR

def limited_position(position):
    x, y = canvas_position(position)
    x = max(0, min(x, WIDTH - 1))
    y = max(0, min(y, HEIGHT - TOOLBAR - 1))

    return x, y

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s and (
                event.mod & (pygame.KMOD_CTRL | pygame.KMOD_META)
            ):
                save_canvas()
            elif typing:

                if event.key == pygame.K_RETURN:
                    rendered = text_font.render(
                        text, True, color
                    )
                    canvas.blit(rendered, text_position)
                    typing = False
                    text = ""
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text = ""

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]

                elif event.unicode.isprintable():
                    text += event.unicode

            elif event.key == pygame.K_1:
                size = 2

            elif event.key == pygame.K_2:
                size = 5

            elif event.key == pygame.K_3:
                size = 10

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button != 1:
                continue

            mx, my = event.pos
            if my < TOOLBAR:
                for name, rect in tool_buttons.items():
                    if rect.collidepoint(event.pos):
                        tool = name
                        typing = False
                        text = ""
                for c, rect in color_buttons.items():
                    if rect.collidepoint(event.pos):
                        color = c
                for s, rect in size_buttons.items():
                    if rect.collidepoint(event.pos):
                        size = s
                if save_button.collidepoint(event.pos):
                    save_canvas()
                if clear_button.collidepoint(event.pos):
                    canvas.fill(WHITE)
                    typing = False
                    text = ""
            else:
                position = canvas_position(event.pos)
                if tool == "Fill":
                    flood_fill(canvas, position, color)
                elif tool == "Text":
                    typing = True
                    text = ""
                    text_position = position
                else:
                    drawing = True
                    start = position
                    previous = position
                    current = position
                    if tool == "Pencil":
                        pygame.draw.circle(
                            canvas, color, position,
                            max(1, size // 2)
                        )
                    elif tool == "Eraser":
                        pygame.draw.circle(
                            canvas, WHITE, position,
                            size
                        )
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current = limited_position(event.pos)
                if tool == "Pencil":
                    pygame.draw.line(
                        canvas, color,
                        previous, current, size
                    )
                elif tool == "Eraser":
                    pygame.draw.line(
                        canvas, WHITE,
                        previous, current, size * 2
                    )

                previous = current
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                current = limited_position(event.pos)
                if tool not in ["Pencil", "Eraser"]:
                    draw_shape(
                        canvas, tool, color,
                        start, current, size
                    )
                drawing = False

    screen.fill(GRAY)
    preview = canvas.copy()
    if drawing and tool not in ["Pencil", "Eraser"]:
        draw_shape(
            preview, tool, color,
            start, current, size
        )
    if typing:
        rendered = text_font.render(text, True, color)
        preview.blit(rendered, text_position)

        cursor_x = text_position[0] + rendered.get_width()
        cursor_y = text_position[1]
        pygame.draw.line(
            preview, color,
            (cursor_x, cursor_y),
            (cursor_x, cursor_y + 28),
            2
        )
    screen.blit(preview, (0, TOOLBAR))
    for name, rect in tool_buttons.items():
        draw_button(rect, name, tool == name)
    for c, rect in color_buttons.items():
        pygame.draw.rect(screen, c, rect)

        pygame.draw.rect(
            screen, BLACK, rect,
            3 if color == c else 1
        )
    for s, rect in size_buttons.items():
        draw_button(rect, f"{s} px", size == s)
    draw_button(save_button, "Save")
    draw_button(clear_button, "Clear")
    status = font.render(
        f"{tool} | {size} px", True, BLACK
    )

    screen.blit(status, (790, 105))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()