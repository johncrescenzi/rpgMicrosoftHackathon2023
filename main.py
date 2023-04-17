import pygame
import sys
import random
from pygame.locals import *

pygame.display.set_caption("Casus")
pygame.display.init()
pygame.mixer.init()
pygame.display.set_gamma(1.0)

ANIMATION_SPEED = 10

agility = 1

class Character(pygame.sprite.Sprite):
    def __init__(self, health, mana, strength, magic, defense, agility, powerPoints, experience):
        super().__init__()
        self.health = health
        self.mana = mana
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.agility = agility
        self.powerPoints = powerPoints
        self.experience = experience

class GameState:
    def __init__(self, screen_width, screen_height):
        self.current_screen = "title"
        self.bg_images = [pygame.image.load(f"assets/title/titleFrame{i}.jpg").convert() for i in range(0, 8)]
        self.bg_index = 0
        self.bg_image = self.bg_images[self.bg_index]
        self.bg_rect = self.bg_image.get_rect(center=(screen_width/2, screen_height/2))
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_counter = 0 

    def handle_event(self, event):
        print(event)
        print(self.current_screen)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and self.current_screen == "character_selection":
                powerPoints -= 1             
            elif event.key == pygame.K_SPACE:
                if self.current_screen == "title":
                    self.current_screen = "character_selection"
                elif self.current_screen == "character_selection":
                    self.current_screen = "stats"
                elif self.current_screen == "stats":
                    self.current_screen = "forest1"
            elif event.key == pygame.K_ESCAPE:
                print("quit")
                pygame.quit()
        elif event.type == pygame.QUIT:
            print("quit")
            pygame.quit()
            sys.exit()

    def update(self):
        # Update background image every 60 frames
        if self.current_screen == "title":
            if self.bg_index < len(self.bg_images) - 1:
                if self.game_counter % 10 == 0:
                    self.bg_index += 1
                    self.bg_image = self.bg_images[self.bg_index]
                    self.bg_rect = self.bg_image.get_rect(center=(self.screen_width/2, self.screen_height/2))
            else:
                # Loop back to first image
                self.bg_index = 0
                self.bg_image = self.bg_images[0]
                self.bg_rect = self.bg_image.get_rect(center=(self.screen_width/2, self.screen_height/2))
            self.game_counter += 1

    def render(self, screen):
        self.update()  # Call update every frame
        if self.current_screen == "title":

            # Calculate the position of the background image to center it on the screen
            bg_x = (self.screen_width - self.bg_rect.width) / 2
            bg_y = (self.screen_height - self.bg_rect.height) / 2
            screen.blit(self.bg_image, (bg_x, bg_y))

            # Load title image and center it on the screen
            title_image = pygame.image.load("assets/title/title.png").convert_alpha()
            title_x = (self.screen_width - title_image.get_rect().width) / 2
            title_y = (self.screen_height - title_image.get_rect().height) / 2 - 200
            screen.blit(title_image, (title_x, title_y))

            # Render "Press space" text at the bottom of the screen
            font = pygame.font.SysFont('papyrus', 50)
            text = font.render("Press space", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.screen_width/2, self.screen_height*0.8))
            screen.blit(text, text_rect)

        elif self.current_screen == "character_selection":
            # Load overlay image and center it on the screen
            overlay_image = pygame.image.load("assets/woodenOverlay.png").convert_alpha()
            overlay_x = (self.screen_width - overlay_image.get_rect().width) / 2
            overlay_y = (self.screen_height - overlay_image.get_rect().height) / 2 
            screen.blit(overlay_image, (overlay_x, overlay_y))

           # Load banner image and scale it
            banner_image = pygame.image.load("assets/banner.png").convert_alpha()
            banner_image = pygame.transform.scale(banner_image, (int(banner_image.get_rect().width / 1.1), int(banner_image.get_rect().height / 1.1)))

            # Place the banner image centered horizontally and towards the top vertically
            banner_x = (self.screen_width - banner_image.get_rect().width) / 2
            banner_y = 50 
            screen.blit(banner_image, (banner_x, banner_y))

            # Display character name and center it over the banner
            font = pygame.font.SysFont('papyrus', 80)
            text = font.render("Fallen Angel", True, (255, 255, 255))
            text_rect = text.get_rect(center=(banner_x + banner_image.get_rect().width / 2, banner_y + banner_image.get_rect().height / 2 + 25))
            screen.blit(text, text_rect)

            # Load and scale the character image
            character1_image = pygame.image.load("assets/characters/Fallen_Angels_1/PNG/IdleBlinking/frame0.png").convert_alpha()
            character1_image = pygame.transform.scale(character1_image, (int(character1_image.get_rect().width/2.75), int(character1_image.get_rect().height/2.75)))

            # Place the character in the middle
            character1_x = (self.screen_width  - character1_image.get_rect().width) / 2
            character1_y = (self.screen_height - character1_image.get_rect().height) / 2 
            screen.blit(character1_image, (character1_x, character1_y))

            # Load left arrow image and scale it to 50%
            leftArrow_image = pygame.image.load("assets/arrowLeft.png").convert_alpha()
            leftArrow_image = pygame.transform.scale(leftArrow_image, (int(leftArrow_image.get_rect().width / 2), int(leftArrow_image.get_rect().height / 2)))

            # Place the left arrow image left and centered vertically
            leftArrow_x = self.screen_width * 0.2 - leftArrow_image.get_rect().width / 2
            leftArrow_y = (self.screen_height - leftArrow_image.get_rect().height) / 2 
            screen.blit(leftArrow_image, (leftArrow_x, leftArrow_y))

            # Load right arrow image and scale it to 50%
            rightArrow_image = pygame.image.load("assets/arrowRight.png").convert_alpha()
            rightArrow_image = pygame.transform.scale(rightArrow_image, (int(rightArrow_image.get_rect().width / 2), int(rightArrow_image.get_rect().height / 2)))

            # Place the right arrow image right and centered vertically
            rightArrow_x = self.screen_width * 0.8 - rightArrow_image.get_rect().width / 2
            rightArrow_y = (self.screen_height - rightArrow_image.get_rect().height) / 2 
            screen.blit(rightArrow_image, (rightArrow_x, rightArrow_y))

            # Load button image 
            squareButton_image = pygame.image.load("assets/squareButton.png").convert_alpha()
            squareButton_image = pygame.transform.scale(squareButton_image, (int(squareButton_image.get_rect().width), int(squareButton_image.get_rect().height)))

            # Place the button image centered horizontally and towards the bottom vertically
            squareButton_x = (self.screen_width - squareButton_image.get_rect().width) / 2
            squareButton_y = self.screen_height - squareButton_image.get_rect().height - 50 
            screen.blit(squareButton_image, (squareButton_x, squareButton_y))

            # Add text to the button
            button_text = font.render("Select", True, (255, 255, 255))
            button_text_rect = button_text.get_rect(center=(self.screen_width/2, squareButton_y + squareButton_image.get_rect().height/2))
            screen.blit(button_text, button_text_rect)


        elif self.current_screen == "stats":

             # Load overlay image and center it on the screen
            overlayStats_image = pygame.image.load("assets/woodenOverlayStats.png").convert_alpha()
            overlayStats_x = (self.screen_width - overlayStats_image.get_rect().width) / 2
            overlayStats_y = (self.screen_height - overlayStats_image.get_rect().height) / 2 
            screen.blit(overlayStats_image, (overlayStats_x, overlayStats_y))

            #Agility
            if agility == 0:
                # Load bar0 and scale it
                bar0_image = pygame.image.load("assets/bar0.png").convert_alpha()
                bar0_image = pygame.transform.scale(bar0_image, (int(bar0_image.get_rect().width / 2.25), int(bar0_image.get_rect().height / 2.25)))

                # Place the bar0 image centered horizontally and towards the bottom vertically
                bar0_x = (self.screen_width - bar0_image.get_rect().width) * 1.25 / 2
                bar0_y = self.screen_height * 0.775 - bar0_image.get_rect().height / 2 
                screen.blit(bar0_image, (bar0_x, bar0_y))
            elif agility == 1:
                # Load bar1 and scale it
                bar1_image = pygame.image.load("assets/bar1.png").convert_alpha()
                bar1_image = pygame.transform.scale(bar1_image, (int(bar1_image.get_rect().width / 2.25), int(bar1_image.get_rect().height / 2.25)))

                # Place the bar1 image centered horizontally and towards the bottom vertically
                bar1_x = (self.screen_width - bar1_image.get_rect().width) * 1.25 / 2
                bar1_y = self.screen_height * 0.775 - bar1_image.get_rect().height / 2 
                screen.blit(bar1_image, (bar1_x, bar1_y))

                # Load bar0 and scale it
                bar0_image = pygame.image.load("assets/bar0.png").convert_alpha()
                bar0_image = pygame.transform.scale(bar0_image, (int(bar0_image.get_rect().width / 2.25), int(bar0_image.get_rect().height / 2.25)))

                # Place the bar0 image centered horizontally and towards the bottom vertically
                bar0_x = (self.screen_width - bar0_image.get_rect().width) * 1.25 / 2
                bar0_y = self.screen_height * 0.575 - bar0_image.get_rect().height / 2 
                screen.blit(bar0_image, (bar0_x, bar0_y))

                # Load bar0 and scale it
                bar0_image = pygame.image.load("assets/bar0.png").convert_alpha()
                bar0_image = pygame.transform.scale(bar0_image, (int(bar0_image.get_rect().width / 2.25), int(bar0_image.get_rect().height / 2.25)))

                # Place the bar0 image centered horizontally and towards the bottom vertically
                bar0_x = (self.screen_width - bar0_image.get_rect().width) * 1.25 / 2
                bar0_y = self.screen_height * 0.375 - bar0_image.get_rect().height / 2 
                screen.blit(bar0_image, (bar0_x, bar0_y))

                # Load bar0 and scale it
                bar0_image = pygame.image.load("assets/bar0.png").convert_alpha()
                bar0_image = pygame.transform.scale(bar0_image, (int(bar0_image.get_rect().width / 2.25), int(bar0_image.get_rect().height / 2.25)))

                # Place the bar0 image centered horizontally and towards the bottom vertically
                bar0_x = (self.screen_width - bar0_image.get_rect().width) * 1.25 / 2
                bar0_y = self.screen_height * 0.175 - bar0_image.get_rect().height / 2 
                screen.blit(bar0_image, (bar0_x, bar0_y))

        elif self.current_screen == "forest1":
            # Load overlay image and center it on the screen
            forest1_image = pygame.image.load("assets/gameBg1.png").convert_alpha()
            forest1_x = (self.screen_width - forest1_image.get_rect().width) / 2
            forest1_y = (self.screen_height - forest1_image.get_rect().height) / 2 
            screen.blit(forest1_image, (forest1_x, forest1_y))

             # Load and scale the character image
            character1_image = pygame.image.load("assets/characters/Fallen_Angels_1/PNG/IdleBlinking/frame0.png").convert_alpha()
            character1_image = pygame.transform.scale(character1_image, (int(character1_image.get_rect().width/2.75), int(character1_image.get_rect().height/2.75)))

            # Place the character in the middle
            character1_x = (self.screen_width  - character1_image.get_rect().width) / 2
            character1_y = (self.screen_height - character1_image.get_rect().height) / 2 
            screen.blit(character1_image, (character1_x, character1_y))



class Game:
    def __init__(self):
        screen_width = 1200
        screen_height = 800
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.game_state = GameState(screen_width, screen_height)  # Create a GameState instance
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            # Handle events
            for event in pygame.event.get():
                self.game_state.handle_event(event)

            # Update game state
            self.game_state.update()

            self.game_state.update()
            self.game_state.render(self.screen)

            pygame.display.update()
            self.clock.tick(60)
game = Game()
game.run()

class Enemy:
    def __init__(self, enemy_type, health, strength):
        self.enemy_type = enemy_type
        self.health = health
        self.strength = strength

class EnemySpawner:
    def __init__(self, game_state):
        self.game_state = game_state
        self.enemy_types = ["orc", "minotaur", "reaper"]
        
    def spawn_enemy(self):
        enemy_type = random.choice(self.enemy_types)
        if enemy_type == "orc":
            health = random.randint(10, 20)
            strength = random.randint(5, 10)
            enemy = Enemy("Orc", health, strength)
        elif enemy_type == "minotaur":
            health = random.randint(15, 25)
            strength = random.randint(8, 12)
            enemy = Enemy("Minotaur", health, strength)
        elif enemy_type == "reaper":
            health = random.randint(20, 30)
            strength = random.randint(10, 15)
            enemy = Enemy("Reaper", health, strength)
        return enemy
  
class Character(pygame.sprite.Sprite):
    def __init__(self, health, mana, strength, magic, defense, agility):
        super().__init__()
        self.health = health
        self.mana = mana
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.agility = agility