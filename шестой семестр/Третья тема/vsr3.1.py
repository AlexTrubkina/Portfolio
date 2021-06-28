"""
Автор: Трубкина А.Ю.

3.3 Реализация графического интерфейса и функционала, позволяющего отображать графические примитивы для игры «Крестики-нолики».
"""



import pygame
import sys

pygame.init()

size_block = 100

margin = 15
width = height = size_block * 3 + margin * 4

size_window = (width, height)

screen = pygame.display.set_mode(size_window)


pink = (255,105,180)
violet = (199,21,133)
white = (255,255,255)

mas = [[0] * 3 for i in range(3)]

query = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] ='x'
                else:
                    mas[row][col] ='o'
                query += 1


    for row in range(3):
        for col in range(3):
            if mas[row][col] == 'x':
                color = pink
            elif mas[row][col] == 'o':
                color = violet
            else:
                color = white
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))
            if color == pink:
                pygame.draw.line(screen, white, (x + 5,y + 5), (x + size_block - 5, y + size_block - 5), 3)
                pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 3)
            elif color == violet:
                pygame.draw.circle(screen, white, (x + size_block // 2,y + size_block // 2), size_block // 2 - 3, 3)

        pygame.display.update()


