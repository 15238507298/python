import pygame, sys

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("pygame")
ball = pygame.image.load('../com.sunland.resources/face.jpg')
ball_x = 40
ball_y = 30
m_x = 1
m_y = 1
fclock = pygame.time.Clock()
ball_rect = ball.get_rect()

bool = False
while True:

    for ev in pygame.event.get():

        #print(''.format(ev.type,pygame.KEYUP))
        #print(pygame.QUIT)

        if ev.type == pygame.QUIT:
            sys.exit(0)

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_UP:
                m_y = -(m_y**21)
                if bool: bool = False
            elif ev.key == pygame.K_DOWN:
                m_y = m_y**2
                if bool: bool = False
            elif ev.key == pygame.K_LEFT:
                m_x = -(m_x**2)
                if bool == False: bool = True
            elif ev.key == pygame.K_RIGHT:
                m_x = m_x**2
                if bool == False: bool = True
        elif ev.type == pygame.VIDEORESIZE:
            print('change')
            size = width, height = ev.w, ev.h
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            print('{} >> {}'.format(width, height))
    if bool:
        print(width)
        if ball_x + m_x <= 0:
            m_x = m_x**2
        elif ball_x + m_x + ball_rect.width >= width:
            m_x = -(m_x**2)
        else:
            ball_x = ball_x + m_x
    else:

        if ball_y + m_y <= 0:
            m_y = m_y**2
        elif ball_y + m_y + ball_rect.height >= height:
            m_y = -(m_y**2)
        else:
            ball_y = ball_y + m_y

    screen.fill((0, 0, 0))
    screen.blit(ball, (ball_x, ball_y))
    pygame.display.update()
    fclock.tick(380)
