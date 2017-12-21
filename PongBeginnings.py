import pygame
import sys


WIN_W=920
WIN_H=570


pygame.init()

WHITE=(255,255,255)
def main():
    pygame.display.set_caption('Pong')
    screen= pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    paddle_width=20
    paddle_height=90


    ball_width=20
    ball_height=20

    x1 = 20
    x2 = WIN_W - 40

    xball = WIN_W / 2
    yball = WIN_H / 2
    speed=10
    ballSpeed=[5,5]





    paddle_1=pygame.Surface((paddle_width, paddle_height))
    paddle_2=pygame.Surface((paddle_width, paddle_height))
    ball=pygame.Surface((ball_width, ball_height))
    ballRect=pygame.Rect(WIN_W/2, WIN_H/2-(ball_height/2), ball_width, ball_height)









    y1=WIN_H/2-paddle_height/2

    y2=WIN_H/2-paddle_height/2

    P1Rect=pygame.Rect(x1,y1, paddle_width, paddle_height)
    P2Rect=pygame.Rect(x2,y2,paddle_width,paddle_height)


    clock=pygame.time.Clock()
    play= True

    screen.fill((WHITE))

    moveUP=False
    moveDOWN=False
    moveUP2=False
    moveDOWN2=False
    score=0

    while play:

        #moving the paddles
        for event in pygame.event.get():
            if event.type==pygame.QUIT: sys.exit()

            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    moveUP2= True
                    moveDOWN2=False
                elif event.key==pygame.K_DOWN:
                    moveUP2=False
                    moveDOWN2=True
                if event.key==pygame.K_w:
                    moveUP=True
                    moveDOWN=False
                elif event.key==pygame.K_s:
                    moveUP=False
                    moveDOWN=True

            elif event.type == pygame.KEYUP:
                if event.key==pygame.K_UP:
                    moveUP2=False
                elif event.key==pygame.K_DOWN:
                    moveDOWN2=False
                if event.key==pygame.K_w:
                    moveUP=False
                elif event.key==pygame.K_s:
                    moveDOWN=False

        if moveUP or moveDOWN:
            if moveUP:
                P1Rect.top-=speed*2
            if moveDOWN:

                P1Rect.top+=speed*2
        if moveUP2 or moveDOWN2:
            if moveUP2:
                P2Rect.top-=speed*2
            if moveDOWN2:
                P2Rect.top+=speed*2
        if P1Rect.top<0:
            P1Rect.top=0
        if P1Rect.top+paddle_height>WIN_H:
            P1Rect.top=WIN_H - paddle_height
        if P2Rect.top<0:
            P2Rect.top=0
        if P2Rect.top+paddle_height>WIN_H:
            P2Rect.top=WIN_H-paddle_height




        ballRect=ballRect.move(ballSpeed)

        #Bounce ball off of top and bottom walls

        if ballRect.top > WIN_H - ballRect.height:
            ballSpeed[1] = -ballSpeed[1]
        elif ballRect.top<0:
            ballSpeed[1]=-ballSpeed[1]


        #Bounce ball off of paddles
        if (ballRect.right>=P2Rect.left-5 and ballRect.right <= P2Rect.left+5) and (ballRect.top<=P2Rect.bottom and ballRect.bottom>=P2Rect.top):
            ballSpeed[0]=-ballSpeed[0]
            ballSpeed[0]=(ballSpeed[0]-1)
            ballSpeed[1]=(ballSpeed[1]-1)
            score=score+1


        if (ballRect.left<=P1Rect.right+5 and ballRect.left>=P1Rect.right-5) and (ballRect.top<=P1Rect.bottom and ballRect.bottom>=P1Rect.top):
            ballSpeed[0]=-ballSpeed[0]
            score=score+1

        if ballRect.left >WIN_W:
            print('Player One Wins!')
            print("Your rally score is:"+ str(score))
            break
        elif ballRect.right<0:
            print("Player Two Wins!")
            print('Your rally score is:'+ str(score))
            break











        screen.fill((WHITE))




        screen.blit(paddle_1, P1Rect)
        screen.blit(paddle_2, P2Rect)
        screen.blit(ball,ballRect)



        clock.tick(60)

        pygame.display.flip()

if __name__== "__main__":
    main()
