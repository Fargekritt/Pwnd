import tkinter as tk
import pwnd

HEIGHT = 700
WIDTH = 900
window_title = "have you been pwned?"
font_size = "Helvetica 15"


def button_click(entry):
    _sha1pwd, count = pwnd.lookup_pwned_api(entry)
    if count == 0:
        label["text"] = "Your password has not been leaked!\n"
    else:
        label["text"] = "Change password now! its been leaked %s times\n" % (
            count)


root = tk.Tk()
root.title(window_title)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)

frame = tk.Frame(root, bg="blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75,
            relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=font_size)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Check password", font=font_size,
                   command=lambda: button_click(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="blue", bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor="n")

label = tk.Label(lower_frame,
                 anchor="nw", justify="left", bd=4, font=font_size)
label.place(relwidth=1, relheight=1)

root.mainloop()
