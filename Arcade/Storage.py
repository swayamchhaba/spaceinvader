# =====================================================================================================================

# snowmannnnnnnnnnnnnnnnnnnnnnnnnnn
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snowman(x, y):
    # Snow
    arcade.draw_circle_filled(x, y + 60, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y + 140, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y + 200, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, y + 210, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, y + 210, 5, arcade.color.BLACK)

    # Smile
    arcade.draw_point(x, y + 175, arcade.color.RED, 5)
    arcade.draw_point(x - 10, y + 180, arcade.color.RED, 5)
    arcade.draw_point(x + 10, y + 180, arcade.color.RED, 5)
    arcade.draw_point(x - 20, y + 185, arcade.color.RED, 5)
    arcade.draw_point(x + 20, y + 185, arcade.color.RED, 5)

    # Nose
    arcade.draw_triangle_filled(x, y + 200, x - 10, y + 190, x + 10, y + 190, arcade.color.RED)

    # reference point
    arcade.draw_point(x, y, arcade.color.RED, 5)


def on_draw(delta_time):

    arcade.start_render()

    draw_grass()
    draw_snowman(on_draw.snow_person1_x, 140)


    on_draw.snow_person1_x += 1

on_draw.snow_person1_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    # Draw the ground
    draw_grass()

    # Draw a snow person
    draw_snowman(300, 100)

    #  Finish and run
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


main()
"""

# =====================================================================================================================

# first drawing
"""
import arcade

window_height = 600
window_width = 800
# window
arcade.open_window(window_width, window_height, "Idk What To Name This")
arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
# start drawing
arcade.start_render()
# draw grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.csscolor.FOREST_GREEN)
# draw tree 1
arcade.draw_rectangle_filled(100, 230, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 285, 30, arcade.csscolor.DARK_GREEN)
# draw tree 2
arcade.draw_rectangle_filled(200, 230, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 295, 60, 80, arcade.csscolor.DARK_GREEN)
# draw tree 3
arcade.draw_rectangle_filled(300, 230, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 260, 80, 100, arcade.csscolor.DARK_GREEN, -20, 200)
# draw tree 4
arcade.draw_rectangle_filled(400, 230, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 350, 370, 260, 430, 260, arcade.csscolor.DARK_GREEN)
# draw tree 5
arcade.draw_rectangle_filled(500, 230, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 340), (480, 300), (470, 260), (530, 260), (520, 300)), arcade.csscolor.DARK_GREEN)
# draw sun
arcade.draw_circle_filled(700, 500, 70, arcade.csscolor.LIGHT_GOLDENROD_YELLOW)
# draw sun's straight lines
arcade.draw_line(700, 500, 800, 500, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 3)
arcade.draw_line(700, 500, 700, 350, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 3)
arcade.draw_line(700, 500, 550, 500, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 3)
arcade.draw_line(700, 500, 700, 600, arcade.csscolor.LIGHT_GOLDENROD_YELLOW, 3)
# draw sun's diagonal lines
arcade.draw_line(start_x=700, start_y=500, end_x=770, end_y=570, color=arcade.color.LIGHT_GOLDENROD_YELLOW,
                 line_width=3)
arcade.draw_line(700, 500, 770, 430, arcade.color.LIGHT_GOLDENROD_YELLOW, 3)
arcade.draw_line(700, 500, 630, 570, arcade.color.LIGHT_GOLDENROD_YELLOW, 3)
arcade.draw_line(700, 500, 630, 430, arcade.color.LIGHT_GOLDENROD_YELLOW, 3)
# draw text
arcade.draw_text("This is my first drawing lol", 200, 100, arcade.csscolor.PALE_VIOLET_RED, 25)
# grid
starting_y = 0
while starting_y <= 600:
    arcade.draw_line(start_x=0, start_y=starting_y, end_x=10, end_y=starting_y, color=arcade.csscolor.BLACK,
                     line_width=3)
    starting_y += 20
starting_y = 0
while starting_y <= 600:
    arcade.draw_line(start_x=0, start_y=starting_y, end_x=5, end_y=starting_y, color=arcade.csscolor.BLACK,
                     line_width=3)
    starting_y += 10
starting_x = 0
while starting_x <= 800:
    arcade.draw_line(start_x=starting_x, start_y=0, end_x=starting_x, end_y=10, color=arcade.csscolor.BLACK,
                     line_width=3)
    starting_x += 20
starting_x = 0
while starting_x <= 800:
    arcade.draw_line(start_x=starting_x, start_y=0, end_x=starting_x, end_y=5, color=arcade.csscolor.BLACK,
                     line_width=3)
    starting_x += 10
starting_y = 0
while starting_y <= 600:
    y = str(starting_y)
    arcade.draw_text(text=y, start_x=15, start_y=(starting_y - 5), color=arcade.csscolor.BLACK, font_size=10)
    starting_y += 40
# end drawing
arcade.finish_render()
arcade.run()
"""

# =====================================================================================================================

# bouncing ball
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)

        self.ball_list = []

        ball1 = Ball(50, 50, 5, 5, 15, arcade.csscolor.LIGHT_SKY_BLUE)
        self.ball_list.append(ball1)
        ball2 = Ball(50, 50, 3, 3, 15, arcade.csscolor.LAVENDER)
        self.ball_list.append(ball2)
        ball3 = Ball(50, 50, 8, 8, 15, arcade.csscolor.BLACK)
        self.ball_list.append(ball3)

    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw()

    def update(self, delta_time):
        for ball in self.ball_list:
            ball.update()


def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Some Title")
    arcade.run()


main()
"""

# =====================================================================================================================

# taking mouse input
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ball:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)
        self.set_mouse_visible(False)

        self.ball = Ball(50, 50, 15, arcade.csscolor.LIGHT_SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.position_x = x
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ball.color = arcade.color.GREEN
        else:
            self.ball.color = arcade.color.LIGHT_SKY_BLUE


def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Some Title")
    arcade.run()


main()
"""

# =====================================================================================================================

# taking all 4 keys input (terrible motion)
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 10


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < 16 or self.position_x > SCREEN_WIDTH - 16:
            self.change_x = 0
        if self.position_y < 16 or self.position_y > SCREEN_HEIGHT - 16:
            self.change_y = 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)

        self.ball = Ball(50, 50, 0, 0, 15, arcade.csscolor.LIGHT_SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.A:
            self.ball.change_x = -MOVEMENT_SPEED

        elif key == arcade.key.D:
            self.ball.change_x = MOVEMENT_SPEED

        elif key == arcade.key.W:
            self.ball.change_y = MOVEMENT_SPEED

        elif key == arcade.key.S:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.ball.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.ball.change_y = 0


def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Some Title")
    arcade.run()


main()
"""

# =====================================================================================================================

# taking 2 keys inputs (fluid motion)
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 10


class Ball:
    def __init__(self, position_x, position_y, change_x, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_x += self.change_x

        if self.position_x < 16 or self.position_x > SCREEN_WIDTH - 16:
            self.change_x = 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)
        self.left = False
        self.right = False
        self.last_key = ""

        self.ball = Ball(50, 50, 0, 15, arcade.csscolor.LIGHT_SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def move(self):
        if self.left and not self.right:
            self.ball.change_x = -MOVEMENT_SPEED
        elif self.right and not self.left:
            self.ball.change_x = MOVEMENT_SPEED
        elif self.left and self.right:
            if self.last_key == "left":
                self.ball.change_x = -MOVEMENT_SPEED
            elif self.last_key == "right":
                self.ball.change_x = MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:
            self.left = True
            self.last_key = "left"
        elif key == arcade.key.RIGHT:
            self.right = True
            self.last_key = "right"

        Game.move(self)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left = False
        elif key == arcade.key.RIGHT:
            self.right = False

        Game.move(self)


def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Some Title")
    arcade.run()


main()
"""

# =====================================================================================================================

# sound
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHEAT)
        self.laser_sound = arcade.load_sound("laser.wav")
        self.laser_sound_player = None

    def on_draw(self):
        arcade.start_render()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.S:
            if not self.laser_sound_player or not self.laser_sound_player.playing:
                self.laser_sound_player = arcade.play_sound(self.laser_sound)


def main():
    window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Some Title")
    arcade.run()


main()
"""

# =====================================================================================================================

# bouncy coin collector game
"""
import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_PASTEL_PURPLE)

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

    def setup(self):

        self.score = 0

        self.player_sprite = arcade.Sprite("player_ship.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 20
        self.player_sprite.center_y = 20
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = Coin("coin_star.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)
            if coin.change_x == 0 or coin.change_y == 0:
                coin.change_x = 1
                coin.change_y = 1
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

        score = f"Score: {self.score}"
        arcade.draw_text(score, 10, 20, arcade.color.BLACK, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        self.coin_list.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Some Title")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
"""

# =====================================================================================================================

# alt coin pattern
"""
import arcade

SPRITE_SCALING_COIN = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_PASTEL_PURPLE)

        self.coin_list = arcade.SpriteList()

        self.set_mouse_visible(False)

    def setup(self):
        for i in range(1, 6):
            coin = Coin("coin_star.png", SPRITE_SCALING_COIN)
            coin.center_x = 400
            coin.center_y = i * 100 - 50
            coin.change_x = 5
            coin.change_y = 0
            self.coin_list.append(coin)
        for i in range(1, 6):
            coin = Coin("coin_star.png", SPRITE_SCALING_COIN)
            coin.center_x = 400
            coin.center_y = i * 100
            coin.change_x = -5
            coin.change_y = 0
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()

    def update(self, delta_time):
        self.coin_list.update()


def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Some Title")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
"""

# =====================================================================================================================

# shooting lasers
"""
import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.4
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites and Bullets Demo")

        self.player_list = None
        self.coin_list = None
        self.bullet_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("player_ship.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coin_star.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(120, SCREEN_HEIGHT)

            self.coin_list.append(coin)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):

        arcade.start_render()

        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        bullet = arcade.Sprite("laser.png", SPRITE_SCALING_LASER)

        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        bullet.change_y = BULLET_SPEED

        self.bullet_list.append(bullet)

    def update(self, delta_time):

        self.coin_list.update()
        self.bullet_list.update()

        for bullet in self.bullet_list:

            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
"""

# =====================================================================================================================

# textures
"""
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Face Left or Right Example"

MOVEMENT_SPEED = 5

TEXTURE_1 = 0

TEXTURE_2 = 1


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.scale = SPRITE_SCALING

        self.textures = []

        texture = arcade.load_texture("enemy.png")

        self.textures.append(texture)

        texture = arcade.load_texture("player_ship.png")

        self.textures.append(texture)

        self.texture = texture

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x < 0:

            self.texture = self.textures[TEXTURE_1]

        elif self.change_x > 0:

            self.texture = self.textures[TEXTURE_2]


class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.player_sprite_list = None

        self.player_sprite = None

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        self.player_sprite_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_sprite_list.append(self.player_sprite)

    def on_draw(self):
        self.clear()

        self.player_sprite_list.draw()

    def on_update(self, delta_time):
        self.player_sprite_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
"""
# =====================================================================================================================
