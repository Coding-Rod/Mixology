#from apis.data import Data
import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
# from apis.control import Control

#dat = Data()
# ctr = Control()

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Roboto', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageOne_trash, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    #TODO: Organize items
    #TODO: Change colors
    #TODO: Add icons
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        canvas = tk.Canvas(bg = "#eeeeee",height = 380,width = 800,bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)
        
        img0 = tk.PhotoImage(file = f"Proxlight_Designer_Export/img0.png")
        b0 = tk.Button(image = img0, borderwidth = 0, highlightthickness = 0, command = lambda: print("Pattosva"), relief = "flat")

        b0.place(x = 535, y = 171, width = 180, height = 80)

        img1 = tk.PhotoImage(file = f"Proxlight_Designer_Export/img1.png")
        b1 = tk.Button(image = img1, borderwidth = 0, highlightthickness = 0, command = lambda: print("Pattosva"), relief = "flat")

        b1.place(x = 310, y = 171, width = 180, height = 80)

        img2 = tk.PhotoImage(file = f"Proxlight_Designer_Export/img2.png")
        b2 = tk.Button(image = img2,borderwidth = 0,highlightthickness = 0,command = lambda: print("Pattosva"),relief = "flat")

        b2.place(x = 85, y = 171,width = 179,height = 80)

        background_img = tk.PhotoImage(file = f"Proxlight_Designer_Export/background.png")
        background = canvas.create_image(400.0, 37.0,image=background_img)

        img3 = tk.PhotoImage(file = f"Proxlight_Designer_Export/img3.png")
        b3 = tk.Button(image = img3, borderwidth = 0, highlightthickness = 0, command = lambda: print("Pattosva"), relief = "flat")

        b3.place(x = 725, y = 7,width = 60,height = 60)


class PageOne(tk.Frame):
    #TODO: Make scrollable
    #TODO: Organize items
    #TODO: Change colors
    #TODO: Add icons
    #TODO: Include data functions
    #TODO: Include control functions

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        t_button = tk.Button(self, text="Trash",
                           command=lambda: controller.show_frame("PageOne_trash"))
        button.pack()
        t_button.pack()
class PageOne_trash(tk.Frame):
    #TODO: Make scrollable
    #TODO: Organize items
    #TODO: Change colors
    #TODO: Add icons
    #TODO: Include data functions
    #TODO: Include control functions

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1 (trash)", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="done",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()


class PageTwo(tk.Frame):
    #TODO: Make scrollable
    #TODO: Organize items
    #TODO: Change colors
    #TODO: Add icons
    #TODO: Include data functions
    #TODO: Include control functions

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
class PageThree(tk.Frame):
    #TODO: Make scrollable
    #TODO: Organize items
    #TODO: Change colors
    #TODO: Add icons
    #TODO: Include data functions
    #TODO: Include control functions

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("800x380")
    app.configure(bg = "#eeeeee")
    app.mainloop()