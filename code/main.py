from settings import *
from player import Player

class Game:
    def __init__(self):
        # SETUP ----------------------------------------------------------------
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivor Clone")

        self.clock = pygame.time.Clock()

        self.running = True

        # GROUPS ---------------------------------------------------------------
        self.all_sprites = pygame.sprite.Group()

        # SPRITES --------------------------------------------------------------
        self.player = Player((400,300), self.all_sprites)

    def run(self):
        while self.running:

            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # UPDATE -------------------------------------------------------
            self.all_sprites.update(dt)

            # DRAW ---------------------------------------------------------
            self.display_surface.fill("#000000")
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
