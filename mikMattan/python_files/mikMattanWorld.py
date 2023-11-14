import pygame
import single_two_player_choice
import snake
import settings_window
import encryption
import pop_allert
from time import time
import restaurant_menu
import school
import mikMattanClient
import json


pygame.init()
pygame.font.init()

#  window settings
WINDOW_WIDTH, WINDOW_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
FPS = 60

CROSSROAD_BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/crossroad_background.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
GYM_RESTAURANT_BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/gym_restaurant_background.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
SCHOOL_BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/school_background.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
ARCADE_BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/arcade_background.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))

ICON_DIM = int(WINDOW_WIDTH * 0.0390625)
ICON_Y = WINDOW_HEIGHT // 1.8

INFO_ICON = pygame.transform.scale(pygame.image.load("Assets/info_icon.png"), (ICON_DIM, ICON_DIM))
INFO_RECT = pygame.Rect(0, ICON_Y, ICON_DIM, ICON_DIM)

CROSSROAD_INFO = pygame.transform.scale(pygame.image.load("Assets/crossroad_info.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
ARCADE_INFO = pygame.transform.scale(pygame.image.load("Assets/arcade_info.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))

FONT_COLOR = 255, 255, 255

MATTAN_WIDTH, MATTAN_HEIGHT = int(WINDOW_WIDTH // 12.8), int(WINDOW_HEIGHT // 3.6)
MATTAN_SPEED = int(MATTAN_WIDTH // 20)

PAD_X, PAD_Y = int(WINDOW_WIDTH // 256) * 2, int(WINDOW_HEIGHT // 72) * 2

CROSSROAD_BORDER = pygame.transform.scale(pygame.image.load("Assets/crossroad_border.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
SCHOOL_BORDER = pygame.transform.scale(pygame.image.load("Assets/school_border.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
GYM_RESTAURANT_BORDER = pygame.transform.scale(pygame.image.load("Assets/gym_restaurant_border.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
ARCADE_BORDER = pygame.transform.scale(pygame.image.load("Assets/arcade_border.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))

BACKGROUNDS = [(CROSSROAD_BACKGROUND, CROSSROAD_BORDER), (GYM_RESTAURANT_BACKGROUND, GYM_RESTAURANT_BORDER), (ARCADE_BACKGROUND, ARCADE_BORDER), (SCHOOL_BACKGROUND, SCHOOL_BORDER), (None, None)]

GO_TO_CROSSROAD = pygame.USEREVENT + 1
GO_TO_GYM_RESTAURANT = pygame.USEREVENT + 2
GO_TO_ARCADE = pygame.USEREVENT + 3
GO_TO_SCHOOL = pygame.USEREVENT + 4
GO_TO_SETTINGS = pygame.USEREVENT + 5
PLAY_SNAKE = pygame.USEREVENT + 6
PLAY_SPACEGAME = pygame.USEREVENT + 7
PLAY_PONG = pygame.USEREVENT + 8
WORK_OUT = pygame.USEREVENT + 9
LEARN = pygame.USEREVENT + 10
EAT = pygame.USEREVENT + 11


EXIT_CODE_STARFIGHTERS = 100
EXIT_CODE_PONG = 200


class Mattan:
    def __init__(self, current_world=None, x=None, y=None, name=None, direction=None, proportion_x=None, proportion_y=None):
        # pygame attributes
        self.mattan_left = pygame.transform.scale(pygame.image.load("Assets/mattan_left.png"), (MATTAN_WIDTH, MATTAN_HEIGHT))
        self.mattan_right = pygame.transform.scale(pygame.image.load("Assets/mattan_right.png"), (MATTAN_WIDTH, MATTAN_HEIGHT))
        self.direction = True  # True for left False for right
        self.pygame_rect_obj = pygame.Rect(WINDOW_WIDTH // 2 - MATTAN_WIDTH // 2, WINDOW_HEIGHT - MATTAN_HEIGHT - 50, MATTAN_WIDTH, MATTAN_HEIGHT)
        self.current_place = 0
        self.draw = True
        self.proportion_x = 1
        self.proportion_y = 1
        self.current_time = 0

        # mattan attributes
        self.hunger = 7
        self.fun = 3
        self.pumped = 3
        self.iq = 90
        self.name = "my mattan"

        if current_world is not None:
            self.current_place = current_world

        if x is not None:
            self.pygame_rect_obj.x = x

        if y is not None:
            self. pygame_rect_obj.y = y

        if name is not None:
            self.name = name

        if direction is not None:
            self.direction = direction

        if proportion_x is not None:
            self.proportion_x = proportion_x

        if proportion_y is not None:
            self.proportion_y = proportion_y

    def __str__(self):
        return f"Name: {self.name}\nHunger: {self.hunger}\nFun: {self.fun}\nPumped: {self.pumped}\nIQ: {self.iq}\n"

    def return_dict_of_data(self):
        return {
            "current_world": self.current_place,
            "x": self.pygame_rect_obj.x,
            "y": self.pygame_rect_obj.y,
            "name": self.name,
            "direction": self.direction,
            "window_width": WINDOW_WIDTH,
            "window_height": WINDOW_HEIGHT
        }

    def get_image(self):
        if self.direction:
            return self.mattan_right
        return self.mattan_left

    def get_draw(self):
        return self.draw

    def set_draw(self, draw):
        self.draw = draw

    def get_coordinates(self):
        return self.pygame_rect_obj.x, self.pygame_rect_obj.y

    def set_direction(self, new_direction):
        self.direction = new_direction

    def get_direction(self):
        return self.direction

    def get_coordinates_for_checking_border(self, move_x, move_y):
        return self.pygame_rect_obj.x + move_x, self.pygame_rect_obj.y + MATTAN_HEIGHT + move_y

    def change_world(self, current_world, world_to_go_to):
        new_x, new_y = 0, WINDOW_HEIGHT - int(1.25*MATTAN_HEIGHT)

        if current_world == 0:  # if from crossroad to somewhere
            if world_to_go_to in (1, 3):  # if to gym_restaurant or schools
                new_x = MATTAN_WIDTH
            else:
                new_x = WINDOW_WIDTH - MATTAN_WIDTH * 2
        else:  # if to crossroad
            if current_world == 1:  # if from gym_restaurant
                new_x = WINDOW_WIDTH - MATTAN_WIDTH * 2

            elif current_world == 2:  # if from arcade
                new_x = MATTAN_WIDTH

            elif current_world == 3:  # if from school
                new_x, new_y = int(WINDOW_WIDTH * 0.859375), int(WINDOW_HEIGHT // 2.88)

        self.pygame_rect_obj.x, self.pygame_rect_obj.y = new_x, new_y

    def move_mattan(self, key_pressed):
        if key_pressed[pygame.K_LEFT]:  # left
            if 0 <= self.pygame_rect_obj.x - MATTAN_SPEED:
                if check_border(self, self.get_coordinates_for_checking_border(-1*MATTAN_SPEED, 0)):
                    self.pygame_rect_obj.x -= MATTAN_SPEED
                    self.set_direction(True)

        if key_pressed[pygame.K_RIGHT]:  # right
            if WINDOW_WIDTH >= self.pygame_rect_obj.x + MATTAN_SPEED + MATTAN_WIDTH:
                if check_border(self, self.get_coordinates_for_checking_border(MATTAN_SPEED, 0)):
                    self.pygame_rect_obj.x += MATTAN_SPEED
                    self.set_direction(False)

        if key_pressed[pygame.K_UP]:  # up
            if check_border(self, self.get_coordinates_for_checking_border(0, -1*MATTAN_SPEED)):
                self.pygame_rect_obj.y -= MATTAN_SPEED

        if key_pressed[pygame.K_DOWN]:  # down
            if check_down(self.pygame_rect_obj.y + MATTAN_SPEED) and check_border(self, self.get_coordinates_for_checking_border(0, MATTAN_SPEED)):
                self.pygame_rect_obj.y += MATTAN_SPEED

    def get_place(self):
        return self.current_place

    def set_place(self, new_place):
        self.current_place = new_place

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def play(self, game_code):
        if game_code == 0:
            self.pygame_rect_obj.x -= PAD_X
            self.pygame_rect_obj.y += PAD_Y
            self.direction = True
            self.fun += snake.play() // 2

        elif game_code == 1:
            pass

        else:
            pass

    def load_data(self):
        key = get_key()

        if key is not None:
            try:
                with open("data.mattan", "rb") as file:
                    all_data = file.read()
                    decrypted_data = encryption.decrypt(all_data, key).split("|")

                    self.hunger = int(decrypted_data[0])
                    self.fun = int(decrypted_data[1])
                    self.pumped = int(decrypted_data[2])
                    self.iq = int(decrypted_data[3])
                    self.name = decrypted_data[4]
            except FileNotFoundError:
                pass

    def save_data(self):
        key = encryption.generate_key()
        with open("key.mattan", "wb") as file:
            file.write(str(key).encode())

        with open("data.mattan", "wb") as file:
            file.write(encryption.encrypt(("|".join([str(self.hunger), str(self.fun), str(self.pumped), str(self.iq), self.name])), key))

    def work_out(self):
        self.direction = False
        self.pygame_rect_obj.y += PAD_Y
        self.pygame_rect_obj.x += PAD_X
        if self.pumped > 15:
            pop_allert.pop_msg("Info", "Mattan is already pumped")

        else:

            self.pumped += 4
            self.hunger += 3
            self.fun += 1
            self.set_draw(False)

    def eat(self):
        self.direction = True
        self.pygame_rect_obj.y += PAD_Y
        self.pygame_rect_obj.x -= PAD_X
        if self.hunger < 2:
            pop_allert.pop_msg("Info", "Mattan is not hungry")

        else:
            food = restaurant_menu.main()

            if food is not None and food != "error":
                self.hunger -= len(food)
                self.pumped -= 2
                self.fun -= 2

    def learn(self):
        self.direction = True
        self.pygame_rect_obj.x -= PAD_X
        self.pygame_rect_obj.y += PAD_Y

        subject = school.main()

        self.iq += len(subject)
        self.hunger += 3
        self.fun -= len(subject) // 2
        self.pumped -= 2

    def check_attributes(self):
        if self.fun < 0:
            self.fun = 0

        if self.hunger < 0:
            self.hunger = 0

        if self.pumped < 0:
            self.pumped = 0

        if self.iq < 0:
            self.iq = 0

    def set_current_time(self):
        self.current_time = time()

    def get_saved_time(self):
        return self.current_time


BACKGROUND_DICT = {"crossroad": 0,
                   "gym_restaurant": 1,
                   "arcade": 2,
                   "school": 3}


GAMES_DICT = {"snake": 0,
              "pong": 1,
              "spacegame": 2}


INFO_COORDINATES = {0: (int(WINDOW_WIDTH * 0.515625), ICON_Y),
                    2: (int(WINDOW_WIDTH * 0.4453125), ICON_Y)}

with open("server_info.txt", "r") as server_info:
    lines = server_info.read().split("\n")
    SERVER_IP = lines[0]
    SERVER_PORT = int(lines[1])


def get_key():
    try:
        with open("key.mattan", "rb") as file:
            key = int(file.read().decode())
            return key
    except FileNotFoundError:
        with open("key.mattan", "wb") as file:
            file.write(str(encryption.generate_key()).encode())


def turn_list_of_dicts_to_mattans(data):
    lst_of_mattans = list()
    for mattan in data:
        lst_of_mattans.append(Mattan(current_world=mattan["current_world"], x=mattan["x"], y=mattan["y"], name=mattan["name"], direction=mattan["direction"], proportion_x=WINDOW_WIDTH / mattan["window_width"], proportion_y=WINDOW_HEIGHT / mattan["window_height"]))

    return lst_of_mattans


def run_pygame_game(game, results):
    results.put(game())


def check_color(color):
    if color == [0, 0, 190]:  # blue
        pygame.event.post(pygame.event.Event(GO_TO_GYM_RESTAURANT))

    elif color == [255, 255, 25]:
        pygame.event.post(pygame.event.Event(GO_TO_SCHOOL))

    elif color == [255, 0, 0]:  # red
        pygame.event.post(pygame.event.Event(GO_TO_CROSSROAD))

    elif color == [0, 255, 0]:  # green
        pygame.event.post(pygame.event.Event(GO_TO_ARCADE))

    elif color == [146, 44, 85]:
        pygame.event.post(pygame.event.Event(GO_TO_SETTINGS))

    elif color == [66, 107, 124]:
        pygame.event.post(pygame.event.Event(PLAY_SPACEGAME))

    elif color == [142, 24, 166]:
        pygame.event.post(pygame.event.Event(PLAY_PONG))

    elif color == [182, 99, 8]:
        pygame.event.post(pygame.event.Event(PLAY_SNAKE))

    elif color == [167, 23, 92]:
        pygame.event.post(pygame.event.Event(WORK_OUT))

    elif color == [117, 73, 109]:
        pygame.event.post(pygame.event.Event(EAT))

    elif color == [87, 140, 60]:
        pygame.event.post(pygame.event.Event(LEARN))


def check_border(mattan, coordinates):
    x, y = coordinates

    color = list(BACKGROUNDS[mattan.get_place()][1].get_at(coordinates))[:3]
    check_color(color)
    result = color.count(0) != 3

    color = list(BACKGROUNDS[mattan.get_place()][1].get_at((x + MATTAN_WIDTH, y)))[:3]
    check_color(color)
    return color.count(0) != 3 and result


def check_down(y):
    return WINDOW_HEIGHT - MATTAN_HEIGHT - PAD_Y > y


def draw_window(window, my_mattan, mattans):
    NAME_FONT = pygame.font.Font(None, int(MATTAN_HEIGHT // 10))

    window.blit(BACKGROUNDS[my_mattan.get_place()][0], (0, 0))

    try:
        window.blit(INFO_ICON, INFO_COORDINATES[my_mattan.get_place()])
        INFO_RECT.x = INFO_COORDINATES[my_mattan.get_place()][0]
    except KeyError:
        pass

    all_mattans = [my_mattan] + mattans

    for mattan in all_mattans:
        if mattan.get_draw() and mattan.get_place() == my_mattan.get_place():
            x, y = mattan.get_coordinates()
            x *= mattan.proportion_x
            y *= mattan.proportion_y

            window.blit(mattan.get_image(), (x, y))  # draw all the other mattans in the server

            if not mattan.get_direction():
                x += PAD_X * 2

            text = NAME_FONT.render(mattan.get_name(), True, (0, 0, 0))
            label_rect = text.get_rect()
            label_rect.center = (x + PAD_X * 4, y - PAD_Y // 2)

            window.blit(text, label_rect)

    pygame.display.update()  # update the window


def draw_info(window, mattan):
    TEXT_FONT = pygame.font.Font(None, int(MATTAN_HEIGHT // 4))
    world = mattan.get_place()

    if world == BACKGROUND_DICT["crossroad"]:
        window.blit(CROSSROAD_INFO, (0, 0))
    elif world == BACKGROUND_DICT["arcade"]:
        window.blit(ARCADE_INFO, (0, 0))

    text = TEXT_FONT.render("Exit by pressing esc", True, (0, 0, 0))
    label_rect = text.get_rect()
    label_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 9.6)

    window.blit(text, label_rect)

    pygame.display.update()  # update the window


def check_event(event, mattan):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
        pop_allert.pop_msg("Data", mattan)

    if event.type == GO_TO_CROSSROAD:
        return BACKGROUND_DICT["crossroad"]

    elif event.type == GO_TO_GYM_RESTAURANT:
        return BACKGROUND_DICT["gym_restaurant"]

    elif event.type == GO_TO_ARCADE:
        return BACKGROUND_DICT["arcade"]

    elif event.type == GO_TO_SCHOOL:
        return BACKGROUND_DICT["school"]

    elif event.type == GO_TO_SETTINGS:
        mattan.direction = False
        mattan.pygame_rect_obj.x += PAD_X * 6
        mattan.pygame_rect_obj.y += PAD_Y * 4

        new_name = settings_window.main()

        if new_name != "Enter new name here":
            mattan.set_name(new_name)

    elif event.type == PLAY_SPACEGAME:
        single_two_players = single_two_player_choice.main()
        with open("runtime_msg.mattan", "wb") as file:
            get_key()
            key = get_key()
            file.write(encryption.encrypt(f"{EXIT_CODE_STARFIGHTERS}|{int(single_two_players)}|{json.dumps(list(mattan.return_dict_of_data().values()))}", key))
        raise EnvironmentError

    elif event.type == PLAY_PONG:
        single_two_players = single_two_player_choice.main()
        with open("runtime_msg.mattan", "wb") as file:
            get_key()
            key = get_key()
            file.write(encryption.encrypt(f"{EXIT_CODE_PONG}|{int(single_two_players)}|{json.dumps(list(mattan.return_dict_of_data().values()))}", key))
        raise EnvironmentError

    elif event.type == PLAY_SNAKE:
        mattan.play(GAMES_DICT["snake"])

    elif event.type == WORK_OUT:
        mattan.set_current_time()
        mattan.work_out()

    elif event.type == EAT:
        mattan.eat()

    elif event.type == LEARN:
        mattan.learn()


def main(current_world=None, x=None, y=None, direction=None, play=None):
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("MikMattan")
    mattan = Mattan(current_world=current_world, x=x, y=y, direction=direction)
    mattan.load_data()
    world_to_go_to = None
    reading_info = False

    clock = pygame.time.Clock()
    to_exit = False

    sock = mikMattanClient.open_socket(SERVER_IP, SERVER_PORT)
    able_to_connect = sock is not None
    print(able_to_connect)
    all_mattans_in_world = list()

    if play is not None:
        mattan.fun += play

    while not to_exit:
        clock.tick(FPS)

        mattan.move_mattan(pygame.key.get_pressed())

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    not reading_info and (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                to_exit = True

            elif reading_info and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                reading_info = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_RECT.collidepoint(event.pos):
                    reading_info = True

            world_to_go_to = check_event(event, mattan)

        if world_to_go_to is not None:  # set different world
            mattan.change_world(mattan.get_place(), world_to_go_to)
            mattan.set_place(world_to_go_to)
            world_to_go_to = None

        if able_to_connect:  # socket things
            try:
                mikMattanClient.send_data(sock, mattan.return_dict_of_data())
                list_of_data = mikMattanClient.receive_data(sock)

                if list_of_data is not None:
                    all_mattans_in_world = turn_list_of_dicts_to_mattans(list_of_data)

            except Exception:
                pass

        if reading_info:  # in case character reading info
            draw_info(window, mattan)
        else:
            draw_window(window, mattan, all_mattans_in_world)

        if not mattan.get_draw():
            new_timer = time()

            if new_timer - mattan.get_saved_time() > 2:
                mattan.set_draw(True)

        mattan.check_attributes()

    pygame.quit()
    mattan.save_data()

    if able_to_connect:
        mikMattanClient.close_socket(sock)


if __name__ == "__main__":
    main()
