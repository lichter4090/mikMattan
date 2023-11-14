import tkinter as tk

TITLE_FONT_SIZE = 23
BTN_FONT_SIZE = 18
ENT_FONT_SIZE = 20

TITLE_FONT = ("Comic Sans MS", TITLE_FONT_SIZE)
ENT_FONT = ("David", ENT_FONT_SIZE)
BTN_FONT = ("Times New Roman", BTN_FONT_SIZE)

BC = "#61b52a"
BORDER_WIDTH = 7

ENT_WIDTH = 30
PAD_WIDGET = 20

DEFAULT_ENTRY_VALUE = "Enter new name here"


name = None


def execute_command(window, entry):
    global name

    name = entry.get()
    window.destroy()


def main():
    ##  window  ##
    window = tk.Tk()
    window.title("Settings window")
    window.resizable(False, False)
    window.configure(background=BC)

    ##  url frame  ##
    url_frm = tk.Frame()
    url_frm.configure(background=BC)

    url_lbl = tk.Label(master=url_frm, text="Settings", font=TITLE_FONT, background=BC)
    name_ent = tk.Entry(master=url_frm, font=ENT_FONT, width=ENT_WIDTH)

    name_ent.insert(0, DEFAULT_ENTRY_VALUE)

    name_ent.bind("<FocusIn>", lambda event: name_ent.delete(0, tk.END))  # Bind event handler for clicking on the Entry

    url_lbl.pack(pady=PAD_WIDGET, padx=PAD_WIDGET)
    name_ent.pack(pady=PAD_WIDGET, padx=PAD_WIDGET)

    ## buttons frame ##
    btn_frm = tk.Frame()
    btn_frm.configure(background=BC)

    activate = tk.Button(master=btn_frm, text="confirm", font=BTN_FONT, borderwidth=BORDER_WIDTH, command=lambda: execute_command(window, name_ent))

    activate.grid(padx=PAD_WIDGET, pady=PAD_WIDGET, row=0, column=0)

    ## place frames ##
    url_frm.pack()
    btn_frm.pack()

    window.bind("<Return>", lambda event=None: execute_command(window, name_ent))
    window.mainloop()

    return name


if __name__ == "__main__":
    main()
