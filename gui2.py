


from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import Text_to_sign

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1644x967")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 967,
    width = 1644,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    60.0,
    231.0,
    1584.0,
    904.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    60.47412109375,
    68.3134765625,
    anchor="nw",
    text="Text to Sign Converter",
    fill="#000000",
    font=("Inter SemiBold", 53 * -1)
)

canvas.create_text(
    60.0,
    149.0,
    anchor="nw",
    text="Enter the text message to play converted sign language sequence",
    fill="#473C3C",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    599.0,
    282.0,
    anchor="nw",
    text="Enter Message",
    fill="#473C3C",
    font=("Inter SemiBold", 64 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    1644.0,
    47.035423278808594,
    fill="#1C005A",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Text_to_sign.say_words(entry_1.get("1.0", "end-1c")),
    relief="flat"
)
button_1.place(
    x=750.0,
    y=809.0,
    width=143.34605407714844,
    height=58.23433303833008
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    822.0,
    584.7950744628906,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=186.0,
    y=388.0,
    width=1272.0,
    height=391.59014892578125
)
window.resizable(False, False)
window.mainloop()
