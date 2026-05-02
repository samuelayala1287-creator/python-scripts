import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("master.mp3")
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)