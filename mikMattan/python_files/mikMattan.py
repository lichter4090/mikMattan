import mikMattanWorld
import starfighters_battle
import starfighters_battle_bot
import pong_game
import pong_bot


def run_game(exit_code, single_two_players):
    if exit_code == mikMattanWorld.EXIT_CODE_STARFIGHTERS:
        if single_two_players:
            right, left = starfighters_battle.main()

        else:
            right, left = starfighters_battle_bot.main()

        return starfighters_battle.STARTER_HEALTH - right + starfighters_battle_bot.STARTER_HEALTH - left

    elif exit_code == mikMattanWorld.EXIT_CODE_PONG:
        if single_two_players:
            right, left = pong_game.main()

        else:
            right, left = pong_bot.main()

        return right + left


def main(info, play=None):
    try:
        mikMattanWorld.main(info[0], info[1], info[2], info[3], play)
        return

    except EnvironmentError:
        try:
            with open("runtime_msg.mattan", "rb") as file:
                key = mikMattanWorld.get_key()

                data = mikMattanWorld.encryption.decrypt(file.read(), key)

            lst_of_data = [int(data.split("|")[0]), int(data.split("|")[1]), mikMattanWorld.json.loads(data.split("|")[2])]

            fun = run_game(lst_of_data[0], lst_of_data[1])

            lst_of_data[2][1] += mikMattanWorld.PAD_X
            lst_of_data[2][2] += mikMattanWorld.PAD_Y
            lst_of_data[2][3] = False

            return main(lst_of_data[2], fun)
        except Exception:
            pass


if __name__ == "__main__":
    main([None, None, None, None, None, None, None])
