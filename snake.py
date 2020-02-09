import pygame
import random

pygame.init()
gameWidth = 600
gameHeight = 600
snakeSpeed = 10
blockSize = 20

game = pygame.display.set_mode((gameWidth, gameHeight))

inGame = True
pygame.display.update()
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()
eatenApples = 0

snakeBody = []
snakeLength = 3
snakeX = gameWidth / 2
snakeY = gameHeight / 2

changeX = blockSize
changeY = 0
appleX = random.randrange(0, (gameWidth - blockSize) / blockSize) * blockSize
appleY = random.randrange(0, (gameHeight - blockSize) / blockSize) * blockSize

while inGame:
    clickX = False
    clickY = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            InGame = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and changeX.__abs__() != blockSize and not clickY:
                changeX = -blockSize
                changeY = 0
                clickX = True
            elif event.key == pygame.K_RIGHT and changeX.__abs__() != blockSize and not clickY:
                changeX = blockSize
                changeY = 0
                clickX = True
            elif event.key == pygame.K_UP and changeY.__abs__() != blockSize and not clickX:
                changeX = 0
                changeY = -blockSize
                clickY = True
            elif event.key == pygame.K_DOWN and changeY.__abs__() != blockSize and not clickX:
                changeX = 0
                changeY = blockSize
                clickY = True

    snakeX += changeX;
    snakeY += changeY;

    if snakeX < 0 or snakeX >= gameWidth or snakeY < 0 or snakeY >= gameHeight:
        inGame = False

    if snakeX == appleX and snakeY == appleY:
        goodApplePosition = False
        while not goodApplePosition:
            goodApplePosition = True
            appleX = random.randrange(0, (gameWidth - blockSize) / blockSize) * blockSize
            appleY = random.randrange(0, (gameHeight - blockSize) / blockSize) * blockSize

            for x in snakeBody:
                if x[0].__int__() == appleX.__int__() and x[1].__int__() == appleY.__int__():
                    goodApplePosition = False

        snakeLength += 3
        eatenApples += 1

    game.fill((0, 0, 0))

    pygame.draw.ellipse(game, (255, 0, 0), [appleX, appleY, blockSize, blockSize])
    pygame.draw.ellipse(game, (0, 0, 0), [appleX, appleY, blockSize, blockSize],1)
    snakeHead = [snakeX, snakeY]
    snakeBody.append(snakeHead)
    if snakeBody.__len__() > snakeLength:
        snakeBody.pop(0)

    for x in snakeBody[:-1]:
        pygame.draw.rect(game, (0, 150, 0), [x[0].__int__(), x[1].__int__(), blockSize, blockSize])
        pygame.draw.rect(game, (0, 0, 0), [x[0].__int__(), x[1].__int__(), blockSize, blockSize], 1)
        if x == snakeHead:
            inGame = False
    pygame.draw.rect(game, (0, 100, 0), [snakeX.__int__(), snakeY.__int__(), blockSize, blockSize])
    pygame.draw.rect(game, (0, 0, 0), [snakeX.__int__(), snakeY.__int__(), blockSize, blockSize], 1)

    if changeX == blockSize:
        pygame.draw.ellipse(game, (0, 0, 0), [snakeX.__int__()+blockSize/4, snakeY.__int__() + blockSize/4 - blockSize / 8, blockSize/4, blockSize/4])
        pygame.draw.ellipse(game, (0, 0, 0), [snakeX.__int__()+blockSize/4, snakeY.__int__() + blockSize/4*3 - blockSize / 8, blockSize/4, blockSize/4])
    elif changeX == -blockSize:
        pygame.draw.ellipse(game, (0, 0, 0), [snakeX.__int__()+blockSize/4*3 - blockSize/8, snakeY.__int__() + blockSize / 4 - blockSize / 8, blockSize/4, blockSize/4])
        pygame.draw.ellipse(game, (0, 0, 0), [snakeX.__int__()+blockSize/4*3 - blockSize/8, snakeY.__int__() + blockSize / 4 * 3 - blockSize / 8, blockSize/4, blockSize/4])
    elif changeY == blockSize:
        pygame.draw.ellipse(game, (0, 0, 0), [snakeX.__int__()+blockSize/4 - blockSize/8, snakeY.__int__() + blockSize/4, blockSize/4, blockSize/4])
        pygame.draw.ellipse(game, (0, 0, 0), [snakeX.__int__()+blockSize/4*3 - blockSize/8, snakeY.__int__() + blockSize/4, blockSize/4, blockSize/4])
    elif changeY == -blockSize:
        pygame.draw.ellipse(game, (0, 0, 0), [snakeX.__int__()+blockSize/4 - blockSize/8, snakeY.__int__() + blockSize/4*3 - blockSize/8, blockSize/4, blockSize/4])
        pygame.draw.ellipse(game, (0, 0, 0), [snakeX.__int__()+blockSize/4*3 - blockSize/8, snakeY.__int__() + blockSize/4*3 - blockSize/8, blockSize/4, blockSize/4])

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("Points: " + eatenApples.__str__(), True, (200, 150, 150))
    textRect = text.get_rect()
    textRect.center = (100, 30)
    game.blit(text, textRect)

    pygame.display.update()
    clock.tick(snakeSpeed)

pygame.quit()
quit()
