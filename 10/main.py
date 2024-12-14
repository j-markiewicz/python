import tkinter as tk
from secrets import randbelow
from tkinter import ttk

root = tk.Tk()
root.title("Kostki")

frame = tk.Frame(root)
frame.pack(anchor=tk.CENTER)

style = ttk.Style()
style.configure(
    "Result.TLabel",
    foreground="black",
    background="white",
    font="default 96",
)

images = {
    "dice": tk.PhotoImage(file="./icons/dice.png"),
    2: tk.PhotoImage(file="./icons/d2.png"),
    4: tk.PhotoImage(file="./icons/d4.png"),
    6: tk.PhotoImage(file="./icons/d6.png"),
    8: tk.PhotoImage(file="./icons/d8.png"),
    10: tk.PhotoImage(file="./icons/d10.png"),
    12: tk.PhotoImage(file="./icons/d12.png"),
    20: tk.PhotoImage(file="./icons/d20.png"),
}

result = tk.StringVar()
ttk.Label(frame, textvariable=result, style="Result.TLabel").grid(
    column=0, columnspan=7, row=0
)

image = ttk.Label(frame, image=images["dice"])
image.grid(column=0, columnspan=7, row=0)


def roll(sides):
    def roll_inner():
        global image
        image.destroy()
        image = ttk.Label(frame, image=images[sides])
        image.grid(column=0, columnspan=7, row=0)
        image.lower()
        result.set(str(randbelow(sides) + 1))

    return roll_inner


ttk.Button(frame, text="D2", command=roll(2)).grid(column=0, row=1)
ttk.Button(frame, text="D4", command=roll(4)).grid(column=1, row=1)
ttk.Button(frame, text="D6", command=roll(6)).grid(column=2, row=1)
ttk.Button(frame, text="D8", command=roll(8)).grid(column=3, row=1)
ttk.Button(frame, text="D10", command=roll(10)).grid(column=4, row=1)
ttk.Button(frame, text="D12", command=roll(12)).grid(column=5, row=1)
ttk.Button(frame, text="D20", command=roll(20)).grid(column=6, row=1)

root.mainloop()
