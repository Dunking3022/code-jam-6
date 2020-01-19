from kivy.app import App
from kivy.core.window import Window

from engine.engine import Engine
from engine.sprite import Sprite, Player, Terrain
from engine.perlin import perlin_array


class MyGame(Engine):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player = Player('testimg.png', [i / 2 for i in Window.size])
        self.map = perlin_array()

        for i in range(-2000, 7000, 1000):
            for j in range(-2000, 6000, 1000):
                self.add_sprite(Terrain(self.map, (i, j)))
        self.add_sprite(self.player)

    def update(self, dt: float) -> None:
        self.player.pos = [i / 2 for i in Window.size]
        if 'w' in self.pressed_keys:
            for i in self.sprites:
                i.vel_y -= 10
        if 's' in self.pressed_keys:
            for i in self.sprites:
                i.vel_y += 10
        if 'a' in self.pressed_keys:
            for i in self.sprites:
                i.vel_x += 10
        if 'd' in self.pressed_keys:
            for i in self.sprites:
                i.vel_x -= 10


class Application(App):
    """Main application class."""

    def build(self):
        """Return the root widget."""
        Window.clearcolor = (51 / 255, 51 / 255, 51 / 255, 1)
        Window.fullscreen = "auto"
        self.title = "Primal"
        game = MyGame()
        return game


if __name__ == "__main__":
    print(Window.size)
    Application().run()