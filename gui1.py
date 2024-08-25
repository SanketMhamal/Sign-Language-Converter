


from pathlib import Path
import subprocess 
import Sign_to_text
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def open_gui2():
    subprocess.Popen(["python", "gui2.py"])

window = Tk()

window.geometry("1644x967")
window.configure(bg = "#FFFFFF")

def run():
    with open("build\gui2.py") as f:
     code = f.read()
     exec(code)

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
    60.47412109375,
    230.697509765625,
    1583.52587890625,
    564.4250183105469,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    60.47412109375,
    582.34326171875,
    1583.52587890625,
    916.0707702636719,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    60.0,
    64.0,
    anchor="nw",
    text="Sign Language Converter app",
    fill="#000000",
    font=("Inter SemiBold", 53 * -1)
)

canvas.create_text(
    60.0,
    149.0,
    anchor="nw",
    text="Communicate using American Sign Language",
    fill="#473C3C",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    394.20166015625,
    287.81201171875,
    anchor="nw",
    text="Sign Language to text converter",
    fill="#473C3C",
    font=("Inter SemiBold", 26 * -1)
)

canvas.create_text(
    394.20166015625,
    324.768310546875,
    anchor="nw",
    text="Convert sign language to text in real time \n[press q to quit]",
    fill="#473C3C",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    394.20166015625,
    657.93603515625,
    anchor="nw",
    text="Text to Sign Language Converter",
    fill="#473C3C",
    font=("Inter SemiBold", 26 * -1)
)

canvas.create_text(
    394.20166015625,
    694.892333984375,
    anchor="nw",
    text="Convert text message to sign language",
    fill="#473C3C",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    1644.0,
    47.035423278808594,
    fill="#1C005A",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    220.8310546875,
    395.73291015625,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    226.4306640625,
    750.73828125,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Sign_to_text.run_sign_to_text(),
    relief="flat"
)
button_1.place(
    x=394.20166015625,
    y=456.91552734375,
    width=143.34605407714844,
    height=58.23433303833008
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_gui2(),
    relief="flat"
)
button_2.place(
    x=394.20166015625,
    y=811.9208984375,
    width=154.54495239257812,
    height=58.23433303833008
)
window.resizable(False, False)
window.mainloop()
