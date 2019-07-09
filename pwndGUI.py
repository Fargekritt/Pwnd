import tkinter as tk
import pwnd

HEIGHT = 700
WIDTH = 900


def button_click(entry):
    _sha1pwd, count = pwnd.lookup_pwned_api(entry)
    if count == 0:
        label["text"] = "Your password has not been leaked!\n"
    else:
        label["text"] = "Change password now! its been leaked %s times\n" % (
            count)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75,
            relheight=0.1, anchor="n")

entry = tk.Entry(frame,)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="button",
                   command=lambda: button_click(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="blue", bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor="n")

label = tk.Label(lower_frame,
                 anchor="nw", justify="left", bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
