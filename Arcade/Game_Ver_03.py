import arcade
import random

SPRITE_SCALING_PLAYER = 0.12
SPRITE_SCALING_ENEMY = 0.9
SPRITE_SCALING_LASER = 0.3

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 675

BULLET_SPEED = 5
PLAYER_MOVEMENT_SPEED = 3
ENEMY_MOVEMENT_SPEED = 5

LEFT_BORDER = 40
RIGHT_BORDER = SCREEN_WIDTH - 40

ENEMY_LEFT_BORDER = 10
ENEMY_RIGHT_BORDER = SCREEN_WIDTH - 10

LASER_FILENAME = "laser.png"
PLAYER_FILENAME = "player_ship.png"

ENEMY_TEXTURE_11 = "enemy_1.1.png"
ENEMY_TEXTURE_12 = "enemy_1.2.png"
ENEMY_TEXTURE_21 = "enemy_2.1.png"
ENEMY_TEXTURE_22 = "enemy_2.2.png"
ENEMY_TEXTURE_31 = "enemy_3.1.png"
ENEMY_TEXTURE_32 = "enemy_3.2.png"
ENEMY_TEXTURE_41 = "enemy_4.1.png"
ENEMY_TEXTURE_42 = "enemy_4.2.png"
ENEMY_TEXTURE_51 = "enemy_5.1.png"
ENEMY_TEXTURE_52 = "enemy_5.2.png"
ENEMY_TEXTURE_61 = "enemy_6.1.png"
ENEMY_TEXTURE_62 = "enemy_6.2.png"

ENEMY_MOTHERSHIP = "enemy_mothership.png"

GAME_STATE = True


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
    enemy_1 = True
    enemy_2 = False

    def __init__(self, texture_1, texture_2, sprite_scaling, center_x, center_y, change_x):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x

        self.scale = sprite_scaling

        self.textures = []

        texture = arcade.load_texture(texture_2)

        self.textures.append(texture)

        texture = arcade.load_texture(texture_1)

        self.textures.append(texture)

        self.texture = texture

    def update(self):

        self.center_x += self.change_x

        if Enemy.enemy_1:

            self.texture = self.textures[1]

        elif Enemy.enemy_2:

            self.texture = self.textures[0]


class Bullet(arcade.Sprite):

    def __init__(self, filename, sprite_scaling, change_y):
        super().__init__(filename, sprite_scaling)
        self.change_y = change_y

    def update(self):
        self.center_y += self.change_y


class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Game : ")

        self.game_state = GAME_STATE

        self.background = None

        self.enemy_list = None
        self.bullet_list = None
        self.armor_list = None

        self.player_sprite = None
        self.player_list = None
        self.mothership = None
        self.mothership_list = None

        self.left_key = False
        self.right_key = False
        self.last_key = ""
        self.isSpacePressed = 0

        self.enemy_left = False
        self.enemy_right = True
        self.enemy_down = False

        self.enemy_switch_left = True
        self.enemy_switch_right = True

        self.score = 0
        self.enemy_score_dict = dict()

        self.del_armor = False

        self.frame_count = 0
        self.mother_frame_count = 0
        self.odds = 0
        # self.laser_sound = None

    def setup(self):

        self.background = arcade.csscolor.BLACK

        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.armor_list = arcade.SpriteList()
        self.mothership_list = arcade.SpriteList()

        self.player_sprite = Ship(PLAYER_FILENAME, SPRITE_SCALING_PLAYER, 375, 30, 0)
        self.player_list.append(self.player_sprite)

        self.create_armor(SCREEN_WIDTH / 4 - 46.5, 100)
        self.create_armor(2 * SCREEN_WIDTH / 4 - 30, 100)
        self.create_armor(3 * SCREEN_WIDTH / 4 - 13.5, 100)

        self.create_enemies()

        self.odds = random.randint(15, 20)

        # self.laser_sound = arcade.load_sound("sfx_laser1.ogg")

    def on_draw(self):

        arcade.start_render()

        self.player_list.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()
        self.armor_list.draw()
        self.mothership_list.draw()

        score = "Score : " + str(self.score)
        arcade.draw_text(score, 10, 650, arcade.color.WHITE, 14)

        if not self.game_state:
            arcade.draw_text("GAME OVER", 220, 350, arcade.color.WHITE, 55)

    def update(self, delta_time):

        if not self.game_state:
            return

        self.player_list.update()
        self.bullet_list.update()
        self.enemy_list.update()
        self.armor_list.update()
        self.mothership_list.update()

        self.handle_collision_bullet()
        self.delete_armor()
        self.move_enemies_logic()
        self.create_enemy_mothership()

    def create_enemies(self):
        for i in range(6):
            enemy = Enemy(ENEMY_TEXTURE_11, ENEMY_TEXTURE_12, SPRITE_SCALING_ENEMY, (i + 1) * 100, 570, 0)
            self.enemy_list.append(enemy)
            self.enemy_score_dict[enemy] = 30
        for i in range(6):
            enemy = Enemy(ENEMY_TEXTURE_21, ENEMY_TEXTURE_22, SPRITE_SCALING_ENEMY, (i + 1) * 100, 500, 0)
            self.enemy_list.append(enemy)
            self.enemy_score_dict[enemy] = 25
        for i in range(6):
            enemy = Enemy(ENEMY_TEXTURE_31, ENEMY_TEXTURE_32, SPRITE_SCALING_ENEMY, (i + 1) * 100, 430, 0)
            self.enemy_list.append(enemy)
            self.enemy_score_dict[enemy] = 20
        for i in range(6):
            enemy = Enemy(ENEMY_TEXTURE_41, ENEMY_TEXTURE_42, SPRITE_SCALING_ENEMY, (i + 1) * 100, 360, 0)
            self.enemy_list.append(enemy)
            self.enemy_score_dict[enemy] = 15
        for i in range(6):
            enemy = Enemy(ENEMY_TEXTURE_51, ENEMY_TEXTURE_52, SPRITE_SCALING_ENEMY, (i + 1) * 100, 290, 0)
            self.enemy_list.append(enemy)
            self.enemy_score_dict[enemy] = 10
        for i in range(6):
            enemy = Enemy(ENEMY_TEXTURE_61, ENEMY_TEXTURE_62, SPRITE_SCALING_ENEMY, (i + 1) * 100, 220, 0)
            self.enemy_list.append(enemy)
            self.enemy_score_dict[enemy] = 5

    def create_armor(self, start_x, start_y):

        width = 5
        height = 30

        def create_single_armor(x, y, a, b):
            for i in range(x):
                for j in range(y):
                    armor_sprite = arcade.SpriteSolidColor(width, height, arcade.color_from_hex_string("#FC4242"))
                    armor_sprite.center_x = start_x + a * width + i * width
                    armor_sprite.center_y = start_y + b * height + j * height
                    self.armor_list.append(armor_sprite)

        # x: breadth of rectangle ,y: length of rectangle, a: shift in x, b: shift in y
        create_single_armor(1, 1, 0, 0)
        create_single_armor(2, 2, 1, 0)
        create_single_armor(5, 2, 3, 0.25)
        create_single_armor(2, 2, 8, 0)
        create_single_armor(1, 1, 10, 0)

    def delete_armor(self):
        if self.del_armor:
            for i in self.armor_list:
                i.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:

            bullet = Bullet(LASER_FILENAME, SPRITE_SCALING_LASER, BULLET_SPEED)

            bullet.center_x = self.player_sprite.center_x
            bullet.center_y = self.player_sprite.top + 10

            if len(self.bullet_list) == 0:
                self.bullet_list.append(bullet)
                # arcade.play_sound(self.laser_sound)

        if key in [arcade.key.LEFT, arcade.key.A]:
            self.left_key = True
            self.last_key = "left"

        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.right_key = True
            self.last_key = "right"

        if key == arcade.key.Q:
            if not self.game_state:
                exit()

        self.move_player()

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.LEFT, arcade.key.A]:
            self.left_key = False

        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.right_key = False

        self.move_player()

    def move_player(self):

        if self.left_key and not self.right_key:
            if self.player_sprite.left > LEFT_BORDER:
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

        elif self.right_key and not self.left_key:
            if self.player_sprite.right < RIGHT_BORDER:
                self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        elif self.left_key and self.right_key:
            if self.last_key == "left":
                if self.player_sprite.left > LEFT_BORDER:
                    self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

            elif self.last_key == "right":
                if self.player_sprite.right < RIGHT_BORDER:
                    self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        else:
            self.player_sprite.change_x = 0

    def movement_border_enemies(self, z):

        if self.enemy_down:
            for ene in self.enemy_list:
                ene.center_y -= z
            self.enemy_down = False
        else:
            if self.enemy_left and not self.enemy_right:
                for ene in self.enemy_list:
                    ene.change_x = -ENEMY_MOVEMENT_SPEED

            if self.enemy_right and not self.enemy_left:
                for ene in self.enemy_list:
                    ene.change_x = ENEMY_MOVEMENT_SPEED

    def movement_enemies(self, x, y, z):
        self.frame_count += 1

        if self.frame_count % x == 0:
            self.movement_border_enemies(z)
            Enemy.enemy_1 = not Enemy.enemy_1
            Enemy.enemy_2 = not Enemy.enemy_2

        if self.frame_count % y == 0:
            for ene in self.enemy_list:
                ene.change_x = 0
            self.frame_count = 0

    def move_enemies_logic(self):

        for enemy in self.enemy_list:

            if enemy.right >= ENEMY_RIGHT_BORDER and self.enemy_switch_right:
                self.enemy_left = True
                self.enemy_right = False
                self.enemy_down = True
                self.enemy_switch_right = False
                self.enemy_switch_left = True

            if enemy.left <= ENEMY_LEFT_BORDER and self.enemy_switch_left:
                self.enemy_left = False
                self.enemy_right = True
                self.enemy_down = True
                self.enemy_switch_left = False
                self.enemy_switch_right = True

            if enemy.bottom < 160:
                self.del_armor = True

            if enemy.bottom <= self.player_sprite.top:
                self.game_state = False

        length = len(self.enemy_list)

        if length == 0:
            self.game_state = False

        if length > 20:
            self.movement_enemies(40, 43, 10)

        elif 10 < length <= 20:
            self.movement_enemies(25, 28, 12)

        elif 3 < length <= 10:
            self.movement_enemies(15, 18, 14)

        elif 1 < length <= 3:
            self.movement_enemies(7, 10, 16)

        elif length == 1:
            self.movement_enemies(1, 4, 18)

    def create_enemy_mothership(self):

        dire = random.choice([1, -1])
        self.mother_frame_count += 1

        if self.mother_frame_count % (60 * self.odds) == 0 and len(self.mothership_list) == 0:
            if dire == 1:
                self.mothership = Enemy(ENEMY_MOTHERSHIP, ENEMY_MOTHERSHIP, SPRITE_SCALING_ENEMY * 1.5, 0, 620, 1.5)
            else:
                self.mothership = Enemy(ENEMY_MOTHERSHIP, ENEMY_MOTHERSHIP, SPRITE_SCALING_ENEMY * 1.5, 900, 620, -1.5)
            self.mothership_list.append(self.mothership)
            self.odds = random.randint(15, 20)

        if len(self.mothership_list) == 1:
            if self.mothership.left > SCREEN_WIDTH or self.mothership.right < 0:
                self.mothership.remove_from_sprite_lists()
                self.mother_frame_count = 0

    def handle_collision_bullet(self):

        for bullet in self.bullet_list:

            hit_list_enemy = arcade.check_for_collision_with_list(bullet, self.enemy_list)

            if len(hit_list_enemy) > 0:
                bullet.remove_from_sprite_lists()

            for enemy in hit_list_enemy:
                enemy.remove_from_sprite_lists()
                self.score += self.enemy_score_dict[enemy]

            hit_list_mothership = arcade.check_for_collision_with_list(bullet, self.mothership_list)

            if len(hit_list_mothership) > 0:
                bullet.remove_from_sprite_lists()

            for mothership in hit_list_mothership:
                mothership.remove_from_sprite_lists()
                self.mother_frame_count = 0
                self.score += 200

            hit_list_armor = arcade.check_for_collision_with_list(bullet, self.armor_list)

            if len(hit_list_armor) > 0:
                bullet.remove_from_sprite_lists()

            for armor in hit_list_armor:
                armor.remove_from_sprite_lists()

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()


def main():
    window = Game()
    window.setup()
    arcade.run()


main()
