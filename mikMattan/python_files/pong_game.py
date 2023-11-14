import pygame
import random
import time


pygame.font.init()


WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400
FPS = 60

BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/tabel_tennis.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))

BLUE = 3, 18, 87
BLACK = 0, 0, 0
WHITE = 255, 255, 255

PONG_BAT_WIDTH, PONG_BAT_HEIGHT = 5, 70
MOVEMENT_SPEED = 6

PAD_X_OF_BAT = 40
PAD_Y_OF_BAT = 10

PONG_BALL_DIMENSION = 20
WAIT_TIME_BETWEEN_EACH_LOST = 4
NUM_OF_HITS_TO_ACC = 3
TENNIS_BALL_PATH = "Assets/tennis_ball.png"

MINIMUM_SPEED = 3
MAXIMUM_SPEED = 8

ACCELERATION_HORIZONTAL = 0.75
ACCELERATION_VERTICAL = 0.5

WINNER_MAX_POINTS = 5


class PongBat:
    def __init__(self, x, y, up_key, down_key, points_x):
        self.pygame_rect_obj = pygame.Rect(x, y, PONG_BAT_WIDTH, PONG_BAT_HEIGHT)
        self.up_key = up_key
        self.down_key = down_key
        self.points = 0
        self.points_x = points_x

    def get_rect(self):
        return self.pygame_rect_obj

    def move_bat(self, key_pressed):
        if key_pressed[self.up_key]:
            if valid_move(self.pygame_rect_obj.y - MOVEMENT_SPEED):
                self.pygame_rect_obj.y -= MOVEMENT_SPEED
            else:
                self.pygame_rect_obj.y = 0

        if key_pressed[self.down_key]:
            if valid_move(self.pygame_rect_obj.y + MOVEMENT_SPEED + PONG_BAT_HEIGHT):
                self.pygame_rect_obj.y += MOVEMENT_SPEED
            else:
                self.pygame_rect_obj.y = WINDOW_HEIGHT - PONG_BAT_HEIGHT

    def add_point(self):
        self.points += 1

    def get_points(self):
        return self.points

    def get_points_x(self):
        return self.points_x

    def check_collision_with_ball(self, ball):
        if pygame.Rect.colliderect(self.pygame_rect_obj, ball.pygame_rect_obj):
            if self.pygame_rect_obj.x < WINDOW_WIDTH // 2:  # left half
                ball.set_coordinates(x=self.pygame_rect_obj.x + PONG_BAT_WIDTH)
            else:
                ball.set_coordinates(x=self.pygame_rect_obj.x)

            ball.ball_hit()


class PongBall:
    def __init__(self, x, y, image_path=None):
        self.pygame_rect_obj = pygame.Rect(x, y, PONG_BALL_DIMENSION, PONG_BALL_DIMENSION)
        self.movement_speed_horizontal = random.choice([1, -1])
        self.movement_speed_vertical = random.choice([1, -1])
        self.horizontal = random.randint(MINIMUM_SPEED, MAXIMUM_SPEED)
        self.vertical = MAXIMUM_SPEED - self.horizontal + 1
        self.hits = 0

        if image_path is not None:
            self.image = pygame.transform.scale(pygame.image.load(image_path), (PONG_BALL_DIMENSION, PONG_BALL_DIMENSION))
        else:
            self.image = None

    def get_rect(self):
        return self.pygame_rect_obj

    def get_coordinates(self):
        return self.pygame_rect_obj.x, self.pygame_rect_obj.y

    def set_coordinates(self, x=None, y=None):
        if x is not None:
            if x < WINDOW_WIDTH // 2:
                self.pygame_rect_obj.x = x
            else:
                self.pygame_rect_obj.x = x - PONG_BALL_DIMENSION

        if y is not None:
            self.pygame_rect_obj.y = y

    def move_ball(self):
        self.pygame_rect_obj.x += self.movement_speed_horizontal * self.horizontal
        self.pygame_rect_obj.y += self.movement_speed_vertical * self.vertical

    def check_collision_in_sides(self):
        if not valid_move(self.pygame_rect_obj.y) or not valid_move(self.pygame_rect_obj.y + PONG_BALL_DIMENSION):  # if hits upper/lower side
            self.movement_speed_vertical *= -1

            if self.pygame_rect_obj.y < WINDOW_HEIGHT // 2:  # upper half collision
                self.pygame_rect_obj.y = 0
            else:
                self.pygame_rect_obj.y = WINDOW_HEIGHT - PONG_BALL_DIMENSION

        if self.pygame_rect_obj.x + PONG_BALL_DIMENSION < 0 or self.pygame_rect_obj.x > WINDOW_WIDTH:  # if hits sides
            return PongBall(WINDOW_WIDTH // 2 - PONG_BALL_DIMENSION // 2, WINDOW_HEIGHT // 2 - PONG_BALL_DIMENSION // 2, TENNIS_BALL_PATH)

    def get_speed(self):
        return self.horizontal, self.vertical

    def set_speed(self, new_horizontal, new_vertical):
        self.horizontal, self.vertical = new_horizontal, new_vertical

    def get_movement_speed(self):
        return self.movement_speed_horizontal, self.movement_speed_vertical

    def set_movement_speed(self, horizontal=None, vertical=None):
        if horizontal is not None:
            self.movement_speed_horizontal = horizontal

        if vertical is not None:
            self.movement_speed_vertical = vertical

    def ball_hit(self):
        self.movement_speed_horizontal *= -1
        self.hits += 1

        if self.hits % 3 == 0:
            self.horizontal += ACCELERATION_HORIZONTAL
            self.vertical += ACCELERATION_VERTICAL


def valid_move(new_y):
    return 0 <= new_y <= WINDOW_HEIGHT


def draw_window(window, pong_bats, pong_ball, timer_text=None):
    TIMER_FONT = pygame.font.SysFont("comicsans", 70)
    POINTS_FONT = pygame.font.SysFont("comicsans", 50)

    window.blit(BACKGROUND, (0, 0))

    for bat in pong_bats:
        points_text = POINTS_FONT.render(f"{bat.get_points()}", 1, BLACK)
        window.blit(points_text, (bat.get_points_x(), 10))  # draw points

        pygame.draw.rect(window, BLUE, bat.get_rect())  # draw bat

    if pong_ball.image is None:
        pygame.draw.rect(window, BLUE, pong_ball.get_rect())  # draw ball
    else:
        window.blit(pong_ball.image, pong_ball.get_coordinates())

    if timer_text is not None:
        timer = TIMER_FONT.render(f"{timer_text}", 1, WHITE)

        window.blit(timer, (WINDOW_WIDTH // 2 - 20, 70))  # draw timer if exists

    pygame.display.update()


def draw_winner(window, winner_text):
    pygame.font.init()

    WINNER_FONT = pygame.font.SysFont("comicsans", 80)
    draw_text = WINNER_FONT.render(winner_text, 1, BLACK)
    window.blit(draw_text, (WINDOW_WIDTH // 2 - draw_text.get_width() // 2, WINDOW_HEIGHT - draw_text.get_height() - PAD_X_OF_BAT))

    pygame.display.update()
    pygame.time.delay(3000)


def main():
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pong Game")

    clock = pygame.time.Clock()
    start_time = time.time()

    pong_bat_left = PongBat(PAD_X_OF_BAT, PAD_Y_OF_BAT, pygame.K_w, pygame.K_s, WINDOW_WIDTH // 2 - 40 - 50)
    pong_bat_right = PongBat(WINDOW_WIDTH - PAD_X_OF_BAT - PONG_BAT_WIDTH, WINDOW_HEIGHT - PONG_BAT_HEIGHT - PAD_Y_OF_BAT, pygame.K_UP, pygame.K_DOWN, WINDOW_WIDTH // 2 + 40)
    pong_ball = PongBall(WINDOW_WIDTH // 2 - PONG_BALL_DIMENSION // 2, WINDOW_HEIGHT // 2 - PONG_BALL_DIMENSION // 2, TENNIS_BALL_PATH)

    to_exit = False
    no_ball = True
    while not to_exit:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                to_exit = True

        key_pressed = pygame.key.get_pressed()
        pong_bat_left.move_bat(key_pressed)
        pong_bat_right.move_bat(key_pressed)

        pong_bat_left.check_collision_with_ball(pong_ball)
        pong_bat_right.check_collision_with_ball(pong_ball)

        if not no_ball:
            output = pong_ball.check_collision_in_sides()

            if output is not None:  # if the method returned a new ball to play with (in case the current ball went out of the boundaries)
                if pong_ball.pygame_rect_obj.x < 0:
                    pong_bat_right.add_point()
                else:
                    pong_bat_left.add_point()

                start_time = time.time()
                no_ball = True
                del pong_ball

                pong_ball = output

            else:
                pong_ball.move_ball()

        if no_ball:
            current_time = time.time()

            stopwatch = current_time - start_time
            no_ball = stopwatch <= WAIT_TIME_BETWEEN_EACH_LOST - 1
            remaining_time = int(WAIT_TIME_BETWEEN_EACH_LOST - stopwatch)

            if remaining_time != 4 and remaining_time != 0:
                draw_window(window, [pong_bat_left, pong_bat_right], pong_ball, remaining_time)
            else:
                draw_window(window, [pong_bat_left, pong_bat_right], pong_ball)
        else:
            draw_window(window, [pong_bat_left, pong_bat_right], pong_ball)

        winner_text = "a"
        if pong_bat_left.get_points() >= WINNER_MAX_POINTS:
            winner_text = "Left Player Won!"
        elif pong_bat_right.get_points() >= WINNER_MAX_POINTS:
            winner_text = "Right Player Won!"

        if winner_text != "a":
            draw_winner(window, winner_text)
            break

    pygame.quit()
    return pong_bat_right.get_points(), pong_bat_left.get_points()


if __name__ == "__main__":
    main()
