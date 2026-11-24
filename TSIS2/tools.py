import pygame
import math
def draw_shape(surface, tool, color, start, end, size):
    x1, y1 = start
    x2, y2 = end
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x2 - x1)
    h = abs(y2 - y1)

    if tool == "Line":
        pygame.draw.line(surface, color, start, end, size)
    elif tool == "Rectangle":
        pygame.draw.rect(surface, color, (x, y, w, h), size)
    elif tool == "Circle":
        radius = int(math.hypot(x2 - x1, y2 - y1))
        pygame.draw.circle(surface, color, start, radius, size)
    elif tool == "Square":
        side = min(w, h)
        pygame.draw.rect(
            surface, color, (x, y, side, side), size
        )
    elif tool == "Right Triangle":
        points = [(x1, y1), (x1, y2), (x2, y2)]
        pygame.draw.polygon(surface, color, points, size)
    elif tool == "Equilateral Triangle":
        side = w
        height = int(side * math.sqrt(3) / 2)
        points = [
            (x + side // 2, y),
            (x, y + height),
            (x + side, y + height)
        ]

        pygame.draw.polygon(surface, color, points, size)
    elif tool == "Rhombus":
        points = [
            (x + w // 2, y),
            (x + w, y + h // 2),
            (x + w // 2, y + h),
            (x, y + h // 2)
        ]

        pygame.draw.polygon(surface, color, points, size)
def flood_fill(surface, position, color):
    width, height = surface.get_size()
    x, y = position
    if not (0 <= x < width and 0 <= y < height):
        return
    old_color = surface.get_at(position)
    new_color = pygame.Color(*color)

    if old_color == new_color:
        return

    stack = [position]
    surface.set_at(position, new_color)
    while stack:
        x, y = stack.pop()

        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]
        for nx, ny in neighbors:
            if 0 <= nx < width and 0 <= ny < height:
                if surface.get_at((nx, ny)) == old_color:
                    surface.set_at((nx, ny), new_color)
                    stack.append((nx, ny))