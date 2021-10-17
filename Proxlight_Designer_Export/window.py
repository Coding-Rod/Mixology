from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("800x380")
window.configure(bg = "#eeeeee")
canvas = Canvas(
    window,
    bg = "#eeeeee",
    height = 380,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"Proxlight_Designer_Export/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 535, y = 171,
    width = 180,
    height = 80)

img1 = PhotoImage(file = f"Proxlight_Designer_Export/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 310, y = 171,
    width = 180,
    height = 80)

img2 = PhotoImage(file = f"Proxlight_Designer_Export/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 85, y = 171,
    width = 179,
    height = 80)

background_img = PhotoImage(file = f"Proxlight_Designer_Export/background.png")
background = canvas.create_image(
    400.0, 37.0,
    image=background_img)

img3 = PhotoImage(file = f"Proxlight_Designer_Export/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 725, y = 7,
    width = 60,
    height = 60)

window.resizable(False, False)
window.mainloop()