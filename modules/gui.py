import pygame

class Main:

    screen_size = (1000, 600)
    screen_title = "AutoColony"
    colours = { "black": (0,0,0),
                "white": (255,255,255),
                "red": (200,0,0),
                "green": (0,200,0),
                "bright_red": (255,0,0),
                "bright_green": (0,255,0)}

    def __init__(self, main):
        self.main = main

        pygame.init()
        self.window = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.screen_title)
        self.clock = pygame.time.Clock()

        self.window.fill(self.colours["white"])

        self.tile_size = 32
        self.tiles_along_x = self.screen_size[0] // self.tile_size
        self.tiles_along_y = self.screen_size[1] // self.tile_size
        self.tiles = None

    def post_post_init(self):
        self.x, self.y, self.z = self.main.MM.modules["worldgen"].world_middle_surface

        self.world = self.main.worldnp

        self.util = Utilities()

        self.util.load_image("soil", f"C:\Mohit\Projects\AutoColony\assets\images\soil.png")

        self.load_tiled_world()

    def load_tiled_world(self):

        x_start = self.x - (self.tiles_along_x // 2)
        x_stop = self.x + (self.tiles_along_x // 2)
        y_start = self.y - (self.tiles_along_y // 2)
        y_stop = self.y + (self.tiles_along_y // 2)

        self.tiles = self.world[x_start:x_stop, y_start:y_stop, self.z]
        x = 0
        y = 0
        for column in self.tiles:
            for tile in column:
                if tile == 1:
                    self.window.blit(self.util.images["soil"], (x*self.tile_size, y*self.tile_size))
                y += 1
            x += 1


        pygame.display.update()

    def quit(self):
        pygame.quit()

    def step(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main.quit()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.x += 1
                    self.load_tiled_world()
                elif event.key == pygame.K_LEFT:
                    self.x -= 1
                    self.load_tiled_world()
                elif event.key == pygame.K_UP:
                    self.y += 1
                    self.load_tiled_world()
                elif event.key == pygame.K_DOWN:
                    self.y -= 1
                    self.load_tiled_world()
                elif event.key == pygame.K_Q:
                    self.z += 1
                    self.load_tiled_world()
                elif event.key == pygame.K_W:
                    self.x -= 1
                    self.load_tiled_world()

        self.clock.tick(60)

class Utilities:
    images = {}
    sounds = {}

    def __init__(self):
        pass

    def load_image(self, name, location):
        self.images[name] = pygame.image.load(location)
    
    def load_sound(self, name, location):
        self.sounds[name] = pygame.mixer.Sound(location)

    def play_sound(self, name):
        pygame.mixer.Sound.play(self.sounds[name])
        pygame.mixer.music.stop()
