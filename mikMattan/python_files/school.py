import tkinter as tk

lst_of_subjects = ["mathematics", "madait handasit", "physics", "history", "hebrew", "bible", "english", "literature"]

TITLE_FONT_SIZE = 23
BTN_FONT_SIZE = 18

TITLE_FONT = ("Comic Sans MS", TITLE_FONT_SIZE)
BTN_FONT = ("Times New Roman", BTN_FONT_SIZE)

BC = "#61b52a"
BORDER_WIDTH = 7

ENT_WIDTH = 30
PAD_WIDGET = 20


def execute_command(window, selected_option, option_var):
    selected_option.set(option_var.get())
    window.destroy()


def main():
    ##  window  ##
    window = tk.Tk()
    window.title("School")
    window.resizable(False, False)
    window.configure(background=BC)

    option_var = tk.StringVar()
    selected_option = tk.StringVar()

    option_var.set(lst_of_subjects[0])  # Set the default selected option

    ##  url frame  ##
    url_frm = tk.Frame()
    url_frm.configure(background=BC)

    url_lbl = tk.Label(master=url_frm, text="Class option", font=TITLE_FONT, background=BC)
    option_menu = tk.OptionMenu(url_frm, option_var, *lst_of_subjects)
    option_menu.unbind('<Return>')
    url_lbl.pack(pady=PAD_WIDGET, padx=PAD_WIDGET)
    option_menu.pack(pady=PAD_WIDGET, padx=PAD_WIDGET)

    ## buttons frame ##
    btn_frm = tk.Frame()
    btn_frm.configure(background=BC)

    activate = tk.Button(master=btn_frm, text="Learn", font=BTN_FONT, borderwidth=BORDER_WIDTH, command=lambda: execute_command(window, selected_option, option_var))

    activate.grid(padx=PAD_WIDGET, pady=PAD_WIDGET, row=0, column=0)

    ## place frames ##
    url_frm.pack()
    btn_frm.pack()

    window.bind("<Return>", lambda event: execute_command(window, selected_option, option_var))
    window.mainloop()

    return option_var.get()


if __name__ == "__main__":
    main()
