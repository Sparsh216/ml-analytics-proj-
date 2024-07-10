import pygame
pygame.init

gamewindow=pygame.display.set_mode((900,600))
pygame.display.set_caption("My first Game")
exit_game=False
game_over=False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_0:
                print("You have pressed 0")


pygame.quit()
quit()