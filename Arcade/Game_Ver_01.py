import arcade
from threading import Timer

SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_ENEMY = 0.1
SPRITE_SCALING_LASER = 0.3

ENEMY_COUNT = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 5
MOVEMENT_SPEED = 10

LEFT_BORDER = 20
RIGHT_BORDER = SCREEN_WIDTH - 20


class Ship(arcade.Sprite):

    def __init__(self, filename, sprite_scaling, center_x, center_y, change_x):
        super().__init__(filename, sprite_scaling)

        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x

    def update(self):
        self.center_x += self.change_x

        if self.left < LEFT_BORDER or self.right > RIGHT_BORDER:
            self.change_x = 0


class Enemy(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.center_y = 500


class Bullet(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

    def update(self):
        self.center_y += BULLET_SPEED


class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Game : ")

        arcade.set_background_color(arcade.csscolor.BLACK)

        self.enemy_list = None
        self.bullet_list = None

        self.left_key = False
        self.right_key = False
        self.last_key = ""
        self.isSpacePressed = 0

        self.score = 0
        self.player_sprite = None

        self.delay_timer = None
        self.laser_sound = arcade.load_sound("sfx_laser1.ogg")

    def setup(self):

        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.player_sprite = Ship("player_ship.png", SPRITE_SCALING_PLAYER, 375, 70, 0)

        self.create_enemies()

    def create_enemies(self):

        for i in range(1, ENEMY_COUNT + 1):
            enemy = Enemy("enemy_1.1.png", SPRITE_SCALING_ENEMY)
            enemy.center_x = (i - (1 / 2)) * int(SCREEN_WIDTH / ENEMY_COUNT)
            self.enemy_list.append(enemy)

        if self.delay_timer is not None:
            self.delay_timer.cancel()
            self.delay_timer = None

    def on_draw(self):

        arcade.start_render()

        self.player_sprite.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()

        score = "Score : " + str(self.score)
        arcade.draw_text(score, 10, 580, arcade.color.WHITE, 14)

    def update(self, delta_time):

        self.player_sprite.update()
        self.bullet_list.update()
        self.enemy_list.update()

        for bullet in self.bullet_list:

            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                self.score += 1

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        if len(self.enemy_list) == 0 and self.delay_timer is None:
            self.delay_timer = Timer(1, self.create_enemies, ())
            self.delay_timer.start()

    def move(self):

        if self.left_key and not self.right_key:
            if self.player_sprite.left > LEFT_BORDER:
                self.player_sprite.change_x = -MOVEMENT_SPEED

        elif self.right_key and not self.left_key:
            if self.player_sprite.right < RIGHT_BORDER:
                self.player_sprite.change_x = MOVEMENT_SPEED

        elif self.left_key and self.right_key:
            if self.last_key == "left":
                if self.player_sprite.left > LEFT_BORDER:
                    self.player_sprite.change_x = -MOVEMENT_SPEED

            elif self.last_key == "right":
                if self.player_sprite.right < RIGHT_BORDER:
                    self.player_sprite.change_x = MOVEMENT_SPEED

        else:
            self.player_sprite.change_x = 0

    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:

            bullet = Bullet("laser.png", SPRITE_SCALING_LASER)

            bullet.center_x = self.player_sprite.center_x
            bullet.center_y = self.player_sprite.top + 10

            if len(self.bullet_list) <= 1:
                self.bullet_list.append(bullet)
                arcade.play_sound(self.laser_sound)

        if key in [arcade.key.LEFT, arcade.key.A]:
            self.left_key = True
            self.last_key = "left"

        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.right_key = True
            self.last_key = "right"

        Game.move(self)

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.LEFT, arcade.key.A]:
            self.left_key = False

        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.right_key = False

        Game.move(self)


def main():
    window = Game()
    window.setup()
    arcade.run()


main()
