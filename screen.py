import pygame
import sys
import random

WIDTH, HEIGHT = 400, 600
FPS = 60
pipe_heights = [200, 150, 100]

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Flappy Bird')

        self.bg_img = pygame.image.load('background.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (400, 600))

        self.pipe_list=[]
        self.pipe_list_opposite=[]

        self.x=WIDTH
        self.upper_y = 0

        self.bird_img = pygame.image.load('player.png')
        self.bird_img = pygame.transform.scale(self.bird_img, (50, 50))
        self.bird_rect = self.bird_img.get_rect(topleft=(50, HEIGHT // 2))
        self.pipe_height = random.randint(200,270)

        self.lower_y = HEIGHT - self.pipe_height

        self.pipe_img = pygame.image.load('pipe.png')
        self.pipe_img = pygame.transform.scale(self.pipe_img, (50,self.pipe_height))
        self.pipe_img_opposite = pygame.image.load('pipeR.png')
        self.pipe_img_opposite = pygame.transform.scale(self.pipe_img_opposite, (50, self.pipe_height))
        

        self.score=0
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.gravity = 1
        self.jump_speed = -30


    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird_rect.y += self.jump_speed

            self.bird_rect.y += self.gravity
            self.x -= 3

            if self.x <= -50:
                self.score+=1
                self.pipe_height = random.randint(200,270)
                self.x = WIDTH
                
                self.pipe_img = pygame.transform.scale(self.pipe_img, (50,self.pipe_height))
                self.pipe_img_opposite = pygame.transform.scale(self.pipe_img_opposite, (50, self.pipe_height))
                self.lower_y = HEIGHT - self.pipe_height

            if self.bird_rect.x-self.x>=0 and self.bird_rect.x-self.x<=50:
                if self.bird_rect.y>=self.lower_y:
                    self.running=False
                    break;
                elif self.bird_rect.y<=self.pipe_height:
                    self.running=False
                    break;
                    

            self.screen.blit(self.bg_img, (0, 0))
            self.screen.blit(self.bird_img, self.bird_rect)
            self.screen.blit(self.pipe_img, (self.x,self.lower_y))
            self.screen.blit(self.pipe_img_opposite, (self.x,self.upper_y))
            # self.screen.blit(self.text, self.text_rect)
            font = pygame.font.Font(None, 36)
            text = font.render(f"{self.score}", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.topright = (WIDTH - 10, 10)
            self.screen.blit(text, text_rect)
            pygame.display.flip()

        pygame.quit()
