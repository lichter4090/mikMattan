import tkinter as tk

PAD_WIDGET = 20
BTN_FONT = ("Times New Roman", 18)
BORDER_WIDTH = 7
BC = "#61b52a"


result = None


def return_result(window, num):
    global result
    window.destroy()

    result = num == 1


def main():
    window = tk.Tk()
    window.resizable(False, False)
    window.title("Single player or two players")
    window.configure(background=BC)

    single_player = tk.Button(window, text="Single player", font=BTN_FONT, borderwidth=BORDER_WIDTH, command=lambda: return_result(window, 0))
    two_players = tk.Button(window, text="Two players", font=BTN_FONT, borderwidth=BORDER_WIDTH, command=lambda: return_result(window, 1))

    single_player.grid(padx=PAD_WIDGET, pady=PAD_WIDGET, row=0, column=0)
    two_players.grid(padx=PAD_WIDGET, pady=PAD_WIDGET, row=0, column=PAD_WIDGET)

    window.mainloop()

    return result  # if returns True - two players else single player


if __name__ == "__main__":
    main()
