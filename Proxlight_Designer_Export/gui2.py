from tkinter import *
from PIL import ImageTk

window = Tk()
window.geometry("800x380")
window.configure(bg = "#eeeeee")

def btn_clicked():
    print("Gattosva")

def startupPage():
    global window
    page1btn = Button(window, text="Page 1", command=page1)
    page2btn = Button(window, text="Page 2", command=page2)

    page1text = Label(window, text="This is page 1")
    page2text = Label(window, text="This is page 2")

    page1btn.pack()
    page2btn.pack()
    page1text.pack()

def page1():
    global window
    canvas = Canvas(
        window,
        bg = "#eeeeee",
        height = 380,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Proxlight_Designer_Export/background_2.png")
    background = canvas.create_image(0, 0,image=background_img)

    # img0 = PhotoImage(file = f"Proxlight_Designer_Export/img0.png")
    # b0 = Button(borderwidth = 0,highlightthickness = 0,command = btn_clicked,relief = "flat", image = img0)

    # b0.place(x = 535, y = 171,width = 180,height = 80)

    # img1 = PhotoImage(file = f"Proxlight_Designer_Export/img1.png")
    # b1 = Button(borderwidth = 0,highlightthickness = 0,command = btn_clicked,relief = "flat", image = img1)

    # b1.place(x = 310, y = 171,width = 180,height = 80)

    # img2 = PhotoImage(file = f"Proxlight_Designer_Export/img2.png")
    # b2 = Button(borderwidth = 0,highlightthickness = 0,command = btn_clicked,relief = "flat", image = img2)

    # b2.place(x = 85, y = 171,width = 179,height = 80)

    # img3 = ImageTk.PhotoImage(file = f"Proxlight_Designer_Export/img3.png")
    # b3 = Button(borderwidth = 0,highlightthickness = 0,command = btn_clicked,relief = "flat")

    # b3.place(x = 725, y = 7,width = 60,height = 60)


def page2():
    page1text.pack_forget()
    page2text.pack()

startupPage()

# window.resizable(False, False)
window.mainloop()