import pygame
import time


#  window settings
WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
FPS = 60
SPACE = pygame.transform.scale(pygame.image.load("Assets/space.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))

# border settings
BORDER_COLOR = 0, 0, 0
BORDER_WIDTH = 10
BORDER = pygame.Rect(WINDOW_WIDTH // 2 - BORDER_WIDTH // 2, 0, BORDER_WIDTH, WINDOW_HEIGHT)

# spaceship settings
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 45
MOVEMENT_SPEED = 2
FUCKED_UP_IMAGE = 10

# bullet settings
MAX_BULLETS = 4
RED_BULLET_COLOR = 255, 0, 0
YELLOW_BULLET_COLOR = 255, 255, 0
BULLETS_MOVEMENT_SPEED = 10
BULLET_WIDTH, BULLET_HEIGHT = 20, 10


RED_BULLET = pygame.transform.scale(pygame.image.load("Assets/red_laser_shot.png"), (BULLET_WIDTH, BULLET_HEIGHT))
YELLOW_BULLET = pygame.transform.scale(pygame.image.load("Assets/yellow_laser_shot.png"), (BULLET_WIDTH, BULLET_HEIGHT))

# health settings
STARTER_HEALTH = 10
FONT_COLOR = 255, 255, 255


class Spaceship:
    def __init__(self, x, y, path, angle, directions, health=STARTER_HEALTH):
        self.x = x
        self.y = y
        self.image = pygame.image.load(path)
        self.spaceship = pygame.transform.rotate(
            pygame.transform.scale(self.image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), angle)
        self.health = health
        self.directions = directions

        self.bullets = list()

        if x < WINDOW_WIDTH // 2:
            self.side = "left"
        else:
            self.side = "right"

    def shoot_bullet(self, bullet_fire_sound):
        if self.side == "left":
            bullet = pygame.Rect(self.x + SPACESHIP_WIDTH, self.y + SPACESHIP_HEIGHT // 2 - BULLET_HEIGHT // 2,
                                 BULLET_WIDTH, BULLET_HEIGHT)
        else:
            bullet = pygame.Rect(self.x, self.y + SPACESHIP_HEIGHT // 2 - BULLET_HEIGHT // 2, BULLET_WIDTH,
                                 BULLET_HEIGHT)

        self.bullets.append(bullet)
        bullet_fire_sound.play()

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def get_bullets(self):
        return self.bullets

    def move_spaceship(self, keys_pressed):
        if keys_pressed[self.directions["left"]] and valid_move(self.x - MOVEMENT_SPEED, self.side) > 0:  # left
            self.x -= MOVEMENT_SPEED

        if keys_pressed[self.directions["right"]] and valid_move(
                self.x + MOVEMENT_SPEED + SPACESHIP_WIDTH - FUCKED_UP_IMAGE, self.side):  # right
            self.x += MOVEMENT_SPEED

        if keys_pressed[self.directions["up"]] and self.y - MOVEMENT_SPEED > 0:  # up
            self.y -= MOVEMENT_SPEED

        if keys_pressed[self.directions["down"]] and self.y + MOVEMENT_SPEED + SPACESHIP_HEIGHT + FUCKED_UP_IMAGE < WINDOW_HEIGHT:  # down
            self.y += MOVEMENT_SPEED

    def get_health(self):
        return self.health

    def get_coordinates(self):
        return self.x, self.y

    def move_bullets_and_check_hit_with_other_spaceship(self, spaceship, bullet_hit_sound):
        for bullet in self.bullets:
            if self.side == "left":
                bullet.x += BULLETS_MOVEMENT_SPEED
            else:
                bullet.x -= BULLETS_MOVEMENT_SPEED

            spaceship_x, spaceship_y = spaceship.get_coordinates()

            if check_hit_of_bullet_in_spaceship(spaceship_x, spaceship_y, bullet.x, bullet.y):
                self.remove_bullet(bullet)
                spaceship.bullet_hit()

                bullet_hit_sound.play()

            elif bullet.x > WINDOW_WIDTH or bullet.x < 0:
                self.remove_bullet(bullet)

    def bullet_hit(self):
        self.health -= 1


def check_hit_of_bullet_in_spaceship(x_spaceship, y_spaceship, x_bullet, y_bullet):
    return x_spaceship <= x_bullet + BULLET_WIDTH <= x_spaceship + SPACESHIP_WIDTH and (
            y_spaceship <= y_bullet + BULLET_HEIGHT <= y_spaceship + SPACESHIP_HEIGHT or y_spaceship <= y_bullet <= y_spaceship + SPACESHIP_HEIGHT)


def valid_move(new_x, side):
    if side == "left":
        return 0 <= new_x <= BORDER.x

    return BORDER.x + BORDER_WIDTH <= new_x <= WINDOW_WIDTH


def draw_window(window, red, yellow):
    pygame.font.init()

    window.blit(SPACE, (0, 0))  # fill the window with the background image
    pygame.draw.rect(window, BORDER_COLOR, BORDER)  # draw border

    health_font = pygame.font.SysFont("comicsans", 40)
    red_health_text = health_font.render(f"Health: {red.get_health()}", 1, FONT_COLOR)
    yellow_health_text = health_font.render(f"Health: {yellow.get_health()}", 1, FONT_COLOR)

    window.blit(red_health_text, (WINDOW_WIDTH - red_health_text.get_width() - 10, 10))
    window.blit(yellow_health_text, (10, 10))

    window.blit(yellow.spaceship, yellow.get_coordinates())
    window.blit(red.spaceship, red.get_coordinates())

    for bullet in red.get_bullets():
        window.blit(RED_BULLET, (bullet.x, bullet.y))

    for bullet in yellow.get_bullets():
        window.blit(YELLOW_BULLET, (bullet.x, bullet.y))

    pygame.display.update()  # update the window


def draw_winner(window, winner_text):
    pygame.font.init()

    winner_font = pygame.font.SysFont("comicsans", 100)
    draw_text = winner_font.render(winner_text, 1, FONT_COLOR)
    window.blit(draw_text,
                (WINDOW_WIDTH // 2 - draw_text.get_width() // 2, WINDOW_HEIGHT // 2 - draw_text.get_height() // 2))

    pygame.display.update()
    pygame.time.delay(3000)


def find_index_of_move(lst_of_moves, move_to_find):
    index = 0
    was_found = False

    for idx, val in enumerate(lst_of_moves):
        if val[0] == move_to_find:
            index = idx
            was_found = True
            break

    if was_found:
        return index
    return None


def get_move(red, yellow):
    lst_of_moves = [(0, -1), (0, 1)]

    yellow_x, yellow_y = yellow.get_coordinates()

    for i in lst_of_moves:
        new_y = yellow_y + i[1] * MOVEMENT_SPEED

        if (new_y < 0) or ((new_y + SPACESHIP_HEIGHT + FUCKED_UP_IMAGE) > WINDOW_HEIGHT):
            lst_of_moves.remove(i)

    move_to_play = list()

    if len(red.get_bullets()) == 0:  # offense
        if len(lst_of_moves) != 1:
            if red.y == yellow_y:
                move_to_play.append((0, 0))
            elif red.y < yellow_y:
                move_to_play.append((0, -1))
            else:
                move_to_play.append((0, 1))

        else:
            move_to_play.append(lst_of_moves[0])

        if yellow_x + MOVEMENT_SPEED + SPACESHIP_WIDTH - FUCKED_UP_IMAGE <= BORDER.x:
            move_to_play.append((1, 0))

    else:  # defense
        if len(lst_of_moves) != 1:
            upper_half_counter, bottom_half_counter = 0, 0

            for bullet in red.get_bullets():
                if yellow_y <= bullet.y + BULLET_HEIGHT <= yellow_y + SPACESHIP_HEIGHT or yellow_y <= bullet.y <= yellow_y + SPACESHIP_HEIGHT:
                    if ((yellow_y + SPACESHIP_HEIGHT / 2) - (bullet.y + BULLET_HEIGHT / 2)) > 0:  # the bullet is in the upper half
                        if bullet.y + BULLET_HEIGHT < WINDOW_HEIGHT - SPACESHIP_HEIGHT:
                            upper_half_counter += 1

                        else:
                            bottom_half_counter += 100

                    else:  # the bullet is in the bottom half
                        if bullet.y > SPACESHIP_HEIGHT:
                            bottom_half_counter += 1

                        else:
                            upper_half_counter += 100

            if upper_half_counter == bottom_half_counter:
                pass

            elif upper_half_counter > bottom_half_counter:
                move_to_play.append((0, 1))

            else:
                move_to_play.append((0, -1))
        else:
            move_to_play.append(lst_of_moves[0])

        if yellow_x - MOVEMENT_SPEED >= 0:
            move_to_play.append((-1, 0))  # if the move valid, add going left

    whether_to_shoot = (red.get_coordinates()[0] == yellow.get_coordinates()[0]) or len(yellow.get_bullets()) <= 3

    return move_to_play, whether_to_shoot


def main():
    pygame.mixer.init()
    BULLET_HIT_SOUND = pygame.mixer.Sound("Assets/Grenade+1.mp3")
    BULLET_FIRE_SOUND = pygame.mixer.Sound("Assets/Gun+Silencer.mp3")

    start_time = time.time()
    previous_time = 0

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Star Fighters Game")

    red = Spaceship(700, 300, "Assets/spaceship_red.png", 270,
                    {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP, "down": pygame.K_DOWN})
    yellow = Spaceship(100, 300, "Assets/spaceship_yellow.png", 90,
                       {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s})

    clock = pygame.time.Clock()

    fire_time = 0.75
    to_exit = False
    can_start_game = False
    while not to_exit:
        if yellow.health < 4:
            fire_time = 0.4

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                to_exit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                can_start_game = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RCTRL and len(red.get_bullets()) < MAX_BULLETS and can_start_game:
                red.shoot_bullet(BULLET_FIRE_SOUND)

        if can_start_game:
            keys_pressed = pygame.key.get_pressed()

            red.move_spaceship(keys_pressed)

            moves_to_play, whether_to_shoot = get_move(red, yellow)

            for move in moves_to_play:
                yellow.x += move[0] * MOVEMENT_SPEED
                yellow.y += move[1] * MOVEMENT_SPEED

            if whether_to_shoot:
                current_time = time.time()

                if (current_time - start_time) - previous_time >= fire_time:
                    previous_time = current_time - start_time
                    yellow.shoot_bullet(BULLET_FIRE_SOUND)

        yellow.move_bullets_and_check_hit_with_other_spaceship(red, BULLET_HIT_SOUND)
        red.move_bullets_and_check_hit_with_other_spaceship(yellow, BULLET_HIT_SOUND)

        draw_window(window, red, yellow)

        winner_text = ""
        if red.get_health() <= 0:
            winner_text = "Yellow Wins!"

        if yellow.get_health() <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(window, winner_text)
            break

    pygame.quit()
    return yellow.get_health(), red.get_health()


if __name__ == "__main__":
    main()
